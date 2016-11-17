var express = require('express')
var app = express()

app.get('/', function (req, res) {
  var resobj = { message: 'Hello, World' }
  var json = JSON.stringify(resobj)
  res.send(json)
})

app.listen(8888, function () {
  console.log('Example app listening on port 8888!')
})