<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>{{i18['app_name']}}</title>
  <link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css'>
  <link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap-theme.min.css'>
  <link rel="stylesheet" href="assets/styles.css">
</head>

<body>

   <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li><a href="/create">{{i18['header_menu']['create']}}</a></li>
            <li><a href="/secret">{{i18['header_menu']['view']}}</a></li>
            <li><a href="/static/about">{{i18['header_menu']['about']}}</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>