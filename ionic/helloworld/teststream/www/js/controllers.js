// capture callback
var captureSuccess = function(mediaFiles) {
    console.log(mediaFiles);
};

// capture error callback
var captureError = function(error) {
  console.log('Error code: ' + error.code, null, 'Capture Error');
};


angular.module('starter.controllers', [])

.controller('LivestreamCtrl', function($scope){
  var btn = document.getElementById('btnCaptureAudio');
  btn.onclick = function(){
    var options = { limit: 1, duration: 10 };
    navigator.device.capture.captureAudio(captureSuccess, captureError, options);  
  }
  
  var btnImg = document.getElementById('btnCaptureImage');
  btnImg.onclick = function(){
    navigator.device.capture.captureImage(captureSuccess, captureError, {limit:1});  
  }
})

.controller('DashCtrl', function($scope) {})

.controller('ChatsCtrl', function($scope, Chats) {
  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  };
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});
