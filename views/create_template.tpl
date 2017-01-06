<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>Create</title>
  
<link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css'>
<link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap-theme.min.css'>
<link rel='stylesheet' href='assets/styles.css'>
  
  
</head>

<body class="page-create">


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


  <h3>Create</h3>

  <form>
    <div class="form-group">
      <label>Paste secret data (total:)</label>
      <textarea class="form-control"></textarea>
    </div>

    <div class="form-group">
      <div class="btn-group" role="group btn-group-sm" aria-label="...">
        <button type="button" v-on:click="toggleTab('showDateSelection')" class="btn btn-default">Select lifetime date</button>
        <button type="button" v-on:click="toggleTab('showNotify')" class="btn btn-default">Notify external url</button>
        <button type="button" v-on:click="toggleTab('showEmail')" class="btn btn-default">Email the link</button>
        <button type="button" v-bind:class="{ active: showExtraOptions }" v-on:click="toggleTab('showExtraOptions')" class="btn btn-default">Extra options</button>
      </div>
      <div class="form-group">
        <section v-show="showDateSelection">
          <label>Select date until which the secret will be valid</label>
          <input type="text" class="form-control">
        </section>
        <section v-show="showNotify">
          <label>Paste the url to send the reqest (GET) when the secret is opened</label>
          <input type="email" class="form-control">
        </section>
        <section v-show="showEmail">
          <label>Paste in the email to nofity</label>
          <input type="email" class="form-control">
        </section>
        <section v-show="showExtraOptions">
          <div class="checkbox">
            <label>
      <input type="checkbox"> Generate QR-code
    </label>
          </div>
          <div class="checkbox">
            <label>
      <input type="checkbox">Use url shortener
    </label>
          </div>
        </section>


      </div>

      <button type="button" class="btn btn-primary">Generate secret</button>
  </form>

  </div>

<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>
<script src='http://getbootstrap.com/dist/js/bootstrap.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/vue/2.0.0/vue.min.js'></script>
<script src="assets/app.js"></script>

</body>
</html>
