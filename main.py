#!/usr/bin/env python
import logging

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
            values["isLogin"] = False
            values["login_text"] = "Login"
            values["greeting"] = ""
        else:
            values["isLogin"] = True
            values["login_text"] = "Logout %s" % (user.nickname())
        # If we're in the dev version, it should send people to the dev version of
        # other apps.
        if dev:
            values["dev_message"] = "You are using the dev version of Dashboard."
            values["signup_url"] = "https://signup-dev.appspot.com"
        else:
            values["signup_url"] = "http://signup.hackerdojo.com"

        self.response.out.write(template.render("main.html", values))


class LockerHandler(webapp2.RequestHandler):
    def get(self):
        # Check if we're in the dev version.
        url = self.request.url
        dev = False
        if "-dev" in url:
            dev = True

        user = users.get_current_user()
        values = {}
        if not user:
            values["isLogin"] = False
            values["login_text"] = "Login"
            values["greeting"] = ""
            values['member_email'] = ""
            self.redirect("/login")
            return
        else:
            values['member_email'] = user.email()
            values["isLogin"] = True
            values["login_text"] = "Logout %s" % (user.nickname())

        self.response.out.write(template.render("locker.html", values))


class LockerConfirmationHandler(webapp2.RequestHandler):
    def get(self):
        # Check if we're in the dev version.
        url = self.request.url
        dev = False
        if "-dev" in url:
            dev = True

        user = users.get_current_user()
        values = {}
        if not user:
            values["isLogin"] = False
            values["login_text"] = "Login"
            values["greeting"] = ""
            values['member_email'] = ""
        else:
            values['member_email'] = user.email()
            values["isLogin"] = True
            values["login_text"] = "Logout %s" % (user.nickname())

        self.response.out.write(template.render("lockerconfirmation.html", values))


class MailboxHandler(webapp2.RequestHandler):
    def get(self):
        # Check if we're in the dev version.
        url = self.request.url
        dev = False
        if "-dev" in url:
            dev = True

        user = users.get_current_user()
        values = {}
        if not user:
            values["isLogin"] = False
            values["login_text"] = "Login"
            values["greeting"] = ""
            values['member_email'] = ""
            self.redirect("/login")
            return
        else:
            values['member_email'] = user.email()
            values["isLogin"] = True
            values["login_text"] = "Logout %s" % (user.nickname())

        self.response.out.write(template.render("mailbox.html", values))


class MailboxConfirmationHandler(webapp2.RequestHandler):
    def get(self):
        # Check if we're in the dev version.
        url = self.request.url
        dev = False
        if "-dev" in url:
            dev = True

        user = users.get_current_user()
        values = {}
        if not user:
            values["isLogin"] = False
            values["login_text"] = "Login"
            values["greeting"] = ""
            values['member_email'] = ""
        else:
            values['member_email'] = user.email()
            values["isLogin"] = True
            values["login_text"] = "Logout %s" % (user.nickname())

        self.response.out.write(template.render("mailboxconfirmation.html", values))


class MailboxSoldOutHandler(webapp2.RequestHandler):
    def get(self):
        # Check if we're in the dev version.
        url = self.request.url
        dev = False
        if "-dev" in url:
            dev = True

        user = users.get_current_user()
        values = {}
        if not user:
            values["isLogin"] = False
            values["login_text"] = "Login"
            values["greeting"] = ""
            values['member_email'] = ""
        else:
            values['member_email'] = user.email()
            values["isLogin"] = True
            values["login_text"] = "Logout %s" % (user.nickname())

        self.response.out.write(template.render("mailboxsoldout.html", values))

class StartupHandler(webapp2.RequestHandler):
    def get(self):
        # Check if we're in the dev version.
        url = self.request.url
        dev = False
        if "-dev" in url:
            dev = True

        user = users.get_current_user()
        values = {}
        if not user:
            values["isLogin"] = False
            values["login_text"] = "Login"
            values["greeting"] = ""
            values['member_email'] = ""
            self.redirect("/login")
            return
        else:
            values['member_email'] = user.email()
            values["isLogin"] = True
            values["login_text"] = "Logout %s" % (user.nickname())

        self.response.out.write(template.render("startup.html", values))


class StartupConfirmationHandler(webapp2.RequestHandler):
    def get(self):
        # Check if we're in the dev version.
        url = self.request.url
        dev = False
        if "-dev" in url:
            dev = True

        user = users.get_current_user()
        values = {}
        if not user:
            values["isLogin"] = False
            values["login_text"] = "Login"
            values["greeting"] = ""
            values['member_email'] = ""
        else:
            values['member_email'] = user.email()
            values["isLogin"] = True
            values["login_text"] = "Logout %s" % (user.nickname())

        self.response.out.write(template.render("startupconfirmation.html", values))



application = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/locker", LockerHandler),
    ("/mailbox", MailboxHandler),
    ("/startup", StartupHandler),

], debug=True)
