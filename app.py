from blueprints.cli_bp import db_commands
from blueprints.categories_bp import categories_bp
# from blueprints.cards_bp import cards_bp
from setup import app


app.register_blueprint(db_commands)
app.register_blueprint(categories_bp)
# app.register_blueprint(cards_bp)

print(app.url_map)