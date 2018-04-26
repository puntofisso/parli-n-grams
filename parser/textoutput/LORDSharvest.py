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

_connection = None
db = None
start_time = None
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0


def main(argument):
	global db
	global start_time 
	start_time = time.time()
	#db = get_connection()

	if argument is not None:
		#filename = argument
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

def housekeeping(year):
	print 'Removing ngrams with low count'
	global db
	#db = get_connection()
        cursor = db.cursor()
	
	sql = 'DELETE FROM 1grams WHERE year = %s AND count < 10'
        data = (year)
        cursor.execute(sql, data)
	sql = 'DELETE FROM 2grams WHERE year = %s AND count < 10'
        data = (year)
        cursor.execute(sql, data)
	sql = 'DELETE FROM 3grams WHERE year = %s AND count < 10'
        data = (year)
        cursor.execute(sql, data)
	sql = 'DELETE FROM 4grams WHERE year = %s AND count < 10'
        data = (year)
        cursor.execute(sql, data)
	sql = 'DELETE FROM 5grams WHERE year = %s AND count < 10'
        data = (year)
        cursor.execute(sql, data)
	sql = 'DELETE FROM mp_1grams WHERE year = %s AND count < 10'
        data = (year)
        cursor.execute(sql, data)
	sql = 'DELETE FROM mp_2grams WHERE year = %s AND count < 10'
        data = (year)
        cursor.execute(sql, data)
	sql = 'DELETE FROM mp_3grams WHERE year = %s AND count < 10'
        data = (year)
        cursor.execute(sql, data)
	sql = 'DELETE FROM mp_4grams WHERE year = %s AND count < 10'
        data = (year)
        cursor.execute(sql, data)
	sql = 'DELETE FROM mp_5grams WHERE year = %s AND count < 10'
        data = (year)
        cursor.execute(sql, data)
	


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

			#parseSpeech(self.speech['text'], self.speech['speakerid'], self.speech['person_id'], self.speech['speakername'], self.speech['filename'])
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
		#update_year_count(self.year)
		pass

   
def parseSpeech(text, speakerid, personid, speakername, filename):
	year = filename[7:11]

	if speakername is None:
		speakername = ''
	if speakerid is None:
		speakerid = ''
		if personid is None:
			personid = ''
		else:
			speakerid = personid
	if text is None:
		text = ''

	if speakerid == '':
		speakerid = 'unknown'
	if speakername == '':
		speakername = 'unknown'

	speech = text.lower().translate(string.maketrans(string.punctuation, ' '*len(string.punctuation)))
	unicode_speech = speech.decode('utf-8')

	unitokens = nltk.word_tokenize(unicode_speech)
	bitokens =  nltk.bigrams(unitokens)
	tritokens = nltk.trigrams(unitokens)

	unigrams = nltk.FreqDist(unitokens)
	for unigram, ngramcount in unigrams.items():
		ngram_update(unigram, ngramcount, year, speakerid, 1)

	bigrams = nltk.FreqDist(bitokens)
	for bigram, ngramcount in bigrams.items():
		ngramstring = ' '.join(str(k) for k in bigram)
		ngram_update(ngramstring, ngramcount, year, speakerid, 2)

	trigrams = nltk.FreqDist(tritokens)
	for trigram, trigramcount in trigrams.items():
		ngramstring = ' '.join(str(k) for k in trigram)
		ngram_update(ngramstring, ngramcount, year, speakerid, 3)

	fourtokens = ngrams(text.split(), 4)
	fourgrams = nltk.FreqDist(fourtokens)
	for fourgram, fourgramcount in fourgrams.items():
		ngramstring = ' '.join(str(k) for k in fourgram)
		ngram_update(ngramstring, ngramcount, year, speakerid, 4)
	
	fivetokens = ngrams(text.split(), 5)
	fivegrams = nltk.FreqDist(fivetokens)
	for fivegram, fivegramcount in fivegrams.items():
		ngramstring = ' '.join(str(k) for k in fivegram)
		ngram_update(ngramstring, ngramcount, year, speakerid, 5)

