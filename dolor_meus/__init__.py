import os

from flask import Flask

from . import home
from . import request

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
      SECRET_KEY='dev'
  )

  app.register_blueprint(home.bp)
  app.register_blueprint(request.bp)

  if test_config is None:
      # load the instance config, if it exists, when not testing
      app.config.from_pyfile('config.py', silent=True)
  else:
      # load the test config if passed in
      app.config.from_mapping(test_config)

  # ensure the instance folder exists
  try:
      os.makedirs(app.instance_path)
  except OSError:
      pass

  if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(debug=False, host='0.0.0.0', port=port)

  return app
