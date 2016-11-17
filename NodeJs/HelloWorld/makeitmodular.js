var mymodule = require('./module1');

var dir = process.argv[2];
var ext = process.argv[3];

mymodule(dir, ext, function (err, list) {
	if (err) { console.log('There was an error:', err); }

	list.forEach(function (file) {
		console.log(file)
	});
});