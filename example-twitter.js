var Twitter = require('node-tweet-stream')
  , t = new Twitter({
    consumer_key: 'kaUQzVdfjgdyy2FnywobjvQnS',
    consumer_secret: 'IH2KqmlIrhqVTptXgCmhBIVFdEu2sbRTvuYIN9MK2x1fiuqYAD',
    token: '2338788337-tg2kKAvBGrcc9db6IaKyVE10P1Un49b7I5PTUpf',
    token_secret: 'Z7vRhlbmPAqjB1cS40CsltapeaeEdJzAoMsq7X0zoRZAN'
  })

var tweetStack = new Array();

t.on('tweet', function (tweet) {
  console.log('tweet received', tweet);
  tweetStack.push(tweet);
})

t.on('error', function (err) {
  console.log('Oh no')
})

t.track('monstersuniversity')

var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  if (tweetStack.length != 0) {
  	res.end(JSON.stringify(tweetStack.pop()));
  } else {
  	res.end('Hello world');
  }
}).listen(80, '127.0.0.1');