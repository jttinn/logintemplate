# 3-ConfigurationSetup

## File Name: logintemplate\docs\3-ConfigurationSetup1.md
## Version: 2.5
## Last Updated: 16-Feb-2024
## Description: The document describes how the framework described in 2-ApplicationArchitecture will be Configured and set up.

### SECTION A: OVERVIEW
This document describes the configuration and setup instructions for the application development framework utilized for the logintemplate development effort. It is documented in this manner so that the AI and developer will always have reference to the components being utilized. By doing this, all feature requirements and development work will only proceed utilizing the software applications, application development tools and custom configurations described in 2-ApplicationArchitecture.md and this document, 3-ConfigurationSetup.md

This document only discusses the configuration and setup instructions specific to the application with exception to the following:
- The installation and standard software configuration instructions for any of the applications utilized for the software development will not be included here. The developer should follow the installation instructions provided by the software provider.
- As this is a proof of concept for an application template, it is only meant to cover the development of the framework and not the completed application.

### SECTION B: APPLICATION DEVELOPMENT ENVIRONMENT CONFIGURATION AND SETUP

#### 1.0 Virtual Environment

- All development work will be done under a virtual environment.
- Once activated, the development will utilize the requirements.txt to ensure all the python modules are loaded and updated specifically for the application.

```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

- For module updates, guidance on updating `requirements.txt` will be provided for adding or removing modules during development.
- When completing work in the virtual environment, deactivate it by running the `deactivate` command:
- After adding/removing modules, the command `pip freeze > requirements.txt` will be used to update the `requirements.txt` file.

#### 2.0 Custom Configurations

##### 2.1 Local Project Folder Structure

- The following directory structure will be used for this project:
    - Location:
    
    ```sh
    C:\PythonScripts\logintemplate
    ```

##### 2.2 Project Folder Structure

```sh
logintemplate/
├── .env
├── .vscode
    ├── launch.json
    ├── settings.json
    ├── logintemplate.code-workspace
├── app/ 
    ├── main.py
├── config.py 
├── README.md
├── requirements.txt 
├── models/
    ├── __init__.py
    ├── user_model.py
    ├── profile_model.py
├── routes/
    ├── __init__.py
    ├── auth_routes.py
    ├── profile_routes.py
├── services/
    ├── auth_service.py
    ├── email_service.py
    ├── user_service.py
    ├── utils.py
├── static/
    ├── css
        └── style.css 
    ├── images
    ├── js
├── templates/ 
    ├── index.html 
    ├── login.html 
├── database.sql
├── tests/
├── docs/
    ├── READMEAI.md
    ├── setup-guide.md
    ├── api-docs.md
    ├── troubleshooting.md
```

Where:

| NAME               | TYPE      | DESCRIPTION                                                                                           |
| ------------------ | --------- | ----------------------------------------------------------------------------------------------------- |
| .env               | File      | Environmental variables to support the application                                                    |
| .vscode            | Directory | Contains Visual Studio Code workspace settings and files                                              |
| api-docs.md        | File      | Contains the specifications for any API end-points developed for the application                      |
| app                | Directory | Contains all the python application files                                                             |
| auth_routes.py     | File      | Routes for user login, registration, and password recovery                                            |
| auth_service.py    | File      | Contains user authentication-related logic                                                            |
| config.py          | File      | Contains the constants and configuration information for the application                              |
| database.sql       | File      | Contains the SQL code for the initial build of database objects and the initial load of reference data |
| db.py              | File      | An application startup script to initialize the database                                              |
| docs               | Directory | Contains documentation related to the project                                                         |
| email_service.py   | File      | Contains logic for sending emails                                                                     |
| models             | Directory | Contains Python files defining the database schema and any associated logic using SQLAlchemy          |
| models/__init__.py | File      | Initializes the models module and database connection                                                 |
| profile_model.py   | File      | Defines the Profile table and related logic                                                           |
| profile_routes.py  | File      | Routes for user profile management                                                                    |
| README.md          | File      | The main project document containing information on the application and reference to other relevant   |
| READMEAI.md        | File      | Represents the documentation that has been refined with language that an AI may find easier to consume |
| requirements.txt   | File      | Contains the python library of modules that need to be loaded to support the application               |
| routes             | Directory | Contains Python files defining Flask routes                                                           |
| routes/__init__.py | File      | Initializes the routes module                                                                          |
| services           | Directory | Provides a centralized location for business logic and shared utilities                               |
| setup-guide.md     | File      | Contains the instructions on which development tools to install and specific configurations needed.    |
| static             | Directory | Contains code or text files to support the application either with styling (style.css) or reference    |
| static/css         | Directory | Location to store the css styling sheets                                                               |
| static/images      | Directory | Location to store images or icons for use on the web pages                                            |
| static/js          | Directory | Location to store any supporting javascript for the applications                                       |
| style.css          | File      | Main styling sheet for the application.                                                               |
| templates          | Directory | Contains the html files to support the web page applications                                          |
| tests              | Directory | Location for scripts that support testing of the application and its environment                       |
| troubleshooting.md | File      | Provides and FAQ list of issues that might come up and how to resolve them                             |
| user_model.py      | File      | Defines the User table and associated relationships                                                   |
| user_service.py    | File      | For user management operations                                                                         |
| utils.py           | File      | For shared helper functions                                                                            |

