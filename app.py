from blueprints.cli_bp import db_commands
from blueprints.categories_bp import categories_bp
from blueprints.languages_bp import languages_bp
from blueprints.stacks_bp import stacks_bp
from blueprints.tools_bp import tools_bp
from blueprints.users_bp import users_bp

from setup import app


app.register_blueprint(db_commands)
app.register_blueprint(categories_bp)
app.register_blueprint(languages_bp)
app.register_blueprint(stacks_bp)
app.register_blueprint(tools_bp)
app.register_blueprint(users_bp)


# print(app.url_map)