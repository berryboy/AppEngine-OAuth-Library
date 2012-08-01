#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import oauth

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class MainHandler(webapp2.RequestHandler):
	
    def get(self, mode=""):
	
	    application_key = "berryboy-2264" 
	    application_secret = "2d71e18eab062618"  

	    callback_url = "%s/verify" % self.request.host_url

	    client = oauth.EvernoteClient(application_key, application_secret, 
	        callback_url, True);

	    if mode == "login":
	      return self.redirect(client.get_authorization_url())

	    if mode == "verify":
	      auth_token = self.request.get("oauth_token")
	      auth_verifier = self.request.get("oauth_verifier")
	      user_info = client.get_user_info(auth_token, auth_verifier=auth_verifier)
	      return self.response.out.write(user_info)

	    self.response.out.write("<a href='/login'>Login via Evernote</a>")

				
app = webapp2.WSGIApplication([('/(.*)', MainHandler)],
                              debug=True)
