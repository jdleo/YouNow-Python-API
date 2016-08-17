# YouNow API  
  
YouNow API wrapper for python :)  
  
## Documentation  
  
Get Trending Users:  
(YouNow API only allows us to pull 50 users at a time from trending. So, if you want the first 50 users, you pass startFrom=0 into the second argument. If you want the next 50 users, you pass startFrom=50 into the second argument. Etc etc)
`data = YouNow.getTrendingUsers(None, startFrom=0)`  
`print(data)`
  
Get Trending Tags:  
`data = YouNow.getTrendingTags(None)`  
`print(data)`  
  
All of the data is in JSON, but thanks to JSON+requests, you can simply call certain values in the output just as if it were a regular python list :)
