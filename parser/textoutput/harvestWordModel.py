import xml.sax
import sys
import nltk
from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer
import MySQLdb, MySQLdb.cursors
import string
import csv
import time
import os
import json

_connection = None
db = None
start_time = None
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
data = None

def get_speaker_info(generic_id, personTF):
	if generic_id == "unknown": 
		return "unknown"
	if generic_id is None:
		return "none"
	person_id = ""
	if (personTF):
		person_id = generic_id
	else:
		person_id = getPersonFromMember(generic_id)

	details = getPersonDetails(person_id)
	name = "missing"

	count = 0
	for det in details["other_names"]:
		if det["note"] == 'Main':
			if 'family_name' in det:
				gn = det["given_name"].encode("utf-8")
				fn = det["family_name"].encode("utf-8")
				name = gn + "_" + fn
		count = count + 1 
	return name
	
	
def getPersonDetails(key):
    global data
    for record in data["persons"]:
        if record["id"] == key:
		return record

def getPersonFromMember(key):
    global data
    for record in data["memberships"]:
        if record["id"] == key:
		return record["person_id"]

def main(argument):
	global db
	global start_time 
	global data
	with open('people.json') as data_file:    
	    data = json.load(data_file)


	start_time = time.time()
	path = '/home/AccHack14/harvester/hansard/'

	if argument is not None:
		filename = os.path.dirname(argument)
	db_filename = filename
	debatedate = filename[7:17]
	fullpath = path + filename
	fullpath = argument
	parse(fullpath, debatedate, filename, db_filename)

def parse(contentsource, debatedate, filename, db_filename):
	source = open(contentsource)
	c = HansardContentHandler()
	c.debatedate = debatedate
	c.filename = filename
	c.db_filename = db_filename
	c.year = filename[7:11]
	xml.sax.parse(source, c)

def html_special_chars(text):
	return text.replace(u"&", u"&amp;").replace(u"<", u"<lt;").replace(u">", u">gt;").replace(u"\n",u" ").replace(u"\t",u" ").encode('ascii', 'ignore').encode('latin1','ignore').strip()



class HansardContentHandler(xml.sax.ContentHandler):

	def __init__(self):
		self.year = '1600'
		self.debatedate = '1600-01-01'
		self.filename = 'notfound.xml'
	        self.db_filename = 'notfound.xml'
		self.section_name = "NOT_IN_DOC"
	        self.majorheading = dict()
	        self.majorheading['text'] = ''
	        self.minorheading = dict()
	        self.minorheading['text'] = ''
	        self.speech = dict()
	        self.speech['text'] = ''
	        self.division = dict()
	        self.last_major_heading = ""
	        self.last_minor_heading = ""
		xml.sax.ContentHandler.__init__(self)

	def startElement(self, name, attrs):
		

		if name.lower() == "major-heading":
			self.majorheading['type'] = "MAJOR-HEADING"
			self.majorheading['id'] = attrs.get("id")
			self.majorheading['nospeaker'] = attrs.get("nospeaker")
			self.majorheading['colnum'] = attrs.get("colnum")
			self.majorheading['time'] = attrs.get("time")
			self.majorheading['url'] = attrs.get("url")
			self.majorheading['date'] = self.debatedate
			self.majorheading['text'] = ""
			self.section_name = "MAJOR-HEADING"

		elif name.lower == "minor-heading":
			self.minorheading['type'] = "MINOR-HEADING"
			self.minorheading['id'] = attrs.get("id")
			self.minorheading['nospeaker'] = attrs.get("nospeaker")
			self.minorheading['colnum'] = attrs.get("colnum")
			self.minorheading['time'] = attrs.get("time")
			self.minorheading['url'] = attrs.get("url")
			self.minorheading['date'] = self.debatedate
			self.minorheading['text'] = ""
			self.section_name = "MINOR-HEADING"

		elif name.lower() == "speech":
			self.speech['filename'] = self.db_filename
			self.speech['type'] = "SPEECH"
			self.speech['id'] = attrs.get('id')

			if 'hansard_id' in attrs:
				self.speech['hansard_id'] = attrs.get('hansard_id')
			else:
				self.speech['hansard_id'] = 'none'


			self.speech['person_id'] = attrs.get('person_id')
			self.speech['speakerid'] = attrs.get('speakerid')
			self.speech['nospeaker'] = attrs.get("nospeaker")
			self.speech['speakername'] = attrs.get("speakername")
			self.speech['time'] = attrs.get("time")
			self.speech['colnum'] = attrs.get("colnum")
			self.speech['majorheading'] = self.last_major_heading
			self.speech['minorheading'] = self.last_minor_heading
			self.speech['url'] = attrs.get("url")
			self.speech['date'] = self.debatedate
			self.speech['text'] = ""
			self.section_name = "SPEECH"

		elif name.lower() == "self.division":
			self.division['type'] = "DIVISION"
			self.section_name = "DIVISION"
			
	def endElement(self, name):
		if name.lower() == "major-heading":
			self.last_major_heading = self.majorheading['text']
			self.majorheading = dict()
			self.majorheading['text'] = ""
				
		elif name.lower() == "minor-heading":
			self.last_minor_heading = self.minorheading['text']
			self.minorheading=dict()
			self.minorheading['text'] = ""
		
		elif name.lower() == "speech":
			data = (self.speech['hansard_id'], self.speech['id'], self.speech['type'], self.speech['text'],  self.speech['filename'], self.speech['speakerid'], self.speech['speakername'], self.speech['time'], self.speech['date'], self.speech['majorheading'], self.speech['minorheading'], self.speech['url'])

			parseSpeechForAggregation(self.speech['text'], self.speech['speakerid'], self.speech['person_id'], self.speech['speakername'], self.speech['filename'])


			self.speech=dict()		
			self.speech['text'] = ""

		elif name.lower() == "division":
			self.division = dict()


	def characters(self, content):
		text = html_special_chars(content);

		if self.section_name == "MAJOR-HEADING":
			self.majorheading['text'] = self.majorheading['text'] + text;
		elif self.section_name == "MINOR-HEADING":
			self.minorheading['text'] = self.minorheading['text'] + text;
		elif self.section_name == "SPEECH":
			self.speech['text'] = self.speech['text'] + text;
		elif self.section_name == "DIVISION":
			pass
	
	def endDocument(self):
		pass

   

def parseSpeechForAggregation(text, speakerid, personid, speakername, filename):
	year = filename[7:11]

	numericid="unknown"
	personTF=False

	if speakerid is not None:
		numericid = speakerid
		personTF = False
	if personid is not None:
		numericid = personid
		personTF = True
	

	speech = text.lower().translate(string.maketrans(string.punctuation, ' '*len(string.punctuation)))
	unicode_speech = speech.decode('utf-8')
	#unicode_speaker = speakername.decode('utf-8')
	#print str(speakername)# + ' ' + unicode_speech

	# TODO PRINT ALSO year, Party
	speaker = get_speaker_info(numericid, personTF)
	print speaker #speech, year, party



if __name__ =='__main__':
	main(sys.argv[1])

