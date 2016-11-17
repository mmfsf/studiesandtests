var express = require('express');
var app = express();

var middleware1 = function(req, res, next){
	console.log('mid 1');
	next();
}

var middleware2 = function (req, res, next) {
	console.log('mid 2');
	res.send('retorna do mid');
}

app.use(middleware1);
app.use('/mid2', middleware2);

var func1 = function (req, res) {
	console.log('func');
	res.send('rodou 1');
}

app.get('/func1', func1);

app.listen(3000);