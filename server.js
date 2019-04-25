var express = require('express');
var app = express();
var server = require('http').Server(app);
var io = require('socket.io').listen(server);
var mongo = require('mongodb');


var MongoClient = require('mongodb').MongoClient;
var url = 'mongodb://3.17.6.164:27017/clueless';

MongoClient.connect(url, function(err, db) {
	if(err) throw err;

	console.log('----------------');
	console.log('database connected');
	
	const mDb = db.db("clueless");
	
	console.log('----------------');
	console.log('list collections');

	mDb.listCollections().toArray(function(err, items) {
		console.log(items);
	});

	const mCollection = mDb.collection('test').find();

	mCollection.toArray(function(err, items) {
		console.log('----------------');
		console.log('list collection content')
		console.log(items);
	});


	// add entry to collection
	insertEntry(mDb, 'test', {name: 'John Doe'});

	// remove entry from collection
	deleteEntry(mDb, 'test', {name: 'John Doe'});

	db.close();
});
 
// remove an entry from a collection of a database
// if there are multiple entries, one is removed
function deleteEntry(aDb, aCol, aEntry) {
	aDb.collection(aCol).deleteOne(aEntry, function(err, obj){
		if(err) throw err;
		console.log(`delete: ${JSON.stringify(aEntry)}`);
	})
}

// add an entry to a collection of a database
function insertEntry(aDb, aCol, aEntry) {
	aDb.collection(aCol).insertOne(aEntry, function(err, obj){
		if(err) throw err;
		console.log(`insert: ${JSON.stringify(aEntry)}`);
	})
}



app.use(express.static(__dirname + '/public'));
 
app.get('/', function (req, res) {
 	res.sendFile(__dirname + '/index.html');
});

// connection established, print to console log
io.on('connection', function (socket) {
 	console.log('a user connected');
  
 	// connection closed, print to console log
 	socket.on('disconnect', function () {
   	console.log('user disconnected');
    
	io.emit('disconnect', socket.id);
 	});
});

// listen to port 3000 
server.listen(3000, function () {
	console.log('----------------');
 	console.log(`Listening on ${server.address().port}`);
});
