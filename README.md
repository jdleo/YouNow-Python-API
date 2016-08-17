# YouNow API  
  
YouNow API wrapper for python :)  
  
## Documentation  
  
Get Trending Users:  
(YouNow API only allows us to pull 50 users at a time from trending. So, if you want the first 50 users, you pass startFrom=0 into the second argument. If you want the next 50 users, you pass startFrom=50 into the second argument. Etc etc)  
```
## THIS will put all trending users in json format, and print the top 50 trending usernames with their viewcount
users = YouNow.getTrendingUsers(None, startFrom=0)

for i in users['trending_users']:
    username = i['username']
    viewers = i['viewers']
    print(username + " has " + str(viewers) + " viewers")
```  
  
Get Trending Tags:  
`data = YouNow.getTrendingTags(None)`  
`print(data)`  
  
All of the data is in JSON, but thanks to JSON+requests, you can simply call certain values in the output just as if it were a regular python list :)
