<?php

include('lastupdate.php');
$ngrams = "all:my+right+hon+friend";
if (isset($_GET['ngrams'])) {
	$ngrams=$_GET['ngrams'];
}

?>

<!DOCTYPE html>
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta charset="utf-8">
<title>Parli-N-Grams</title>
<meta name="viewport" content="width=device-width, initial-scale=1">

 <meta property="og:url" content="http://parli-n-grams.puntofisso.net/index.php"/>
      <meta property="og:title" content="Parli-N-Grams"/>
      <meta name="keywords", content="parliament,parli,data,opendata,politics,labour,conservative,conservatives,tories,tory,labour party,libdem,lib dem,libdems,lib dems,brexit,ukip,independence party,uk independence party,snp,scottish national party,nationalism,eu,european,european union,eurovision,eu referendum,referendum,russia,trump,obama,socialism"/>
      <meta property="og:image" content="http://parli-n-grams.puntofisso.net/parli.PNG"/>
      <meta property="og:site_name" content="Parli-N-Grams" />
      <meta property="og:description" content="Parli-N-Grams"/>
<link rel="stylesheet" href="boot/bootstrap.css" media="screen">
<link rel="stylesheet" href="boot/bootswatch.min.css">
<link rel="stylesheet" href="parligram.css">
<link rel="stylesheet" type="text/css" href="nv.d3.css">
<link href="share-button.min.css" rel="stylesheet">
<script src='share-button.min.js'></script>
<script src="d3.min.js" charset="utf-8"></script>
<script src="nv.d3.min.js" charset="utf-8"></script>
<script src="jquery-2.1.1.min.js" charset="utf-8"></script>
<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
<!--[if lt IE 9]>
<script src="../bower_components/html5shiv/dist/html5shiv.js"></script>
<script src="../bower_components/respond/dest/respond.min.js"></script>
<![endif]-->
</head>
<body>
<div class="navbar navbar-default navbar-fixed-top">
	<div class="container">
		<div class="navbar-header">
			<a href="http://parli-n-grams.puntofisso.net" class="navbar-brand">Parli-N-Grams</a>
			<button class="navbar-toggle" type="button" data-toggle="collapse" data-target="#navbar-main">
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
		</div>
		<div class="navbar-collapse collapse" id="navbar-main">
			<ul class="nav navbar-nav">
				<li>
					<a href="about.php">About</a>
				</li>
			</ul>
			<ul class="nav navbar-nav navbar-right">
			</ul>
		</div>
	</div>
</div>


<div class="container fill">
	<div class="page-header" id="banner" style="height: !important 100px;">
		<div class="row">
			<div class="col-lg-9">
				<h1 class="tohide2">Parli-N-Grams</h1>
				<p class="lead tohide2">Chart the frequency of words and phrases in UK Parliament debates</p>
	

				<div id="control">
					<form method="post">
						<p>
							<a href="#" class="btn btn-default" id="addVar">+</a>
							<input id="searchsubmit" class="btn btn-default" type="submit" value="Search"/>
							<a href="#" class="btn btn-default" id="reset">Reset</a>
						</p>
					</form>
				</div>
				<div id="spinner"></div>
				<div id="chart" >
					<!--share-button></share-button-->
					<svg id="chartsvg"></svg>
				</div>
			</div>

			<div class="col-lg-3"style="padding-top:300px" >
					<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
					<ins class="adsbygoogle" style="display:inline-block;width:300px;height:250px" data-ad-client="ca-pub-4410734268512605" data-ad-slot="4652812342">
					</ins>
					<script>
						(adsbygoogle = window.adsbygoogle || []).push({});
					</script>
			</div>

		</div>
	</div>
</div>



<footer>
	<div class="row">
		<div class="col-lg-12">

			<ul class="list-unstyled">
			</ul>
			<p>Last update: <?php dolast() ?>.</p>
			<p>Made by <a href="http://puntofisso.net/" rel="nofollow">Giuseppe Sollazzo</a>.</p>
			<p>UI based on <a href="http://bootswatch.com">Bootswatch<a>, <a href="http://getbootstrap.com/" rel="nofollow">Bootstrap</a>. Icons from <a href="http://fortawesome.github.io/Font-Awesome/" rel="nofollow">Font Awesome</a>. Web fonts from <a href="http://www.google.com/webfonts" rel="nofollow">Google</a>.</p>

		</div>
	</div>

</footer>


</div>


<script src="boot/dist/js/bootstrap.min.js"></script>
<script src="boot/bootswatch.js"></script>


