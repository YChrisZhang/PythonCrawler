#Crawler1Qiubai

Qiubai doesn't need to log in to get its information,so we don't need to make a simulation-login. And I decide to use the following method to craw some information from Qiubai.

1.Use urllib2 to request.
2.Use urlopen method to get a response.
3.Read the response.
4.Open a text-file and write the response in the file.

And after these steps you can read the jokes you craw by yourself from the text-file you've just wrotten.


#lianXiangCi

This crawler help you to get the associational words when you type in your key words in the Sina---a kind of seach engine focusing on news.And I implement the crawler by doing the following steps.

1.Get a target key word from keyboard.
2.Use urllib.quote method to encode the inputting into url form.
3.Create a regular headers to include important information like 'Get','Host','Referer'and 'User-Agent'.
3.To make our IP safe,I choose to use a proxy to void to be forbidden.And I dowmload some Ip address from the internet randomly and chose one of them every time I run this crawler.But there is one problem which is the Ip address from the internet may not be valid somtimes.As a result of that,this crawler may not work normally every time when you run it unless you use your own valid IP address.
4.Use urllib2.Request method to get the response from the server.
5.Write the result into a text-file.

And after these steps you can read the associational words related to the word you type in in the text file.


#getCookie

When we need to get a cookie from the website we can do it handfully by ourselves or we can use this crawler to achieve the same goal.

1.Build a cookieJar to memory the cookie.
2.Make a cookie processor to use it to build a opener.
3.Use open method and get a response.
4.Save the response to a file.

After these steps we will get the cookie from the target website.


#simulateLogin

Sometimes we have to log in to visit some kind of websites for their special users,for instance,we need to log in Sina Weibo to visit our own website.So if we need to crawl information like that,we have to make our crawler smarter which means it could simulate a login action.These are the following steps.

1.Make sure that you have already got the cookie of the website you need to login.
2.Create a headers just like before except adding a 'cookie' to the headers.
3.Use urllib2.Request method to make a request.
4.Use urllib.urlopen method to open the response.
5.Write your own regression to get what you want from the html file.

After these steps we can visit the website after login and extract some useful information we need.
