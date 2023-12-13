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

```
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

```
{
	"name":"Created Category",
	"description":"Created Category Description"
}
```

> Example Response

```
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

```
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

```
{
	"name":"Category Changed",
	"description":"Changed Description"
}
```

> Example Response

```
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

```
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

```
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

```
{
	"name":"Test Language"
}
```

> Example Response

```
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

```
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

```
{
	"name":"language Changed"
}
```

> Example Response

```
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

```
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

```
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

```
{
	"name":"New Stack",
	"description": "New Stack descriptions"
}
```

> Example Response

```
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

```
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

```
{
	"name":"Changed Stack",
	"description": "Changed Stack description"
}
```

> Example Response

```
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

```
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

```
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

```
{
	"tool": {
		"id": "3"
	}
}
```

> Example Response

```
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

```
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

```
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
- Required Data: name (string(50)), description (text), category_id (int, foreign key), language_id (int, foreign key)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description:

> Example Request

```

```

> Example Response

```

```

#### /tools/\<id>  

- HTTP Request Verb: ```GET```
- Required Data:
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the name, ID and description of a single tool as well as their relevant category name and language name.

> Example Response

```
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
- Description:

> Example Request

```
{
	"name":"Changed tool",
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

```

```

- HTTP Request Verb: ```DELETE```
- Required Data:
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description:

> Example Response

```

```

#### /tools/\<id>/steps  

- HTTP Request Verb: ```GET```
- Required Data:
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the description, step number and learning length in days of the tool steps from a single tool.

> Example Response

```
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
- Required Data: step_no (int), description (text), time_days (int), tool_id (int, foreign key)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description:

> Example Request

```

```

> Example Response

```

```

#### /tools/\<id>/steps/\<id>  

- HTTP Request Verb: ```GET```
- Required Data:
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the description, step number and learning length in days of a single tool step.

> Example Response

```
{
	"description": "The first step",
	"step_no": 1,
	"time_days": 2
}
```

- HTTP Request Verb: ```PUT``` ```PATCH```
- Required Data: *missing fields will default to current data*
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description:

> Example Request

```

```

> Example Response

```

```

- HTTP Request Verb: ```DELETE```
- Required Data:
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required.
- Description:

> Example Response

```

```

### /users  

- HTTP Request Verb: ```GET```
- Required Data:
- Expected Response: A '200 OK' response with a JSON.
- Authentication: null
- Description: Provides a JSON containing the names, IDs, emails and admin status of all users within the table.

> Example Response

```
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
	},
	{
		"email": "test12345@test.com",
		"id": 3,
		"is_admin": true,
		"name": "changed user"
	}
]
```

- HTTP Request Verb: ```POST```
- Required Data: email (text), password (text), name (text), is_admin (boolean, either "True" or "False", requires admin privledges)
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: null
- Description:

> Example Request

```

```

> Example Response

```

```

#### /users/login  

- HTTP Request Verb: ```POST```
- Required Data:
- Expected Response: A '201 CREATED' response with a JSON.
- Authentication: null
- Description:

> Example Request

```

```

> Example Response

```

```

#### /users/\<id>  

- HTTP Request Verb: ```GET```
- Required Data:
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required or a valid JWT token from the relevant user.
- Description: Provides a JSON containing the name, ID and email of a single user.

> Example Response

```
{
	"email": "admin@test.com",
	"id": 1,
	"name": "Admin User"
}
```

- HTTP Request Verb: ```PUT``` ```PATCH```
- Required Data: *missing fields will default to current data*
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required or a valid JWT token from the relevant user. Admin rights required to update administrator status.
- Description:

> Example Request

```

```

> Example Response

```

```

- HTTP Request Verb: ```DELETE```
- Required Data:
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required or a valid JWT token from the relevant user.
- Description:

> Example Response

```

```

#### /users/\<id>/tools  

- HTTP Request Verb: ```GET```
- Required Data:
- Expected Response: A '200 OK' response with a JSON.
- Authentication: Valid JWT Token from an administrator user required or a valid JWT token from the relevant user.
- Description: Provides a JSON containing the name and ID of all tools related to a single user.

> Example Response

```
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

## ERD

![ERD_Diagram](./docs/ERD.png)

## Third Party Services



## Model Relationships



## Database Relations



## Project Management

