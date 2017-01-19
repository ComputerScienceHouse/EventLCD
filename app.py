import yaml
from website import app
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, Application

try:
  with open('website/app.yaml', 'r') as f:
    config = yaml.load(f)
    app.config.update(config)
except:
  print('Missing/invalid config (app.yaml)')
  quit()

#app.run(debug=True, port=config['port'], host=config['host'])

application = Application([
  (r'.*', FallbackHandler, dict(fallback=WSGIContainer(app)))])

application.listen(config['port'])
IOLoop.instance().start()
