#this is tutorial code on how to consume an API

#https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow query parameters...

#tools to use
import requests
import json

#this just does everything automatically for you
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

#very intuitive, you can pretty much take the information as if it were a db
for questions in response.json()['items']:
    if questions['answer_count'] == 0:
        print(questions['title'])
        print(questions['link'])
    else:
        print('skipped')
    print()