% include('partials/header.tpl')
<div class="container">
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

   <h3>Results</h3>
  <div class="alert alert-success" role="alert">Your secret data storage is generated</div>
  <div class="row">
    <div class="col-xs-3">
      <img src="data:image/png;base64,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">
    </div>
    <div class="col-xs-9">
      <form>
        <div class="form-group">
          <label>Full link</label>
          <div class="input-group">
            <input type="text" class="form-control" placeholder="http://dfhjsagfhjsagdhjasgdasjhdghjasd">
            <span class="input-group-btn">
        <button class="btn btn-default" type="button">Copy</button>
      </span>
          </div>
        </div>
        <div class="form-group">
          <label>Shortened link</label>
          <div class="input-group">
            <input type="text" class="form-control" placeholder="http://dfhjsagfhjsagdhjasgdasjhdghjasd">
            <span class="input-group-btn">
        <button class="btn btn-default" type="button">Copy</button>
      </span>
          </div>
          <!-- /input-group -->
        </div>
      </form>
      <br><br>
      <button type="button" class="btn btn-default">Close and create new secret</button>

    </div>

  </div>
</div> 
% include('partials/footer.tpl')