var webdriver = require('wd')
  , assert = require('assert');

var browser = webdriver.remote(
  "ondemand.saucelabs.com"
  , 80
  , "issuu"
  , "23a5b32a-6ab8-4866-8f1d-9a13c98348c2"
);

browser.on('status', function(info){
  console.log('\x1b[36m%s\x1b[0m', info);
});

browser.on('command', function(meth, path){
  console.log(' > \x1b[33m%s\x1b[0m: %s', meth, path);
});

var desired = {
  browserName: 'firefox'
  , version: '16'
  , platform: 'Windows 2003'
  , tags: ["examples"]
  , name: "This is an example test"
}

browser.init(desired, function() {
  browser.get("http://saucelabs.com/test/guinea-pig", function() {
    browser.title(function(err, title) {
      assert.ok(~title.indexOf('I am a page title - Sauce Labs'), 'Wrong title!');
      browser.elementById('submit', function(err, el) {
        browser.clickElement(el, function() {
          browser.eval("window.location.href", function(err, title) {
            assert.ok(~title.indexOf('#'), 'Wrong title!');
            browser.quit()
          })
        })
      })
    })
  })
})