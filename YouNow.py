import requests
import pickle
import json




class YouNow:

    def getTrendingTags(self):
        getTrending = "https://cdn.younow.com/php/api/younow/dashboard/locale=en/trending=50"
        response = requests.get(getTrending)
        response.raise_for_status()
        data = response.json()['trending_tags']
        return data

    def getTrendingUsers(self, startFrom):
        getTrending = "https://api.younow.com/php/api/younow/trendingUsers/locale=en/numberOfRecords=50/startFrom=%s" % startFrom
        response = requests.get(getTrending)
        response.raise_for_status()
        data = response.json()
        return data

