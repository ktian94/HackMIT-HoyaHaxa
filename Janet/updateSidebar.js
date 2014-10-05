var tweets = [];

var sidebar = document.getElementById("sidebar");
var underbar = document.getElementById("underbar");
underbar.innerHTML = "OTHER STUFF GOES HERE";

var hashtag = '#hackMIT';
var tweetHeaderText = document.getElementById('tweetHeaderText');
tweetHeaderText.innerHTML = hashtag;

function getJSONs(){
    //Retrieves data from Twitter
    try {
        
    } catch(err){
        console.error('Check your internet connection!');
    }
}

tweets[0] = new Tweet('janetzoo', 'url', 'tweet tweet tweet tweet tweet tweet #hackMIT', 0.7);
tweets[1] = new Tweet('ktian94', 'url', 'testing #nodejs #hackMIT', 0.9);
tweets[2] = new Tweet('AndrewsTwitter', 'url', 'i like to eat eat eat apples and bananas #hackMIT', 0);
tweets[3] = new Tweet('JordanIsKing', 'url', 'I\'m hungry #hackmit', -0.5);

for(var n = 4; n < 15; n++){
	tweets[n] = new Tweet('JordanIsKing', 'url', 'I\'m hungry #hackmit', -0.5);
}

var tweetDiv = document.getElementById('tweetsContainer');

for (var i = 0; i < tweets.length; i++) {
	var curTweet = tweets[i];

	var newTweet = document.createElement("DIV");
	newTweet.className = 'newTweet';
	newTweet.style.backgroundColor = getSentimentColor(curTweet.sentiment);
	var twitterHandleHeader = document.createElement("H2");
	twitterHandleHeader.className = 'twitterHandleHeader';
	var twitterHandle = document.createTextNode(curTweet.contents);
	twitterHandleHeader.appendChild(twitterHandle);
	newTweet.appendChild(twitterHandleHeader);
	var tweetContentsDiv = document.createElement("DIV");
	tweetContentsDiv.className = 'tweetContentsDiv';
	var tweetContents = document.createTextNode(curTweet.handle);
	tweetContentsDiv.appendChild(tweetContents);
	newTweet.appendChild(tweetContentsDiv);
	tweetDiv.appendChild(newTweet);
};

function getSentimentColor(sentimentValue) {
	var color = d3.scale.linear()
    	.domain([-1, 0, 1])
    	.range(["#FF0033", "#989898", "#009933"]);
 
	return color(sentimentValue);
}