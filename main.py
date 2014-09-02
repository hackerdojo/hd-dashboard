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
      values["isLogin"] = True
      values["login_text"] = "Login"
      values["greeting"] = ""
    else:
      values["isLogin"] = False
      values["login_text"] = "Logout %s" % (user.nickname())
    # If we're in the dev version, it should send people to the dev version of
    # other apps.
    if dev:
      values["dev_message"] = "You are using the dev version of Dashboard."
      values["signup_url"] = "http://signup-dev.appspot.com"
    else:
      values["signup_url"] = "http://signup.hackerdojo.com"

    self.response.out.write(template.render("main.html", values))

application = webapp2.WSGIApplication([
    ("/", MainHandler),
    ], debug=True)  
