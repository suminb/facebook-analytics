import operator

from fetch import *
from lib import *

#friend_ids = get_friend_ids(fetch_friends())
uid = CONFIG['uid']
token = CONFIG['token']

"""
Overview of data structure

"data": [
    {
      "id": "", 
      "from": {
        "name": "", 
        "id": ""
      }, 
      "message": "", 
      "updated_time": "2011-10-06T10:59:35+0000", 
      "likes": {
        "data": [
          {
            "id": "", 
            "name": ""
          },
        ]
      }, 
      "comments": {
        "data": [
          {
            "id": "", 
            "from": {
              "name": "", 
              "id": ""
            }, 
            "message": "", 
            "can_remove": true, 
            "created_time": ""
          }, 
        ]
      }
    ]
}
"""

"""
entries = {'data':[]}
for uid in get_friend_ids(fetch_friends()) + [CONFIG['uid']]:
    try:
        statuses = fetch(uid, 'statuses', token)
        
        for status in statuses['data']:
            print status['from'], status['message'][:40]
        
        entries['data'] += statuses['data']
    except Exception, e:
        print e

f = open('entries.json', 'w')
f.write(json.dumps(entries))
f.close()

"""

like_weight = 1.25
comment_weight = 2.0
comment_weight_by_nonunique_user = 1.1
#unique_user_commented_weight = 

freq = {}

#for entry in json.loads(open('entries.json').read())['data']:
for entry in fetch(CONFIG['uid'], 'statuses', token)['data']:
    message = entry['message']
    like_count = len(entry['likes']['data']) if 'likes' in entry else 0
    
    if 'comments' in entry:
        comment_count = len(entry['comments']['data'])
        unique_users_commented = len(unique_users(entry['comments']))
    else:
        comment_count = 0
        unique_users_commented = 0
    
    weighed_score = sum((like_count*like_weight,
            unique_users_commented*comment_weight,
            (comment_count-unique_users_commented)*comment_weight_by_nonunique_user
    ))
            
    words = split_words(message)
    for word in words:
        if not word in freq: freq[word] = 0.0
        
        freq[word] += weighed_score

            
# Sorting words by their 'value' in ascending order
ranks = sorted(freq.iteritems(), key=operator.itemgetter(1), reverse=True)

print ranks
print 'Analyzed %d entries' % len(ranks)

print ' '.join(map(lambda x: x[0], ranks[:25]))

