app = angular.module('Bawkr', [])

app.controller('BawkrController', ['$scope', '$http', ($scope, $http) ->
    $scope.username = '';
    $scope.signedin = false;
    $scope.connection = 'connecting';
    $scope.socket = null;
    $scope.bawks = [];

    $scope.message = '';

    $scope.refreshBawks = ->
      $http.get('/bawks').success (e) ->
        $scope.bawks = e.bawks

    $scope.signIn = ->
      $scope.signedin = true;

    $scope.postMessage = ->
      $scope.socket.send('MSG\n'+$scope.username+'\n'+$scope.message)

    $scope.socketConnect = ->
      $scope.socket = new WebSocket('ws://'+window.location.host+'/stream/')

      $scope.socket.onopen = ->
        $scope.connection = 'connected'
        $scope.$apply()

      $scope.socket.onmessage = (e) ->
        if(e.data == 'PING')
          return
        $scope.bawks.unshift(JSON.parse(e.data))
        $scope.$apply()

      $scope.socket.onerror = (error) ->
        $scope.connection = "closed"
        alert("No connection possible :-(")

      $scope.socket.onclose = () ->
        $scope.connection = 'connecting'
        setTimeout $scope.socketConnect, 10

    setTimeout $scope.refreshBawks, 10
    setTimeout $scope.socketConnect, 10

])