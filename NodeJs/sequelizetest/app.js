var express = require('express');
var Sequelize = require('sequelize');
var app = express();
var sequelize = new Sequelize('POCSBase', 'sa', '159753', {
  host: 'localhost',
  dialect: 'mssql',
  define: {
    timestamps: false // true by default
  }
});


var User = sequelize.define('POC_USER', {
  Name: Sequelize.STRING,
  Birthday: Sequelize.DATE,
  Surname: Sequelize.STRING,
  Ournumber: Sequelize.INTEGER,
  Ourvalue: Sequelize.FLOAT,
  Email: Sequelize.STRING,
  extra1: Sequelize.TEXT,
  extra2: Sequelize.INTEGER,
  valid: Sequelize.BOOLEAN
}, {tableName: 'POC_USER'});

var UserDetail = sequelize.define('POC_USER_DETAIL', {
  poc_user_id: Sequelize.INTEGER,
  field1: Sequelize.STRING,
  field2: Sequelize.INTEGER,
  field3: Sequelize.FLOAT,
}, {tableName: 'POC_USER_DETAIL'});

User.hasOne(UserDetail, { foreignKey: 'poc_user_id' });

/*
sequelize.transaction().then(function (t) {
  return User.create({
    Name: 'Homer',
    Birthday: new Date(1983, 2, 27)
  }, {transaction: t}).then(function () {
    return User.create({
      Name: 'Lisa',
      //Birthday: 'BAD DATA'
      Birthday: new Date(1983, 2, 27)
    }, {transaction: t});
  }).then(function () {
    t.commit().then(function(){console.log('commit!!');});
  }).catch(function (err) {
    t.rollback().then(function(){console.log('rollback!!');});
  });
});

sequelize.transaction(function (t) {
  // chain all your queries here. make sure you return them.
  return User.create({
    Name: 'Abraham',
    Birthday: new Date(2000, 11, 31)
  }, {transaction: t}).then(function() {
    return User.create({
      Name: 'John',
      //Birthday: 'BAD DATA'
      Birthday: new Date(2001, 0, 1)
    }, {transaction: t});
  });
}).then(function (result) {
  // Transaction has been committed
  // result is whatever the result of the promise chain returned to the transaction callback
  console.log(result);
}).catch(function (err) {
  // Transaction has been rolled back
  // err is whatever rejected the promise chain returned to the transaction callback
  console.log(err);
});
*/

/**
 * @api {get} / Request Parish
 *
 * @apiSuccess {Object} array.
 */
app.get('/', function(req, res) {
  console.log(new Date().toISOString());
	User.findAll({ order: 'id' }).then(function (user) {
      console.log(new Date().toISOString());
      res.send(user);
  });
});

app.get('/limit', function(req, res) {
  User.findAll({ order: '', limit: 1000, include: [ UserDetail ] }).then(function (user) {
      console.log('fim!');
      res.send(user);
  });
});

app.listen(3000, function(){
	console.log('started');
});