// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('starter', ['ionic'])
  .run(function ($ionicPlatform) {
    $ionicPlatform.ready(function () {
      // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
      // for form inputs)
      if (window.cordova && window.cordova.plugins.Keyboard) {
        cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      }
      if (window.StatusBar) {
        StatusBar.styleDefault();
      }

      var push = PushNotification.init({
        "android": { "senderID": "1048618102111", "icon": "phonegap", "iconColor": "blue" },
        "ios": { "alert": "true", "badge": "true", "sound": "true" },
        "windows": {}
      });

      push.on('registration', function (data) {
        // data.registrationId
        console.log("registration event");
        document.getElementById("cardtext").innerHTML = data.registrationId;
        console.log(JSON.stringify(data));
      });

      push.on('notification', function (data) {
        // data.message,
        // data.title,
        // data.count,
        // data.sound,
        // data.image,
        // data.additionalData
        console.log("notification event");
        console.log(JSON.stringify(data));
        var cards = document.getElementById("cards");
        var push = '<div class="row">' +
          '<div class="col s12 m6">' +
          '  <div class="card darken-1">' +
          '    <div class="card-content black-text">' +
          '      <span class="card-title black-text">' + data.title + '</span>' +
          '      <p>' + data.message + '</p>' +
          '    </div>' +
          '  </div>' +
          ' </div>' +
          '</div>';
        cards.innerHTML += push;
      });

      push.on('error', function (e) {
        // e.message
        console.log("push error " + e.message);
      });


    });
  });

