import requests
import pickle
import json




class YouNow:

    def getTrendingTags():
        getTrending = "https://cdn.younow.com/php/api/younow/dashboard/locale=en/trending=50"
        response = requests.get(getTrending)
        response.raise_for_status()
        data = response.json()['trending_tags']
        return data

    def getTrendingUsers(startFrom):
        getTrending = "https://api.younow.com/php/api/younow/trendingUsers/locale=en/numberOfRecords=50/startFrom=%s" % startFrom
        response = requests.get(getTrending)
        response.raise_for_status()
        data = response.json()
        return data

    def follow(userID, channelID, broadcastID):
        followUser = "https://api.younow.com/php/api/channel/fan"
        _userID = userID
        _channelID = channelID
        _broadcastID = broadcastID
        headers = {'User-Agent': 'Mozilla/5.0'}
        payload = {'userId' :_userID, 'channelId':_channelID, 'broadcastId':_broadcastID, 'fan_type':'BROADCAST'}
        session = requests.Session()
        followed = session.post(followUser, headers=headers, data=payload)
        print(followed)

    def getFans(userID, startFrom):
        fansUrl = "https://cdn.younow.com/php/api/channel/getFans/channelId=%s/startFrom=%s" % (userID, startFrom)
        response = requests.get(fansUrl)
        response.raise_for_status()
        data = response.json()
        return data['fans']
