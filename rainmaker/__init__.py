"""
Api for rainmaker V1.0
"""
import json
import logging
import urllib
import urllib2

API_VERSION = "v1"
API_ENDPOINT = "http://api.rainmaker.cc/%(version)s/" % {'version': API_VERSION}

CLIENT_VERSION = "1.0"
USER_AGENT = "rainmaker python client v%s" % CLIENT_VERSION

class RainmakerException():
    pass

class RainMaker():
    def __init__(self, api_key):
        self.api_key = api_key

    def helper(self, path, method="GET", vars={}):
        """
        Helper function to get a remote url and return the json results as a
        dictionary.
        """        
        # Kludgey hack for getting variables safe for urllib
        str_values = {}
        for k, v in vars.iteritems():
            str_values[k] = unicode(v).encode('utf-8')        
        

        if method == "GET":
            # Mux in the api key to the get variables
            str_values['apiKey'] = self.api_key

            # Generate the get request string
            data = urllib.urlencode(str_values)

            # Compute the correct path
            url = "%s%s?%s" % (API_ENDPOINT, path, data)
            
            # Construct the request as a get
            request = urllib2.Request(url)
        
        elif method == "POST":
            # Compute the correct url to post to
            url = "%s%s?apiKey=%s" % (API_ENDPOINT, path, self.api_key)
            
            # Now go and build the request
            request = urllib2.Request(url, data)

        # Force a reasonable user-agent
        request.add_header('User-Agent',USER_AGENT)

        try:
            response = urllib2.urlopen(request)
            return json.load(response)
        except urllib2.URLError, e:
            logging.error(e.code, e.read())
            raise RainmakerException()

    def do_lookup(self, email="lorangb@gmail.com"):
        return self.helper("person.json", method="GET", vars={'email':email})