def parseSpeechForAggregation(text, speakerid, personid, speakername, filename):
	year = filename[7:11]

	if speakername is None:
		speakername = ''
	if speakerid is None:
		speakerid = ''
		if personid is None:
			personid = ''
		else:
			speakerid = personid
	if text is None:
		text = ''

	if speakerid == '':
		speakerid = 'unknown'
	if speakername == '':
		speakername = 'unknown'

	speech = text.lower().translate(string.maketrans(string.punctuation, ' '*len(string.punctuation)))
	unicode_speech = speech.decode('utf-8')
	print unicode_speech

def ngram_update(ngram, ngramcount, year, speakerid, ngramtype):
	global db
	global start_time
	global g5

	stat_g5 = 0

	#db = get_connection()
        cursor = db.cursor()
	elapsed_time = time.time() - start_time
	if ngramtype == 1:
		sql = ("INSERT INTO 1grams (ngram, year, count) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE count = count + %s;")
		sql_mp = ("INSERT INTO mp_1grams (ngram, year, count, speakerid) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE count = count + %s;")
	elif ngramtype == 2:
		sql = ("INSERT INTO 2grams (ngram, year, count) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE count = count + %s;")
		sql_mp = ("INSERT INTO mp_2grams (ngram, year, count, speakerid) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE count = count + %s;")
	elif ngramtype == 3:
		sql = ("INSERT INTO 3grams (ngram, year, count) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE count = count + %s;")
		sql_mp = ("INSERT INTO mp_3grams (ngram, year, count, speakerid) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE count = count + %s;")
	elif ngramtype == 4:
		sql = ("INSERT INTO 4grams (ngram, year, count) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE count = count + %s;")
		sql_mp = ("INSERT INTO mp_4grams (ngram, year, count, speakerid) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE count = count + %s;")
	elif ngramtype == 5:
		sql = ("INSERT INTO 5grams (ngram, year, count) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE count = count + %s;")
		sql_mp = ("INSERT INTO mp_5grams (ngram, year, count, speakerid) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE count = count + %s;")
	else:
		return
	g5 = g5 + 1
	if g5 % 1000 == 0 :
		stat_g5 = g5 / elapsed_time 
		print "ngram/sec: " + str(stat_g5) 

	data = (ngram, year, ngramcount, ngramcount)
	cursor.execute(sql, data)
	data_mp = (ngram, year, ngramcount, speakerid, ngramcount)
	cursor.execute(sql_mp, data_mp)


