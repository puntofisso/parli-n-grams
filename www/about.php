<?php
?>
<!DOCTYPE html>
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <title>Parli-N-Grams</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="boot/bootstrap.css" media="screen">
    <link rel="stylesheet" href="boot/bootswatch.min.css">
    <link rel="stylesheet" href="parligram.css">
 <link rel="stylesheet" type="text/css" href="nv.d3.css">
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
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-5727641-4', 'auto');
  ga('send', 'pageview');
</script>

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

        <div class="row">
          <div class="col-lg-12">
            <h1 class="tohide">Parli-N-Grams</h1>
		<h3>What is it?</h3>
		<p>Parli-N-Grams is an N-Gram viewer. The N-Grams it displays are extracted from Hansard, the archive of parliamentary debates, and most specifically from the House of Commons debates.
		<h3>How does it work?</h3>
		<p>Parli-N-Grams is based on a collection of scripts.</p>
		<p>There is a <b>harvesting</b> component that collects the debates files, a <b>parsing</b> component that extracts the actual N-Grams and builds a database model, and a <b>data visualization</b> component that creates the charts.</p>
		<p>If you want to try, just type some words in the field and click on search. You can add multiple ngrams using the &quot;+&quot; button.</p>
		<p>The ngrams are extracted from the original text using <b>word2phrase</b> and <b>word2vec</b>. The viewer supports 1- through 8-grams.</p>
		<h3>Where do the data come from?</h3>
		All data comes from the XML archive at <a href="http://parser.theyworkforyou.com/hansard.html">TheyWorkForYou</a>, made by the awesome people at <a href="http://www.mysociety.org">mySociety</a>.</p>
		<h3>How often is it upgraded</h3>
		<p>The data is refreshed often, generally at least once a week after Prime Minister's Questions (on Wednesday).</p>
		</ul>
		</p>
	   </div>
      </div>


      <footer>
        <div class="row">
          <div class="col-lg-12">

            <ul class="list-unstyled">
              <li><a href="http://puntofisso.net/techblog/2014/11/11/on-parliamentary-language-analysis/">About</a></li>
            </ul>
            <p>Made by <a href="http://puntofisso.net/" rel="nofollow">Giuseppe Sollazzo</a>.</p>
            <p>UI based on <a href="http://bootswatch.com">Bootswatch<a>, <a href="http://getbootstrap.com/" rel="nofollow">Bootstrap</a>. Icons from <a href="http://fortawesome.github.io/Font-Awesome/" rel="nofollow">Font Awesome</a>. Web fonts from <a href="http://www.google.com/webfonts" rel="nofollow">Google</a>.</p>

          </div>
        </div>

      </footer>


    </div>


    <script src="boot/jquery-1.10.2.min.js"></script>
    <script src="boot/dist/js/bootstrap.min.js"></script>
    <script src="boot/bootswatch.js"></script>
  

</body></html>
<?php
?>
