var http = require('http');

var server = http.createServer(function(req,res){
	res.writeHead(200, {'Content-Type':'text/html'});
	res.write('<html><body><h1>Hello Pi from Node </h1></body></html>');
	res.end();
});

server.listen(8080);

console.log('Server is up and running on port 8080');
