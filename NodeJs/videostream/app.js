var express = require('express');
var app = new express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var fs = require("fs");
var path = require("path");

app.get('/movie.mp4', function(req, res) {
  var file = path.resolve(__dirname, "movie_10mb.mp4");
  var range = req.headers.range;
  var positions = range ? range.replace(/bytes=/, "").split("-") : [0];
  var start = parseInt(positions[0], 10);

  fs.stat(file, function(err, stats) {
    var total = stats.size;
    var end = positions[1] ? parseInt(positions[1], 10) : total - 1;
    var chunksize = (end - start) + 1;

    res.writeHead(206, {
      "Content-Range": "bytes " + start + "-" + end + "/" + total,
      "Accept-Ranges": "bytes",
      "Content-Length": chunksize,
      "Content-Type": "video/mp4"
    });

    var stream = fs.createReadStream(file, {
        start: start,
        end: end
      })
      .on("open", function() {
        stream.pipe(res);
      }).on("error", function(err) {
        res.end(err);
      });
  });
});

app.get('/small.ogv', function(req, res) {
  var file = path.resolve(__dirname, "small.ogv");
  var range = req.headers.range;
  var positions = range ? range.replace(/bytes=/, "").split("-") : [0];
  var start = parseInt(positions[0], 10);

  fs.stat(file, function(err, stats) {
    var total = stats.size;
    var end = positions[1] ? parseInt(positions[1], 10) : total - 1;
    var chunksize = (end - start) + 1;

    res.writeHead(206, {
      "Content-Range": "bytes " + start + "-" + end + "/" + total,
      "Accept-Ranges": "bytes",
      "Content-Length": chunksize,
      "Content-Type": "video/ogg"
    });

    var stream = fs.createReadStream(file, {
        start: start,
        end: end
      })
      .on("open", function() {
        stream.pipe(res);
      }).on("error", function(err) {
        res.end(err);
      });
  });
});

app.get('/small.webm', function(req, res) {
  var file = path.resolve(__dirname, "small.webm");
  var range = req.headers.range;
  var positions = range ? range.replace(/bytes=/, "").split("-") : [0];
  var start = parseInt(positions[0], 10);

  fs.stat(file, function(err, stats) {
    var total = stats.size;
    var end = positions[1] ? parseInt(positions[1], 10) : total - 1;
    var chunksize = (end - start) + 1;

    res.writeHead(206, {
      "Content-Range": "bytes " + start + "-" + end + "/" + total,
      "Accept-Ranges": "bytes",
      "Content-Length": chunksize,
      "Content-Type": "video/webm"
    });

    var stream = fs.createReadStream(file, {
        start: start,
        end: end
      })
      .on("open", function() {
        stream.pipe(res);
      }).on("error", function(err) {
        res.end(err);
      });
  });
});

app.get('/file', function(req, res) {
  res.setHeader('Content-disposition', 'attachment; filename=movie.mp4');
  res.download('movie.mp4');
/*  var options = {
    root: __dirname,
    dotfiles: 'deny',
    headers: {
      'x-timestamp': Date.now(),
      'x-sent': true
    }
  };

  res.sendFile('/movie.mp4', options, function(err) {
    if (err) {
      console.log(err);
      res.status(err.status).end();
    } else {
      console.log('Sent:', fileName);
    }
  });*/
});


app.get('/ping', function(req, res) {
  res.send('pigou!');
});

app.listen(3000, function() {
  console.log('listen');
});