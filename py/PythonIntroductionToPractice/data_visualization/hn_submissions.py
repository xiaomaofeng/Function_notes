import requests

from operator import itemgetter

#executing APi call, and storage response
url = 'https://hacker-news.firebaseio.com/v0/topstorie.json'
r = requests.get(url)
print("Status code: ", r.status_code)

#processing information about each article
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    #for each article,excuting API call
    url = ('http://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + 'json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {'title': response_dict['title'],
                       'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
                       'comments': response_dict.get('descendants', 0)
                       }
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

    for submission_dict in submission_dicts:
        print("\nTitile:", submission_dict['title'])
        print("Disscussion link:", submission_dict['link'])
        print("Comments:", submission_dict['comments'])

