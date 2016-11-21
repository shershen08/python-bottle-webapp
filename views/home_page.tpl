% include('partials/header.tpl')
<div class="container">
     <h3>Welcome</h3>
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
% include('partials/footer.tpl')