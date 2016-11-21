new Vue({
  el: '#app',
  data: {
    showExtraOptions: false,
    showEmail: false,
    showNotify: false,
    showDateSelection: false
  },
  created: function() {},
  methods: {
    toggleTab: function(tabId) {
    this.showExtraOptions = this.showEmail = this.showNotify = this.showDateSelection = false;
      this[tabId] = true;
    }
  }
})