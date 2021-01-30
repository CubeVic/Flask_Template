from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_redis import FlaskRedis

# Global accessible libraries
# db = SQLAlchemy()
# r = FlaskRedis()

def create_app(): 
    """ Initialize the core application """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize plug-ins
    # db.init_app(app)
    # r.init_app(app)

    with app.app_context():

        # Include routes
        from .home import home
        from .forms import routes

        # register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(routes.form_sign_in_bp)
        # app.register_blueprint(auth.auth_bp)
        # app.register_blueprint(admin.admin_bp)

        return app