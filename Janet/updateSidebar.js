var tweets = [];
var curTweetIndex = 0;

var sidebar = document.getElementById("sidebar");
var underbar = document.getElementById("underbar");
var tweetDiv = document.getElementById('tweetsContainer');
//underbar.innerHTML = "OTHER STUFF GOES HERE";

var tweetHeaderText = document.getElementById('tweetHeaderText');

// $.ajax({
//     "url": "http://172.16.0.155:8080/tv/getTuned",
//     "crossDomain": true,
//     "dataType": "jsonp"
// });
addHashtag("#hi");

function addHashtag(hashtag) {
	tweetHeaderText.innerHTML = hashtag;
}

function addTweet(handle, contents, sentiment) {
	tweets[curTweetIndex] = new Tweet(handle, contents, sentiment);
	updateTweets(curTweetIndex);
	curTweetIndex++;
}

tweets[0] = new Tweet('janetzoo', 'tweet tweet tweet tweet tweet tweet tweet tweet #hackMIT', 0.7);
updateTweets(0);
tweets[1] = new Tweet('ktian94', 'testing #nodejs #hackMIT', 0.9);
updateTweets(1);
tweets[2] = new Tweet('AndrewsTwitter', 'i like to eat eat eat apples and bananas #hackMIT', 0);
tweets[3] = new Tweet('JordanIsKing', 'I\'m hungry #hackmit', -0.5);

for(var n = 4; n < 12; n++){
	tweets[n] = new Tweet('JordanIsKing', 'url', 'I\'m hungry #hackmit', -0.5);
}

function updateTweets(index) {
	var curTweet = tweets[index];

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
}

function getSentimentColor(sentimentValue) {
	var color = d3.scale.linear()
    	.domain([-1, 0, 1])
    	.range(["#FF0033", "#989898", "#009933"]);
 
	return color(sentimentValue);
}