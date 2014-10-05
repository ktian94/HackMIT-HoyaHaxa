from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import threading
import json
import Queue
import requests

PORT_NUMBER = 8080

consumer_key="kaUQzVdfjgdyy2FnywobjvQnS"
consumer_secret="IH2KqmlIrhqVTptXgCmhBIVFdEu2sbRTvuYIN9MK2x1fiuqYAD"
access_token="2338788337-tg2kKAvBGrcc9db6IaKyVE10P1Un49b7I5PTUpf"
access_token_secret="Z7vRhlbmPAqjB1cS40CsltapeaeEdJzAoMsq7X0zoRZAN"


templateHTML = """
<DOCTYPE html>
<html>
	<head>
	  <link rel="stylesheet" href="http://altstudentsuccess.com/localhost/style.css">
	  <script type="text/javascript">
	  	  //resize screen (input coord, output coord)
	      VideoSource.setInputOutputWindow(0, 0, 1920, 1080, 0, 0, 1600, 900);
	    </script>
	    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	    <link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.1/themes/smoothness/jquery-ui.css" />
      <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.1/jquery-ui.min.js"></script>
      <style>
  .ui-widget {
    font-size: 11px;
  }
  .dialog-drop-shadow {
    -moz-box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.5);
    -webkit-box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.5);
    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.5);
  }
  #tabs.ui-widget-content {
    border: none;
  }
  .ui-tabs .ui-tabs-panel {
    background-color: #ffffff;
  }
  .ui-datepicker-trigger {
    vertical-align: bottom;
    margin-bottom: 2px;
    margin-left: 2px;
  }
</style>
	</head>

	<body>
		<div id="container">
			<div id="left">
				<div id="screen">
	  			</div>
	  			<div id="underbar">

	  			</div>
			</div>
	  		<div id="sidebar">
	  			<div id="tweetHeader">
	  				<h1 id="tweetHeaderText">
	  				</h1>
	  			</div>
	  			<div id="tweetsContainer">
	  			</div>
	  		</div>
	  	</div>
	</body>

<script type="text/javascript" src="Highcharts-4.0.4/js/highcharts.js"></script>

<!-- Javascript source -->

<!-- Define all the config and global variables first -->
<script type="text/javascript" src="draw.js"></script>
<script type="text/javascript" src="global-var.js"></script>
<script type="text/javascript" src="html.js"></script>
<script type="text/javascript" src="example.js">
</script>

<script type="text/javascript" src="timeline.js">
</script>

	<script type="text/javascript" src="http://altstudentsuccess.com/localhost/d3.min.js"></script>
  <script type="text/javascript" src="http://altstudentsuccess.com/localhost/tweet.js"></script>
	<script type="text/javascript" src="http://altstudentsuccess.com/localhost/updateSidebar.js"></script>
	<script type="text/javascript" src="http://altstudentsuccess.com/localhost//updateBottom.js"></script>

	<script type='text/javascript'>
	  console.log("My javascript! - Andrew");
    var newTweetFunc = function() {
      console.log("Posting power Andrew!!!");
	    $.ajax({
	    	url: '172.16.3.13:8080',
	    	method:'post',
	    	success: function(data) {
	    	  console.log('I have received data!');
	    	  console.log(data);
	    	  //jData = JSON.parse(data);
	    	  //console.log(jData);
          jData = data;
          console.log('I haz tweets: ' + jData.text);
          console.log('I haz sentiment' + jData.sentiment);

	    	  addTweet(jData.user.screen_name, jData.text, jData.sentiment);

	    	  //var tweetLI = document.createElement('div');
	    	  //tweetLI.innerHTML = jData.text;
	    	  //tweetLI.style.color = 'white';
	    	  //document.getElementById('underbar').appendChild(tweetLI);
	    	  //document.getElementById('tweetsContainer').appendChild(tweetLI);
	    	  //document.getElementById('tweetHeaderText').text = jData.text;

	    	}
	    	});
    }
    var intervalID = setInterval(newTweetFunc, 5000);
	</script>
</html>


"""

tweetJsonQueue = Queue.Queue()


class streamThread (threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name
		
	def run(self):
		print 'Streaming thread is starting'
		l = StdOutListener()
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		stream = Stream(auth, l)
		print "About to start Stream"
		stream.filter(track=['gonegirl'])
		#time.sleep(5)

class tvHandler (BaseHTTPRequestHandler):
	def do_GET(self):
		print 'GET!'
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		#self.wfile.write("Hello World")
		self.wfile.write(templateHTML)
		#add other code to html file here
		return

	def do_POST(self):
		print 'POST! We will send back JSON!'
		self.send_response(200)
		self.send_header('Content-type', 'text/json')
		self.end_headers()
		if not tweetJsonQueue.empty():
		  self.wfile.write(tweetJsonQueue.get())
		return

class serverThread(threading.Thread):
	def __init__(self, name):
	  threading.Thread.__init__(self)
	  self.name = name

	def startServer(self):
		try:
			server = HTTPServer(('',PORT_NUMBER), tvHandler)
			print "Server started"
			server.serve_forever()    	
		except Exception, e:
			print 'SERVER ERROR ANDREW'
			raise

	def run(self):
		self.startServer()



class StdOutListener(StreamListener):
  """ A listener handles tweets are the received from the stream.
  This is a basic listener that just prints received tweets to stdout.
  """
  def on_data(self, data):
    print "TWEET: \n"
    print data

    #jResponse = json.loads(data)
    #jResponse = data
    #if 'created_at' in jResponse:
      #time = jResponse['created_at']
    #calculate sentiment
    #if 'text' in jResponse:
    	#sent = self.getSentiment(jResponse["text"])

    #text = jResponse["text"]
    #jsonObj = {'time':time, 'sentiment':sent, 'text':text}
    #jsonObj.time = time
    #jsonObj.sentiment = sent
   

    #tweetJsonQueue.put(json.dumps(jsonObj))
    jResponse = json.loads(data)
    if 'text' in jResponse:
      sentiVal = getTextSentiment(jResponse["text"]);

    jResponse["sentiment"] = sentiVal
    jsonString = json.dumps(jResponse)
    tweetJsonQueue.put(jsonString)
    return True

 

def getTextSentiment(text):
    
  # format for idol api
  text = text.replace('#', '')
  text = text.replace(' ', '+')
    
  # create query url
  url = 'https://api.idolondemand.com/1/api/sync/analyzesentiment/v1?text='
  url = url + text
  url = url + '&apikey=a4ee749a-0deb-4ff4-800d-7b00e1290151'
    
  # query
  response = requests.get(url)
    
  # return 0 if fail
  if 'aggregate' in response.json().keys():
  	print 'Found sentiment! ', response.json()['aggregate']['score']
  	return response.json()['aggregate']['score']
  else:
    return 0


def on_error(self, status):
  print status



if __name__ == '__main__':
	t1 = streamThread("stream thread")
	t2 = serverThread("Server Thread")
	t1.start()
	t2.start()
    
