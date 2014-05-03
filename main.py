#!/usr/bin/env python

import webapp2
from google.appengine.api import users
from google.appengine.ext.webapp import template
#from google.appengine.ext import webapi

class MainHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    values = {}
    if not user:
      values["login_text"] = "Login"
    else:
      values["login_text"] = "Logout"

    self.response.out.write(template.render("main.html", values))

application = webapp2.WSGIApplication([
    ("/", MainHandler),
], debug=True)  
