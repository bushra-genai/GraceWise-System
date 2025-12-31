from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.dashboard import dashboard_bp
from routes.devotionals import devotionals_bp
from routes.child_progress import child_progress_bp
from routes.planner import planner_bp
from routes.curriculum import curriculum_bp
from models import db  # import db from models.py

#Create Flask app
app = Flask(__name__)

#Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/gracewise" # simple SQLite DB for testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize database with app
db.init_app(app)

#Register blueprint
app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
app.register_blueprint(devotionals_bp, url_prefix="/devotionals")
app.register_blueprint(child_progress_bp, url_prefix="/child_progress")
app.register_blueprint(planner_bp, url_prefix="/planner")
app.register_blueprint(curriculum_bp, url_prefix="/curriculum")


#Create tables (optional, for first run)
with app.app_context():
    db.create_all()

#Run the app
if __name__ == "__main__":
    app.run(debug=True)
