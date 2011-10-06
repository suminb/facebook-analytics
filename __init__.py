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

like_weight = 1.0
comment_weight = 2.0
comment_weight_by_nonunique_user = 1.1
#unique_user_commented_weight = 

for entry in fetch(uid, 'statuses', token)['data']:
    print entry['message'][:48]
    
    message = entry['message']
    like_count = len(entry['likes']['data']) if 'likes' in entry else 0
    comment_count = len(entry['comments']['data'])
    unique_users_commented = len(unique_users(entry['comments']))
    
    weighed_score = sum((like_count*like_weight,
            unique_users_commented*comment_weight,
            (comment_count-unique_users_commented)*comment_weight_by_nonunique_user
    ))
            
    print weighed_score
    

    