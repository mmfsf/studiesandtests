var express = require('express');
var multer  = require('multer');

var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/');
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + '_' + file.originalname);
  }
});

var upload = multer({ storage: storage });
var fs = require('fs');

var app = express();

app.use(express.static('views'));

app.get('/', function (req, res) {
  res.redirect('/views/index.html');
});

app.post('/upload', upload.single('fileupload'), function (req, res, next) {
  console.log(req.body); // form fields
  console.log(req.file); // form files
  next();
});

app.post('/upload-list', upload.array('listupload', 4), function (req, res, next) {
  console.log(req.body); // form fields
  console.log(req.files); // form files
  next();
});

app.post('/upload', function(req, res){
  res.send('upload done!');
  res.status(204).end();
});

app.post('/upload-list', function(req, res){
  res.send('upload done!');
  res.status(204).end();
});

app.get('/download', function(req, res){
  var list = fs.readdirSync(__dirname + '/uploads');
  
  var file = __dirname + '/uploads/' + list[0];
  res.download(file);
});

app.listen(3000);