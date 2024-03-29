import json
import urllib2

from lib import deprecated

def get_config():
    """Note: This function assumes 'config.json' file exists in the same directory."""
    f = open('config.json')
    config = json.loads(f.read())
    f.close()
    
    return config

@deprecated
def get_token():
    """Note: This function assumes 'token.txt' file exists in the same directory."""
    f = open('token.txt')
    token = f.read()
    f.close()
    
    return token
    
def get_statuses(uid, token):
    entries = fetch(uid, 'statuses', token)
    
    return entries['data']
    
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
    
    url = 'https://graph.facebook.com/%d/%s?limit=400&access_token=%s' % (uid, object, token)
    print url

    f = urllib2.urlopen(url)
    data = f.read() # Expects JSON responsees
    f.close()
    
    return json.loads(data)
    
def export_as_json(dict, filename):
    """dict: A JSON serializable dictionary object."""
    f = open(filename, 'w')
    f.write(json.dumps(dict))
    f.close()

def get_friend_ids(friends):
    """Expects a dictionary object parsed from Facebook Graph API output."""
    return map(lambda x: int(x['id']), friends['data'])

CONFIG = get_config()