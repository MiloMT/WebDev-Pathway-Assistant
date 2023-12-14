# T2A2 - API Webserver Project

[Github Repository](https://github.com/MiloMT/WebDev-Pathway-Assistant)  
[Github Project](https://github.com/users/MiloMT/projects/3)

## Problem Definition

When beginning a learning journey in web development, there are innumerable resources, tools and pathways a person can use and undergo. This can lodge individuals in a state of indecision when trying to navigate the best way to learn. Not only this, but the information surrounding tooling in web development is spread across a variety of sources, making it difficult to track down information about the variety of tools available and enlarging the task of effective learning.

## Problem Reasoning

This problem creates a lack of clarity surrounding the learning process in web development. This can cause anxiety, lost time and effort and a lack of direction for those wishing to develop their skills further in this field.

This API intends to remedy the above by creating a single source of truth that users can utilise to plan their learning approach to web development. It contains information on a variety of web development tools and the tech stacks that utilise these tools. It can also generate a learning plan based on the users needs, and provide suggestions on time frames for users to dedicate to the task.

## Database Selection



## ORM



## End Points

### /categories

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the names, IDs and descriptions of all categories within the table.

> Example Response

```json
[
	{
		"description": "A framework",
		"id": 1,
		"name": "Framework"
	},
	{
		"description": "A tool",
		"id": 2,
		"name": "Tool"
	},
	{
		"description": "A software",
		"id": 3,
		"name": "Software"
	}
]
```

- HTTP Request Verb: ```POST```
- Required Data: name (string(50), required), description (text)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to create a new category in the categories table and returns a JSON of the name, ID and description of the created category.

> Example Request

```json
{
	"name":"Created Category",
	"description":"Created Category Description"
}
```

> Example Response

```json
{
	"description": "Created Category Description",
	"id": 4,
	"name": "Created Category"
}
```

#### /categories/\<id> 

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the name, ID and description of a single category.

> Example Response

```json
{
	"description": "A framework",
	"id": 1,
	"name": "Framework"
}
```

- HTTP Request Verb: ```PUT``` ```PATCH```
- Required Data: name (char(50)), description (text) *missing fields will default to current data*
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to make adjustments to fields from an existing category and returns a JSON of the updated name, ID and description of the affected category.

> Example Request

```json
{
	"name":"Category Changed",
	"description":"Changed Description"
}
```

> Example Response

```json
{
	"description": "Changed Description",
	"id": 1,
	"name": "Category Changed"
}
```

- HTTP Request Verb: ```DELETE```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to delete single categories, provided there are no dependencies related to that category, and returns a JSON confirming the name of the category that has been deleted.

> Example Response

```json
{
	"status": "Created Category has been deleted"
}
```

### /languages  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the names and IDs of all languages within the table.

> Example Response

```json
[
	{
		"id": 1,
		"name": "Python"
	},
	{
		"id": 2,
		"name": "Javascript"
	},
	{
		"id": 3,
		"name": "C#"
	}
]
```

- HTTP Request Verb: ```POST```
- Required Data: name (string(50))
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to create a new language in the languages table and returns a JSON with the ID and name of the created language.

> Example Request

```json
{
	"name":"Test Language"
}
```

> Example Response

```json
{
	"id": 4,
	"name": "Test Language"
}
```

#### /languages/\<id>  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the name and ID of a single language.

> Example Response

```json
{
	"id": 1,
	"name": "Python"
}
```

- HTTP Request Verb: ```PUT``` ```PATCH```
- Required Data: name (string(50)) *missing fields will default to current data*
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to make adjustments to fields from an existing language and returns a JSON of the updated name and ID of the affected language.

> Example Request

```json
{
	"name":"language Changed"
}
```

> Example Response

```json
{
	"id": 1,
	"name": "language Changed"
}
```

- HTTP Request Verb: ```DELETE```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to delete single languages, provided there are no dependencies related to that language, and returns a JSON confirming the name of the language that has been deleted.

> Example Response

```json
{
	"status": "Test Language has been deleted"
}
```

### /stacks  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the names, IDs and descriptions of all stacks within the table.

> Example Response

```json
[
	{
		"description": "Stack 1",
		"id": 1,
		"name": "Stack 1"
	},
	{
		"description": "Stack 2",
		"id": 2,
		"name": "Stack 2"
	},
	{
		"description": "Stack 3",
		"id": 3,
		"name": "Stack 3"
	}
]
```

- HTTP Request Verb: ```POST```
- Required Data: name (string(50)), description (text)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to create a new stack in the stacks table and returns a JSON with the ID and name of the created language.

> Example Request

```json
{
	"name":"New Stack",
	"description": "New Stack descriptions"
}
```

> Example Response

```json
{
	"description": "New Stack descriptions",
	"id": 4,
	"name": "New Stack"
}
```

#### /stacks/\<id>  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the name, ID and description of a single stack.

> Example Response

```json
{
	"description": "Stack 1",
	"id": 1,
	"name": "Stack 1"
}
```

- HTTP Request Verb: ```PUT``` ```PATCH```
- Required Data: name (string(50)), description (text) *missing fields will default to current data*
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to make adjustments to fields from an existing stack and returns a JSON of the updated name, ID and description of the affected stack.

> Example Request

```json
{
	"name":"Changed Stack",
	"description": "Changed Stack description"
}
```

> Example Response

```json
{
	"description": "Changed Stack description",
	"id": 1,
	"name": "Changed Stack"
}
```

- HTTP Request Verb: ```DELETE```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to delete single stacks, provided there are no dependencies related to that stack, and returns a JSON confirming the name of the stack that has been deleted.

> Example Response

```json
{
	"status": "New Stack has been deleted"
}
```

#### /stacks/\<id>/tools  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the names and IDs of all tools related to a single stack.

> Example Response

```json
[
	{
		"tool": {
			"id": 1,
			"name": "Tool 1"
		}
	},
	{
		"tool": {
			"id": 2,
			"name": "Tool 2"
		}
	},
	{
		"tool": {
			"id": 3,
			"name": "Tool 3"
		}
	}
]
```

- HTTP Request Verb: ```POST```
- Required Data: tool.id (int, foreign key, in a nested dictionary)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Provides a JSON containing the names and ID of the tool that has been added to the stack.

> Example Request

```json
{
	"tool": {
		"id": "3"
	}
}
```

> Example Response

```json
{
	"tool": {
		"id": 3,
		"name": "Tool 3"
	}
}
```

#### /stacks/\<id>/tools/\<id>  



- HTTP Request Verb: ```DELETE```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to delete single tools from stacks, and returns a JSON confirming the name of the tool that has been deleted from the relevant stack.

> Example Response

```json
{
	"status": "Tool 3 has been removed"
}
```

### /tools 

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the names, IDs and descriptions of tools within the table as well as their relevant category name and language name.

> Example Response

```json
[
	{
		"category": {
			"name": "Framework"
		},
		"description": "Tool 1",
		"id": 1,
		"language": {
			"name": "Python"
		},
		"name": "Tool 1"
	},
	{
		"category": {
			"name": "Tool"
		},
		"description": "Tool 2",
		"id": 2,
		"language": {
			"name": "Javascript"
		},
		"name": "Tool 2"
	},
	{
		"category": {
			"name": "Software"
		},
		"description": "Tool 3",
		"id": 3,
		"language": {
			"name": "C#"
		},
		"name": "Tool 3"
	}
]
```

- HTTP Request Verb: ```POST```
- Required Data: name (string(50)), description (text), category.id (int, foreign key, in a nested dictionary), language.id (int, foreign key, in a nested dictionary)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to create a new tool in the tools table and returns a JSON with the ID, name and description of the created tool along with the relevant category and language names.

> Example Request

```json
{
	"name": "Created Tool",
	"description": "Created Tool description",
	"category": {
		"id": "1"
	},
	"language": {
		"id": "1"
	}
}
```

> Example Response

```json
{
	"category": {
		"name": "Framework"
	},
	"description": "Created Tool description",
	"id": 4,
	"language": {
		"name": "Python"
	},
	"name": "Created Tool"
}
```

#### /tools/\<id>  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the name, ID and description of a single tool as well as their relevant category name and language name.

> Example Response

```json
{
	"category": {
		"name": "Framework"
	},
	"description": "Tool 1",
	"id": 1,
	"language": {
		"name": "Python"
	},
	"name": "Tool 1"
}
```

- HTTP Request Verb: ```PUT``` ```PATCH```
- Required Data: name (string(50)), description (text), category.id (int, foreign key, in a nested dictionary), language.id (int, foreign key, in a nested dictionary) *missing fields will default to current data*
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to make adjustments to fields from an existing tool and returns a JSON of the updated name, ID and description of the affected stack along with the relevant category and language name.

> Example Request

```json
{
	"name": "Changed Tool Name",
	"description": "Changed tool description",
	"category": {
		"id": "2"
	},
	"language": {
		"id": "2"
	}
}
```

> Example Response

```json
{
	"category": {
		"name": "Tool"
	},
	"description": "Changed tool description",
	"id": 1,
	"language": {
		"name": "Javascript"
	},
	"name": "Changed Tool Name"
}
```

- HTTP Request Verb: ```DELETE```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to delete a single tool, and returns a JSON confirming the name of the tool that has been deleted.

> Example Response

```json
{
	"status": "Created Tool has been deleted"
}
```

#### /tools/\<id>/steps  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the description, step number and learning length in days of the tool steps from a single tool.

> Example Response

```json
[
	{
		"description": "The first step",
		"step_no": 1,
		"time_days": 2
	},
	{
		"description": "The second step",
		"step_no": 2,
		"time_days": 1
	},
	{
		"description": "The second step",
		"step_no": 3,
		"time_days": 3
	}
]
```

- HTTP Request Verb: ```POST```
- Required Data: step_no (int), description (text), time_days (int)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to create a new tool step in the tool steps table and returns a JSON with the containing the description, step number and learning length in days of the created tool step.

> Example Request

```json
{
	"step_no": "10",
	"description": "Created Tool Step",
	"time_days": "5"
}
```

> Example Response

```json
{
	"description": "Created Tool Step",
	"step_no": 10,
	"time_days": 5
}
```

#### /tools/\<id>/steps/\<id>  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the description, step number and learning length in days of a single tool step.

> Example Response

```json
{
	"description": "The first step",
	"step_no": 1,
	"time_days": 2
}
```

- HTTP Request Verb: ```PUT``` ```PATCH```
- Required Data: step_no (int), description (text), time_days (int) *missing fields will default to current data*
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to make adjustments to fields from an existing tool step and returns a JSON of the updated description, step number and learning length in days of the created tool step.

> Example Request

```json
{
	"step_no": "20",
	"description": "adjusted step",
	"time_days": "10"
}
```

> Example Response

```json
{
	"description": "adjusted step",
	"step_no": 20,
	"time_days": 10
}
```

- HTTP Request Verb: ```DELETE```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to delete a single tool step, and returns a JSON confirming the step number of the tool step that has been deleted.

> Example Response

```json
{
	"status": "Tool Step 10 has been deleted"
}
```

### /users  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description: Allows an admin to request a JSON containing the names, IDs, emails and admin status of all users within the table.

> Example Response

```json
[
	{
		"email": "admin@test.com",
		"id": 1,
		"is_admin": true,
		"name": "Admin User"
	},
	{
		"email": "test@test.com",
		"id": 2,
		"is_admin": false,
		"name": "Test User"
	}
]
```

- HTTP Request Verb: ```POST```
- Required Data: email (text), password (text), name (text)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: null
- Description: Allows any user to create a new user in the users table and returns a JSON with the ID, name and email of the created user.

> Example Request

```json
{
	"name":"Created User",
	"email": "user@test.com",
	"password": "password123"
}
```

> Example Response

```json
{
	"email": "user@test.com",
	"id": 3,
	"name": "Created User"
}
```

#### /users/login  

- HTTP Request Verb: ```POST```
- Required Data: email (text), password (text)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: null
- Description: Allows a user to login using their email and password and retrieve a JSON containing a valid JWT token for authentication as well as the users email, ID and name as confirmation.

> Example Request

```json
{
	"email": "test@test.com",
	"password": "password"
}
```

> Example Response

```json
{
	"token": "example JWT token",
	"user": {
		"email": "test@test.com",
		"id": 2,
		"name": "Test User"
	}
}
```

#### /users/\<id>  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required or a valid JWT token from the relevant user.
- Description: Provides a JSON containing the name, ID and email of a single user.

> Example Response

```json
{
	"email": "admin@test.com",
	"id": 1,
	"name": "Admin User"
}
```

- HTTP Request Verb: ```PUT``` ```PATCH```
- Required Data: email (text), password (text), name (text), is_admin (boolean, requires admin privledges to set, requires either a "True" or "False" string) *missing fields will default to current data*
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required or a valid JWT token from the relevant user. Admin rights required to update administrator status.
- Description: Allows a user to update their details, and if they have administrator privledges, can adjust the is_admin property of users. Returns a JSON of the updated status including email, ID, and name. If the is_admin property was adjusted, will include it in the returned JSON.

> Example Request (non-admin)

```json
{
	"name":"changed user",
	"email": "test12345@test.com",
	"password": "changedpassword"
}
```

> Example Response (non-admin)

```json
{
	"email": "test12345@test.com",
	"id": 3,
	"name": "changed user"
}
```

> Example Request (admin)

```json
{
	"name":"changed user",
	"email": "test12345@test.com",
	"password": "changedpassword",
	"is_admin": "true"
}
```

> Example Response (admin)

```json
{
	"email": "test12345@test.com",
	"id": 3,
	"is_admin": true,
	"name": "changed user"
}
```

- HTTP Request Verb: ```DELETE```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required or a valid JWT token from the relevant user.
- Description: Allows an admin to delete a user from the users table or the relevant user to delete their user from the users table, and returns a JSON confirming the name of the user that has been deleted.

> Example Response

```json
{
	"status": "changed user has been deleted"
}
```

#### /users/\<id>/tools  

- HTTP Request Verb: ```GET```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required or a valid JWT token from the relevant user.
- Description: Provides a JSON containing the name and ID of all tools related to a single user.

> Example Response

```json
[
	{
		"tool": {
			"id": 1,
			"name": "Tool 1"
		}
	},
	{
		"tool": {
			"id": 2,
			"name": "Tool 2"
		}
	},
	{
		"tool": {
			"id": 3,
			"name": "Tool 3"
		}
	}
]
```

- HTTP Request Verb: ```POST```
- Required Data: tool.id (int, foreign key, in a nested dictionary)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required or a valid JWT token from the relevant user.
- Description: Allows an admin to add a tool to a users account or the relevant user to add a tool to their own account, returns a JSON with the added tool's ID and name.

> Example Request

```json
{
	"tool": {
		"id": 3
	}
}
```

> Example Response

```json
{
	"tool": {
		"id": 3,
		"name": "Tool 3"
	}
}
```

#### /users/\<id>/tools/\<id>

- HTTP Request Verb: ```DELETE```
- Required Data: null
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required or a valid JWT token from the relevant user.
- Description: Allows an admin to remove a tool from a user or the relevant user to remove a tool from their user, and returns a JSON confirming the name of the tool that has been removed.

> Example Response

```json
{
	"status": "Tool 1 has been removed"
}
```

## ERD

![ERD_Diagram](./docs/ERD.png)

## Third Party Services



## Model Relationships

#### Summation

There are three main tables that act as the backbone to this API, that is: Tool, Stack and User. Each of the other resources are designed to contribute to these three combined with two join tables that act as a link between these major tables.

#### Tool Model

The tool model contains it's own information in the form of an ID for a primary key, a name and a description. This table also contains two foreign keys attached to the tables 'Categories' and 'Languages'. These foreign keys are used so that each tool can be defined in conjunction with categories and languages, which both can be related to multiple records within the tools table. So each of these follow a one to many relationship from the tools to the categories and languages. Outside of this, the tools table is used as a foreign key / conjoined primary key in the tool_steps table as one tool can have multiple steps forming a one to many relationship from tools to tool_steps. Lastly, the tools table is attached to two join tables, both user_tools and stack_tools, to provide the functionality of a many to many relationship between the three major tables through a one to many relationship to the join table from both ends. As with the tool_steps table, each of the join tables uses the tools ID within their primary key, allowing for efficient routing for correct information.

```python
class Tool(db.Model):
    __tablename__ = "tools"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text, nullable=False)
    
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id"), nullable=False
        )
    category = db.relationship("Category", back_populates="tools")
    
    language_id = db.Column(
        db.Integer, db.ForeignKey("languages.id"), nullable=False
        )
    language = db.relationship("Language", back_populates="tools")
    
    tool_steps = db.relationship("Tool_Step", back_populates="tool")
    stack_tools = db.relationship("Stack_Tool", back_populates="tool")
    user_tools = db.relationship("User_Tool", back_populates="tool")

```

#### Category Model

The categories table is very straight forward, it contains an ID for a primary key, and a name and description. There are no foreign keys contained within the categories table, however as mentioned above, the tools table makes use of the category ID as a foreign key link between the two tables in a one to many relationship.

```python
class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    tools = db.relationship("Tool", back_populates="category")
```

#### Language Model

As with the categories table, the languages table is very straight forward, it contains an ID for a primary key and a name. There are no foreign keys contained within the languages table, however as mentioned above, the tools table makes use of the language ID as a foreign key link between the two tables in a one to many relationship.

```python
class Language(db.Model):
    __tablename__ = "languages"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    tools = db.relationship("Tool", back_populates="language")
```

#### Tool_Step Model

The tool step table is the first of the tables discussed to contain a joined primary key. As the tool_steps entries acts as a sub-resource for the tools, this joined primary key makes evident this relationship. The primary key consists of two fields, the step_no which is a straight integer field, and the tool_id which is a foreign key from the tools table in a many to one relationship from tool_steps to tools. Lastly, it also contains two other fields in the description and time_days to account for other required information.

```python
class Tool_Step(db.Model):
    __tablename__ = "tool_steps"
    
    step_no = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    time_days = db.Column(db.Integer, nullable=False)
    
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False)
    tool = db.relationship("Tool", back_populates="tool_steps")
    
    __table_args__ = (
        db.PrimaryKeyConstraint(
            tool_id, step_no,
        ),
    )
```

#### User Model

The second of the major tables, the users table allows information about the tools to be associated with a given user. The table itself contains the ID as a primary key, and also an email field, a password, a name and is_admin to form the administrator privledges status. No foreign keys are contained within this table, however this table forms a one to many relationship with the user_tools joint able to link users to tools. This user table has it's primary key joined from the user_id and the tool_id and the routing logically uses the user_tools as a subresource for users through the 'user/user id/tools' end points.

```python
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, default="Anonymous")
    is_admin = db.Column(db.Boolean, default=False)
    
    user_tools = db.relationship("User_Tool", back_populates="user")
```

#### User_Tool Model

As discussed above, the user_tool model is a join table to allow a relationship between the users and tools tables. Both of it's fields are foreign keys taken from the ID of each of these major tables, and these form the primary key to emphasise the relationship between the users and the tools. This table forms a many to one relationship to both the users and the tools tables.

```python
class User_Tool(db.Model):
    __tablename__ = "user_tools"
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="user_tools")
    
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False)
    tool = db.relationship("Tool", back_populates="user_tools")
    
    __table_args__ = (
        db.PrimaryKeyConstraint(
            user_id, tool_id,
        ),
    )
```

#### Stack Model

The last of the major tables with a smaller amount of information. It contains an ID for the primary key, a name and a description. There are no foreign keys directly in the table however it forms a one to many relationship to the stack_tools table similar to the relationship between users and user_tools. The stack_tools is also treated as a subresource of stacks so that the tools associated to a stack can be easily obtained through the 'stacks/stack id/tools' end points.

```python
class Stack(db.Model):
    __tablename__ = "stacks"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text, nullable=False)
    
    stack_tools = db.relationship("Stack_Tool", back_populates="stack")
```

#### Stack_Tool Model

Lastly, the stack_tool model is a join table to allow a relationship between the stacks and tools tables. Both of it's fields are foreign keys taken from the ID of each of these major tables, and these form the primary key to emphasise the relationship between the stacks and the tools. This table forms a many to one relationship to both the stacks and the tools tables.

```python
class Stack_Tool(db.Model):
    __tablename__ = "stack_tools"
    
    stack_id = db.Column(db.Integer, db.ForeignKey("stacks.id"), nullable=False)
    stack = db.relationship("Stack", back_populates="stack_tools")
    
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False)
    tool = db.relationship("Tool", back_populates="stack_tools")
    
    __table_args__ = (
        db.PrimaryKeyConstraint(
            stack_id, tool_id,
        ),
    )
```

## Database Relations



## Project Management

