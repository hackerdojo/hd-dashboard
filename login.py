#!/usr/bin/env python

import webapp2

from google.appengine.api import users


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            # Logging in.
            self.redirect(users.create_login_url("/"))
        else:
            # Logging out.
            self.redirect(users.create_logout_url("/"))


application = webapp2.WSGIApplication([
    ("/login", LoginHandler),
], debug=True)
