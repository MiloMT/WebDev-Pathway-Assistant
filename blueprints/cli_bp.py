# from datetime import date
from setup import db, bcrypt
from flask import Blueprint

from models.category import Category
from models.language import Language
# from models.user_plan import User_Plan
from models.stack_tool import Stack_Tool
from models.stack import Stack
from models.tool_step import Tool_Step
from models.tool import Tool
from models.user_tool import User_Tool
from models.user import User

db_commands = Blueprint("db", "__name__")

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")

@db_commands.cli.command("seed")
def db_seed():
    
    
    # Categories
    categories = [
        Category(
            name = "Framework",
            description = "A framework"
        ),
        Category(
            name = "Tool",
            description = "A tool"
        ),
        Category(
            name = "Software",
            description = "A software"
        ),
    ]
    
    db.session.add_all(categories)
    db.session.commit()
    
    # Languages
    languages = [
        Language(
            name = "Python"
        ),
        Language(
            name = "Javascript"
        ),
        Language(
            name = "C#"
        ),
    ]
    
    db.session.add_all(languages)
    db.session.commit()
    
    # Stacks
    stacks = [
        Stack(
            name = "Stack 1",
            description = "Stack 1"
        ),
        Stack(
            name = "Stack 2",
            description = "Stack 2"
        ),
        Stack(
            name = "Stack 3",
            description = "Stack 3"
        ),
    ]
    
    db.session.add_all(stacks)
    db.session.commit()
    
    # Tools
    tools = [
        Tool(
            name = "Tool 1",
            description = "Tool 1",
            category_id = categories[0].id,
            language_id = languages[0].id
        ),
        Tool(
            name = "Tool 2",
            description = "Tool 2",
            category_id = categories[1].id,
            language_id = languages[1].id
        ),
        Tool(
            name = "Tool 3",
            description = "Tool 3",
            category_id = categories[2].id,
            language_id = languages[2].id
        ),
    ]
    
    db.session.add_all(tools)
    db.session.commit()
    
    # Tool Steps
    tool_steps = [
        Tool_Step(
            step_no = "1",
            description = "The first step",
            time_days = "2",
            tool_id = tools[0].id
        ),
        Tool_Step(
            step_no = "2",
            description = "The second step",
            time_days = "1",
            tool_id = tools[0].id
        ),
        Tool_Step(
            step_no = "3",
            description = "The second step",
            time_days = "3",
            tool_id = tools[0].id
        ),
    ]
    
    db.session.add_all(tool_steps)
    db.session.commit()
    
    # Users
    users = [
        User(
            name = "Admin User",
            email = "admin@test.com",
            password = bcrypt.generate_password_hash("adminadmin").decode("utf8"),
            is_admin = True
        ), 
        User(
            name = "Test User",
            email = "test@test.com",
            password = bcrypt.generate_password_hash("password").decode("utf8")
        ), 
    ]
    
    db.session.add_all(users)
    db.session.commit()

    # Stack Tools
    stack_tools = [
        Stack_Tool(
            stack_id = stacks[0].id,
            tool_id = tools[0].id
        ),
        Stack_Tool(
            stack_id = stacks[0].id,
            tool_id = tools[1].id
        ),
        Stack_Tool(
            stack_id = stacks[0].id,
            tool_id = tools[2].id
        ),
    ]
    
    db.session.add_all(stack_tools)
    db.session.commit()
    
    # User Tools
    user_tools = [
        User_Tool(
            user_id = users[0].id,
            tool_id = tools[0].id
        ),
        User_Tool(
            user_id = users[0].id,
            tool_id = tools[1].id
        ),
        User_Tool(
            user_id = users[0].id,
            tool_id = tools[2].id
        ),
    ]
    
    db.session.add_all(user_tools)
    db.session.commit()

    print("Database seeded")