var express = require('express');
var app = express();
var mymodule = require('./modulo');

app.get('/news/:ano/:mes/:dia', function (req, res) {
	mymodule.method(mymodule.name + ':' + req.params.dia + '/' + req.params.mes + '/' + req.params.ano);
	res.send("foi!");
});

app.listen(3000);