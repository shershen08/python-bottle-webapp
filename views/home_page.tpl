<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>Home</title>
  
<link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css'>
<link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap-theme.min.css'>
<link rel='stylesheet' href='assets/styles.css'>
  
  
</head>

<body class="page-home">



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

  <div class="container" id="app">
  <h3>Home</h3>
  <div class="row">
    <div class="col-xs-6">
      Open existing secret<br><br>
      <input type="text" class="form-control" placeholder="Paste id (16 symbols) here">
      <br>
      <button type="button" class="btn btn-default">Open secret</button>
    </div>
    <div class="col-xs-6">
      Or create your own<br>
      <button type="button" class="btn btn-primary btn-lg">Create secret</button>
    </div>
  </div>
  

  </div>

<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>
<script src='http://getbootstrap.com/dist/js/bootstrap.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/vue/2.0.0/vue.min.js'></script>
<script src="assets/app.js"></script>

</body>
</html>