<script src="spin.min.js"></script>

	<script>
		(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
			(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
			m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

		ga('create', 'UA-5727641-4', 'auto');
		ga('send', 'pageview');
	</script>

	<script>


	var mpdict = {};

	mpdict["commons"] = "House of Commons";
	mpdict["lords"] = "House of Lords";
		var receivedString = "<?php print $ngrams?>";
		receivedString = receivedString.replace(/\+/g, ' ').replace(/%3A/g, ':').replace(/%7C/g, '|');
		var receivedStringArray = receivedString.split(";");

		var startingNo = receivedStringArray.length;
		var $node = "";

		for (varCount=0;varCount<startingNo;varCount++){

			var this_entry_arr = receivedStringArray[varCount].split(":");
			var this_ngrams = this_entry_arr[1];
			var this_mp = this_entry_arr[0];
			var displayCount = varCount+1;

			$node += '<p class="tohide"><label for="var'+displayCount+'">N-Gram '+displayCount+': </label><input type="text" value="'+ this_ngrams +'" class="ngraminput parli-form-control" name="var'+displayCount+'" id="var'+displayCount+'"></input> at the ';

			$node += '<select id="select'+displayCount+'" class="ngramselect parli-form-control">';
	
			$.each(mpdict, function(key, value) {

				if (this_mp == key)	{		
					option = '<option value="'+key+'" selected>'+value+'</option>';
				} else {
					option = '<option value="'+key+'">'+value+'</option>';
				} 
				$node += option;

			});

			
	
			$node += '</select>&nbsp;<a href="#" class="btn btn-default" id="removeVar">X</a></p>';
		}


		$('form').prepend($node);

		$('form').on('click', '#removeVar', function(event){
			event.preventDefault();
			$(this).parent().remove();

		});

		$('#addVar').on('click', function(event){
			event.preventDefault();
			varCount++;

			 $node = '<p class="tohide"><label for="var'+varCount+'">N-Gram '+varCount+': </label><input type="text"class="ngraminput parli-form-control" name="var'+varCount+'" id="var'+varCount+'"></input> at the ';

                      $node += '<select id="select'+varCount+'" class="ngramselect parli-form-control">';
			$.each(mpdict, function(key, value) {
					if (key == "commons") {
	                                        option = '<option value="'+key+'" selected>'+value+'</option>';
					} else {
	                                        option = '<option value="'+key+'">'+value+'</option>';
					}
                                $node += option;

			});
			 $node += '</select>&nbsp;<a href="#" class="btn btn-default" id="removeVar">X</a></p>';

			$(this).parent().before($node);
		});

// intercept click on submit
$('#searchsubmit').on('click',function(event){
	event.preventDefault();

	if ($('.ngraminput').length > 0) {	
	var stringarray = [];
	
	var countoutput = 0;
	var ngraminputarray = $('.ngraminput').each(function() {
		var this_ngram = $(this).val();
		var this_mp = $('.ngramselect')[countoutput].value;
        	stringarray.push(this_mp+":"+this_ngram);
		countoutput++;
    });


	var urlstringarray = 'http://parli-n-grams.puntofisso.net/index.php?ngrams='+encodeURIComponent(stringarray.join(";")).replace(/%20/g, '+').replace(/%2C/g, ',');
	//var urlstringarray = 'http://parli-n-grams.puntofisso.net/indexmp.php';
	window.urltoshare = urlstringarray;
	if (typeof (history.pushState) != "undefined") {
        var obj = { Title: 'Parli-N-Grams', Url: urlstringarray };
        history.pushState(obj, obj.Title, obj.Url);
    } else {
        alert("Browser does not support HTML5.");
    }

	var target = document.getElementById('spinner');
	var spinner = new Spinner().spin()
	target.appendChild(spinner.el);
	generateChart(false);
}
});

$('#reset').on('click', function(event) {
	varCount=0;
	$('.tohide2').empty();
	$('.tohide2').empty();
	$('.tohide').empty();
	$('.tohide').remove();
});

</script>

<script>
	function generateChart(onboot) {
		var ngramsArray = new Array();
		var ngramsSelectArray = new Array();
		$('.ngraminput').each(function(i,obj) {
			var value = "#"+obj['id'];
			var y = $(value).val();
			ngramsArray.push(y);
		});
		$('.ngramselect').each(function(i,obj) {
           	     var value = "#"+obj['id'];
	                var y = $(value).val();
	                ngramsSelectArray.push(y);
	        });
		if (ngramsArray.length==0)
			return;
		


		$("#chartsvg").empty();
		var searchNgram = "";
		/*These lines are all chart setup.  Pick and choose which chart features you want to utilize. */
		nv.addGraph(function() {
			var chart = nv.models.lineChart()
		.margin({left: 100})  //Adjust chart margins to give the x-axis some breathing room.
		.useInteractiveGuideline(true)  //We want nice looking tooltips and a guideline!
		.transitionDuration(350)  //how fast do you want the lines to transition?
		.showLegend(true)       //Show the legend, allowing users to turn on/off line series.
		.showYAxis(true)        //Show the y-axis
		.showXAxis(true)        //Show the x-axis
		.width(800).height(400)
		;


		chart.xAxis
		.axisLabel('Year');

		chart.yAxis
		.axisLabel('Mentions %').tickFormat(d3.format('.07f'));;



		var myData = extractData();
		d3.select('#chart svg')
		.datum(myData)
		.call(chart);


		d3.selectAll("g.nv-line")
		.on("click.mine", function(dataset){


			var singlePoint, pointIndex, pointXLocation, allData = [];
			var lines = chart.lines;

			var xScale = chart.xAxis.scale();
			var yScale = chart.yAxis.scale();
			var mouseCoords = d3.mouse(this);
			var pointXValue = xScale.invert(mouseCoords[0]);

			dataset
			.filter(function(series, i) {
				series.seriesIndex = i;
				return !series.disabled;
			})
			.forEach(function(series,i) {
				pointIndex = nv.interactiveBisect(series.values, pointXValue, lines.x());
				lines.highlightPoint(i, pointIndex, true);

				var point = series.values[pointIndex];

				if (typeof point === 'undefined') return;
				if (typeof singlePoint === 'undefined') singlePoint = point;
				if (typeof pointXLocation === 'undefined')
					pointXLocation = xScale(lines.x()(point,pointIndex));

				allData.push({
					key: series.key,
					strokeWidth: 100.0,
					value: lines.y()(point, pointIndex),
					color: lines.color()(series,series.seriesIndex)
				});
			});
/*
Returns the index in the array "values" that is searchNgram to searchVal.
Only returns an index if searchVal is within some "threshold".
Otherwise, returns null.
*/
nv.nearestValueIndex = function (values, searchVal, threshold) {
	"use strict";
	var yDistMax = Infinity, indexToHighlight = null;
	values.forEach(function(d,i) {
		var delta = Math.abs(searchVal - d);
		if ( delta <= yDistMax && delta < threshold) {
			yDistMax = delta;
			indexToHighlight = i;
		}
	});
	return indexToHighlight;
};

//Determine which line the mouse is closest to.
var yValue = yScale.invert( mouseCoords[1] );
var domainExtent = Math.abs(yScale.domain()[0] - yScale.domain()[1]);
var threshold = 0.03 * domainExtent;
var indexToHighlight = nv.nearestValue/Index(
	allData.map(function(d){ return d.value}), yValue, threshold
	);
if (indexToHighlight !== null) {
	allData[indexToHighlight].highlight = true;
	searchNgram = allData[indexToHighlight];
}
var term = searchNgram['key'];
var year = Math.round(pointXValue);



});

nv.utils.windowResize(function() { chart.update() });
if (!onboot) {
	$('.tohide2').empty();
	$('.tohide2').remove();
}
d3.select('#chart svg')
.datum(myData)
.call(chart)
.style({ 'width': '800px', 'height':'400px' });

$('#spinner').empty();
return chart;

});
}// Data extraction





function extractData() {
	var returnArray = new Array();
	var ngramsArray = new Array();
	var ngramsSelectArray = new Array();
	$('.ngraminput').each(function(i,obj) {
		var value = "#"+obj['id'];
		var y = $(value).val();
		ngramsArray.push(y);
	});
	$('.ngramselect').each(function(i,obj) {
                var value = "#"+obj['id'];
                var y = $(value).val();
                ngramsSelectArray.push(y);
        });
	var ngrams = ngramsArray;
	
	// TODO build array of MP name
		
	if (ngrams.length==0) {
		alert("You need to enter at least one search term");
		return;
	}
	var colourArray = ['#ff0000','#00ff00','#0000ff','#ff00ff','#00ffff','#ffff00'];
	var colourIndex = 0;


	//var ngrstr = ngrams.join(",");


	var countselect = 0;
	ngrams.forEach(function(entry) {
		if ((entry=='') || (typeof entry == 'undefined')) return;
		var countArray = [];
		var fileListArray = [];
		entry = entry.replace(/ /g,"_");
		var mpentry = ngramsSelectArray[countselect];
	$.ajax({
		url: 'logmp.php',
		data: 'ngrams='+entry+'&mp='+mpentry,
	});
		$.ajax({

			url: 'mysqlmplords.php',
			data: "ngram="+entry+"&mp="+mpentry,
			dataType: 'json',
			async: false,
			success: function(data)
			{
				for (var i=1935; i<=2018; i++) {
					var thisobj = data[i];
					if ((thisobj == '') || (typeof thisobj == 'undefined')) {
						countArray.push({x: i, y:0});
						fileListArray[i] = null;
					} else {
						var count = thisobj['count'];
						var yearcount = thisobj['yearcount'];
						var mpstring = thisobj['mpstring'];
						var percent = count * 100 / yearcount;
//countArray.push({x: i, y:parseInt(thisobj['count'])});
countArray.push({x: i, y:percent});

}
}
},
error: function(x, t, m) {
	if(t==="timeout") {
		alert("got timeout");
	} else {
		alert(t);
	}
}
});

		countselect++;
		var mpname = mpdict[mpentry];
		returnArray.push({values: countArray, key: entry + " (" + mpname + ")", color: colourArray[colourIndex]});
		colourIndex++;

	});



return returnArray;

}

//if (onboot)
generateChart(true);

</script>

</body>
</html>
<?php
?>
