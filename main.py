#!/usr/bin/env python

import webapp2
from google.appengine.api import users
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
  def get(self):
    # Check if we're in the dev version.
    url = self.request.url
    dev = False
    if "-dev" in url:
      dev = True

    user = users.get_current_user()
    values = {}
    if not user:
      values["login_text"] = "Login"
      values["greeting"] = ""
    else:
      values["login_text"] = "Logout"
      values["greeting"] = "Hello, %s!" % (user.nickname())
    # If we're in the dev version, it should send people to the dev version of
    # other apps.
    if dev:
      values["signup_url"] = "http://signup-dev.hackerdojo.com/key"
    else:
      values["signup_url"] = "http://signup.hackerdojo.com/key"

    self.response.out.write(template.render("main.html", values))

application = webapp2.WSGIApplication([
    ("/", MainHandler),
    ], debug=True)  
