var express = require('express');
var app = express();

var func1 = function(req, res) {
	res.send('rodou func1');
}

var func2 = function(req, res) {
	res.send('rodou func2');
}

var func3 = function(req, res){
	res.send('roudou func3');
}

var func4 = function(req, res){
	res.send('rodou func4');
}

app.get('/func1', func1);

app.post('/func2', func2);

app.get('/[a-z]*', func3);

app.get('/[0-9]*', func4);

app.listen(3000);