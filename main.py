#!/usr/bin/env python

import webapp2
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp


class MainHandler(webapp2.RequestHandler):

  def get(self):
    self.response.out.write(template.render('main.html', locals()))


application = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)  