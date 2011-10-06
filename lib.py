import re
import warnings


#
# http://code.activestate.com/recipes/391367-deprecated/
#
def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used."""
    def newFunc(*args, **kwargs):
        warnings.warn("Call to deprecated function %s." % func.__name__,
                      category=DeprecationWarning)
        return func(*args, **kwargs)
    newFunc.__name__ = func.__name__
    newFunc.__doc__ = func.__doc__
    newFunc.__dict__.update(func.__dict__)
    return newFunc
    
def split_words(sentence):
    """The function name itself is self-explanatory."""
    return map(lambda x: x.lower(), re.findall(r'\w+', sentence, re.UNICODE))
    
def count_word_frequency(sentence):
    """The function name itself is self-explanatory."""
    freq = {}
    for word in split_words(sentence):
        if not word in freq:
            freq[word] = 1
        else:
            freq[word] += 1
        
    return freq

def unique_users(comments):
    """
    Calculates the number of unique users who wrote comments on a partigular entity (i.e. status, picture, etc.)
    
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
    """
    users = set()
    
    for comment in comments['data']:
        user = comment['from']
        
        users.add(hashabledict(user))
        
    return users
    
#
# http://stackoverflow.com/questions/1151658/python-hashable-dicts
#
class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))
    