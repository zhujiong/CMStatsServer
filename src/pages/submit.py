from base import BasePage
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Device

class SubmitPage(BasePage):
    def get(self):
        kwargs = {
            'key_name': self.request.get('id'),
            'type': self.request.get('type'),
            'version': self.request.get('version'),
            'country': self.request.get('country'),
            'carrier': self.request.get('carrier'),
            'ip': self.request.remote_addr,
        }
        Device.add(**kwargs)

    def post(self):
        kwargs = {
            'key_name': self.request.get('id'),
            'type': self.request.get('type'),
            'version': self.request.get('version'),
            'country': self.request.get('country'),
            'carrier': self.request.get('carrier'),
            'ip': self.request.remote_addr,
        }
        Device.add(**kwargs)

application = webapp.WSGIApplication(
        [('/submit', SubmitPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
