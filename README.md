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

### /

- HTTP Request Verb: GET
- Required Data: N/A
- Expected Response: A '200 OK' response with a json of API end points.
- Authentication: N/A
- Description: Provides an index of all the end points available with this API.

**Example**



### /categories

- HTTP Request Verb: GET
- Required Data: N/A
- Expected Response: A '200 OK' response with a json of category names and IDs.
- Authentication: JWT Bearer Token Required
- Description: Provides a JSON containing the names and IDs of all categories within the table.

**Example**



- HTTP Request Verb: POST
- Required Data: name (char(50), required), description (text)
- Expected Response: A '201 CREATED' response with a json of the category name and description.
- Authentication: JWT Bearer Token Required, User with Admin Privledges required.
- Description: Allows an admin to create a new category in the categories table.

**Example**



#### /categories/\<id>  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: PUT/PATCH
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: DELETE
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



### /tools  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: POST
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /tools/\<id>  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: PUT/PATCH
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: DELETE
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /tools/\<id>/steps  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: POST
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /tools/\<id>/steps/\<id>  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: PUT/PATCH
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: DELETE
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



### /languages  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: POST
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /languages/\<id>  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: PUT/PATCH
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: DELETE
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



### /stacks  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: POST
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /stacks/\<id>  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: PUT/PATCH
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: DELETE
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /stacks/\<id>/tools  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /stacks/\<id>/languages  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



### /users  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: POST
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /users/register  

- HTTP Request Verb: POST
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /users/login  

- HTTP Request Verb: POST
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /users/\<id>  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: PUT/PATCH
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: DELETE
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /users/\<id>/tools  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /users/\<id>/plans  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /users/\<id>/plans/generate  

- HTTP Request Verb: POST
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



#### /users/\<id>/plans/\<id>  

- HTTP Request Verb: GET
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



- HTTP Request Verb: DELETE
- Required Data:
- Expected Response:
- Authentication:
- Description:

**Example**



## ERD

![ERD_Diagram](./docs/ERD.png)

## Third Party Services



## Model Relationships



## Database Relations



## Project Management

