# YouNow API  
  
YouNow API wrapper for python :)  
## Dependencies & setup:  
You will need to install requests framework (if you don't have it yet... I hope you do...)  
Since I don't have a pip setup yet, You'll just need to download the YouNow.py file and put it in the same folder as your script that you write. 
```
from YouNow import YouNow
```
  
## Documentation  
  
Get Trending Users:  
(YouNow API only allows us to pull 50 users at a time from trending. So, if you want the first 50 users, you pass startFrom=0 into the second argument. If you want the next 50 users, you pass startFrom=50 into the second argument. Etc etc)  
```
## THIS will put all trending users in json format, and print the top 50 trending usernames with their viewcount
users = YouNow.getTrendingUsers(startFrom=0)

for i in users['trending_users']:
    username = i['username']
    viewers = i['viewers']
    print(username + " has " + str(viewers) + " viewers")
```  
  
Get Trending Tags:  
```  
data = YouNow.getTrendingTags() 
print(data)  
```   
Get list of people following a certain user. Their "fans" lol  
```
YouNow.getFans(userID, startFrom)
##startFrom=0 will start from beginning of list, I think it's pulling 10 at a time. Write a loop to get bigger list :)
```  
    
Follow A User (requires google login):
```
YouNow.follow(userID, channelID, broadcastID)
##that will follow them. Currently investigating to see if broadcastID and channelID are relevant formdata, but for now, it's safe to pass those in as well. This function will be inoperable until i get oauth2 working. we need to have a google session logged in
```  
All of the data is in JSON, but thanks to JSON+requests, you can simply call certain values in the output just as if it were a regular python list :)
