import os

class Config(object):
    #########################
    #   REQUIRED SETTINGS   #
    #########################

    # Cache
    CACHE_TYPE=os.environ.get('CACHE_TYPE') or 'simple'

    # Google
    GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY') 
