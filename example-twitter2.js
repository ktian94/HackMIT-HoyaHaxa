var http = require("http");
var util = require('util'),
    twitter = require('twitter');

var twit = new twitter({
    consumer_key: 'kaUQzVdfjgdyy2FnywobjvQnS',
    consumer_secret: 'IH2KqmlIrhqVTptXgCmhBIVFdEu2sbRTvuYIN9MK2x1fiuqYAD',
    access_token_key: ' 2338788337-tg2kKAvBGrcc9db6IaKyVE10P1Un49b7I5PTUpf',
    access_token_secret: 'Z7vRhlbmPAqjB1cS40CsltapeaeEdJzAoMsq7X0zoRZAN'
});

/*
app.get('/', twit.gatekeeper('/login'), routes.index);
app.get('/login', routes.login);
app.get('/twauth', twit.login());
*/

twit.stream('statuses/sample', function(stream) {
    stream.on('data', function(data) {
        console.log(util.inspect(data));
    });
});


http.createServer(function(request, response) {
  console.log("REQUEST RECEIVED!");
response.writeHead(200, {"Content-Type": "text/html"});
  response.write("<!DOCTYPE \"html\">");
  response.write("<html>");
  response.write("<head>");
  response.write("<title>Hello World Page</title>");
  response.write("</head>");
  response.write("<body>");
  response.write("<h1 style='color:blue'>Hello World!</h1>");
  response.write("</body>");
  response.write("</html>");
  response.end();
response.end();

}).listen(80, '127.0.0.1');

var sentimentStr = "";