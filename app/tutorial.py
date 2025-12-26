#https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow query parameters...

#tools to use
import requests
import json

#this just does everything automatically for you
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

#very intuitive, you can pretty much take the information as if it were a db
for questions in response.json()['items']:
    print(questions['title'])
    print(questions['link'])
    print()