import requests
import pickle
import json




class YouNow:

    def getTrendingTags(self):
        getTrending = "https://cdn.younow.com/php/api/younow/dashboard/locale=en/trending=50"
        response = requests.get(getTrending)
        response.raise_for_status()
        data = response.json()['trending_tags']
        print(data)

    def getTrendingUsers(self):
        getTrending = "https://cdn.younow.com/php/api/younow/dashboard/locale=en/trending=50"
        response = requests.get(getTrending)
        response.raise_for_status()
        data = response.json()['trending_users']
        print(data)
