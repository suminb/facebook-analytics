import json
import urllib2

def get_token():
    f = open('token.txt')
    token = f.read()
    f.close()
    
    return token
    
def fetch_friends():
    """Note: This function assumes 'friends.json' file exists in the same directory."""
    f = open('friends.json')
    friends = json.loads(f.read())
    f.close()
    
    return friends

def fetch(uid, object, token):
    """uid: Facebook user ID (integer)
       object: Object to be fetched (statuses, friends, likes, ...)
       token: Facebook access token
    """
    
    url = 'https://graph.facebook.com/%d/%s?access_token=%s' % (uid, object, token)
    print url
    
    f = urllib2.urlopen(url)
    data = f.read() # Expects JSON responsees
    f.close()
    
    return json.loads(data)
    

token = get_token()

#friends = fetch(10132775, 'friends', token)

#f = open('friends.json', 'w')
#f.write(json.dumps(friends))
#f.close()

