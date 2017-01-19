import yaml
import os
from website import app
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, Application

config = {
    "DEBUG": False,
    "IP": '0.0.0.0',
    "PORT": '8080',
    "calendar_id": os.environ.get('EVENTLCD_CALENDAR_ID', ''),
    "token": os.environ.get('EVENTLCD_CALENDAR_TOKEN', '')
}
app.config.update(config)

application = Application([
  (r'.*', FallbackHandler, dict(fallback=WSGIContainer(app)))])

application.listen(config['PORT'])
IOLoop.instance().start()
