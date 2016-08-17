# YouNow API  
  
YouNow API wrapper for python :)  
  
## Documentation  
  
Get Trending Users:  
`data = YouNow.getTrendingUsers(None)`  
`print(data)`
  
Get Trending Tags:  
`data = YouNow.getTrendingTags(None)`  
`print(data)`  
  
All of the data is in JSON, but thanks to JSON+requests, you can simply call certain values in the output just as if it were a regular python list :)