def update_year_count(year):
	global db
        #db = get_connection()

        # update 1gram count
        cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("SELECT sum(count) from 1grams WHERE year = %s")	
	data = (year)
        cursor.execute(sql, data)
        yeartot = cursor.fetchone()[0]
        cursor.close()
        cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("INSERT INTO yearcounts (year, ngramtype, total, mpidorall) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE total = %s")
	data = (year, 1, yeartot, 'all', yeartot)
        cursor.execute(sql, data)
        cursor.close()

	# update 2gram count
        cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("SELECT sum(count) from 2grams WHERE year = %s")	
	data = (year)
        cursor.execute(sql, data)
        yeartot = cursor.fetchone()[0]
        cursor.close()
        cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("INSERT INTO yearcounts (year, ngramtype, total, mpidorall) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE total = %s")
	data = (year, 2, yeartot, 'all', yeartot)
        cursor.execute(sql, data)
        cursor.close()

	# update 3gram count
        cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("SELECT sum(count) from 3grams WHERE year = %s")	
	data = (year)
        cursor.execute(sql, data)
        yeartot = cursor.fetchone()[0]
        cursor.close()
        cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("INSERT INTO yearcounts (year, ngramtype, total, mpidorall) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE total = %s")
	data = (year, 3, yeartot, 'all', yeartot)
        cursor.execute(sql, data)
        cursor.close()

	# update 4gram count
        cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("SELECT sum(count) from 4grams WHERE year = %s")	
	data = (year)
        cursor.execute(sql, data)
        yeartot = cursor.fetchone()[0]
        cursor.close()
        cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("INSERT INTO yearcounts (year, ngramtype, total, mpidorall) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE total = %s")
	data = (year, 4, yeartot, 'all', yeartot)
        cursor.execute(sql, data)
        cursor.close()

	# update 5gram count
        cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("SELECT sum(count) from 5grams WHERE year = %s")	
	data = (year)
        cursor.execute(sql, data)
        yeartot = cursor.fetchone()[0]
        cursor.close()
        cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("INSERT INTO yearcounts (year, ngramtype, total, mpidorall) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE total = %s")
	data = (year, 5, yeartot, 'all', yeartot)
        cursor.execute(sql, data)
        cursor.close()

	# update MP 1gram count
	cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("SELECT speakerid, sum(count) from mp_1grams WHERE year = %s group by speakerid")
        mydata = (str(year))
        cursor.execute(sql,mydata)
        yeartots = cursor.fetchall()
        for yeartot_row in yeartots:
                speakerid = yeartot_row[0]
                yeartot = yeartot_row[1]
                cursor2 = db.cursor()
                sql2 = ("INSERT INTO yearcounts (year, ngramtype, total, mpidorall) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE total = %s")
		data = (year, 1, yeartot, speakerid, yeartot)
                cursor2.execute(sql2,data)
                cursor2.close()
        cursor.close()

	# update MP 2gram count
	cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("SELECT speakerid, sum(count) from mp_2grams WHERE year = %s group by speakerid")
        mydata = (str(year))
        cursor.execute(sql,mydata)
        yeartots = cursor.fetchall()
        for yeartot_row in yeartots:
                speakerid = yeartot_row[0]
                yeartot = yeartot_row[1]
                cursor2 = db.cursor()
                sql = ("INSERT INTO yearcounts (year, ngramtype, total, mpidorall) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE total = %s")
                data = (year, 2, yeartot, speakerid, yeartot)
                cursor2.execute(sql2,data)
                cursor2.close()
        cursor.close()

	# update MP 3gram count
	cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("SELECT speakerid, sum(count) from mp_3grams WHERE year = %s group by speakerid")
        mydata = (str(year))
        cursor.execute(sql,mydata)
        yeartots = cursor.fetchall()
        for yeartot_row in yeartots:
                speakerid = yeartot_row[0]
                yeartot = yeartot_row[1]
                cursor2 = db.cursor()
                sql = ("INSERT INTO yearcounts (year, ngramtype, total, mpidorall) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE total = %s")
                data = (year, 3, yeartot, speakerid, yeartot)
                cursor2.execute(sql2,data)
                cursor2.close()
        cursor.close()

	# update MP 4gram count
 	cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("SELECT speakerid, sum(count) from mp_4grams WHERE year = %s group by speakerid")
        mydata = (str(year))
        cursor.execute(sql,mydata)
        yeartots = cursor.fetchall()
        for yeartot_row in yeartots:
                speakerid = yeartot_row[0]
                yeartot = yeartot_row[1]
                cursor2 = db.cursor()
                sql = ("INSERT INTO yearcounts (year, ngramtype, total, mpidorall) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE total = %s")
                data = (year, 4, yeartot, speakerid, yeartot)
                cursor2.execute(sql2,data)
                cursor2.close()
        cursor.close()

	# update MP 5gram count
 	cursor = MySQLdb.cursors.SSCursor(db)
        sql = ("SELECT speakerid, sum(count) from mp_5grams WHERE year = %s group by speakerid")
        mydata = (str(year))
        cursor.execute(sql,mydata)
        yeartots = cursor.fetchall()
        for yeartot_row in yeartots:
                speakerid = yeartot_row[0]
                yeartot = yeartot_row[1]
                cursor2 = db.cursor()
                sql = ("INSERT INTO yearcounts (year, ngramtype, total, mpidorall) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE total = %s")
                data = (year, 5, yeartot, speakerid, yeartot)
                cursor2.execute(sql2,data)
                cursor2.close()
        cursor.close()


if __name__ =='__main__':
	main(sys.argv[1])

