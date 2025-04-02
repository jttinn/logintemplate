# 3-ConfigurationSetup

## File Name: mrclean\docs\3-ConfigurationSetup1.md
## Version: 2.6
## Last Updated: 19-Feb-2025
## Description: The document describes how the framework described in 2-ApplicationArchitecture will be Configured and set up.

### SECTION A: OVERVIEW
This document describes the configuration and setup instructions for the application development framework utilized for the mrclean development effort. It is documented in this manner so that the AI and developer will always have reference to the components being utilized. By doing this, all feature requirements and development work will only proceed utilizing the software applications, application development tools and custom configurations described in 2-ApplicationArchitecture.md and this document, 3-ConfigurationSetup.md

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
    C:\PythonScripts\mrclean
    ```

##### 2.2 Project Folder Structure

```sh
mrclean/
├── .env
├── .vscode
    ├── launch.json
    ├── settings.json
    ├── mrclean.code-workspace
├── app/ 
    ├── __init__.py
    ├── main.py
├── config.py 
├── requirements.txt 
├── models/
    ├── __init__.py
    ├── user_model.py
    ├── profile_model.py
    ├── csv_uploads.py
    ├── csvconfig.py
    ├── stock_lt.py
├── csv_processors/
    ├── __init__.py
    ├── utils.py
    ├── mrclean_processor.py
├── routes/
    ├── __init__.py
    ├── auth_routes.py
    ├── profile_routes.py
    ├── process_csv_routes.py
    ├── upload_csv_routes.py
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
    ├── process_csv.html
    ├── upload_csv.html
├── database.sql
├── tests/
├── docs/
    ├── README.md
    ├── 1.ProjectOverview.md
    ├── 2.ApplicationArchitecture
    ├── 3.ConfigurationSetup1.md
    ├── 3.ConfigurationSetup2.md
    ├── 4.EnvironmentValidation.md
    ├── api-docs.md
    ├── troubleshooting.md
```

Where:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| NAME                                  | TYPE      | DESCRIPTION                                                                                                       |
| ------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------- |
| .vscode/                              | Directory | Contains Visual Studio Code workspace settings and files                                                          |
| .vscode/launch.json                   | JSON      | Launch configuration for the mrclean project                                                                    |
| .vscode/settings.json                 | JSON      | Workspace-specific settings for the mrclean project.                                                            |
| .vscode/mrclean.code-workspace      | JSON      | Workspace-specific settings for the mrclean project.                                                            |
| app                                   | Directory | Contains all the python application files                                                                         |
| app/__init__.py                       | Python    | Initialize the Flask application and configure it.                                                                |
| app/main.py                           | Python    | Entry point for running the Flask application.                                                                    |
| models                                | Directory | Contains Python files defining the database schema and any associated logic using SQLAlchemy                      |
| models/__init__.py                    | Python    | Initializes the models module and database connection                                                             |
| models/csv_uploads.py                 | Python    | Model for the CSVUploads table stored in mySQL. This table stores the log for each CSV file uploaded by the user. |
| models/csvconfig.py                   | Python    | Model for the csvconfig table. This configuration table provides guidance on how to process each csv_type.        |
| models/stock_lt.py                    | Python    | Model for the stock_lt table. This is the landing table for all csv uploads                                       |
| models/user_model.py                  | Python    | Defines the User table and associated relationships                                                               |
| models/profile_model.py               | Python    | Defines the Profile table and related logic                                                                       |
| csv_processors/                       | Directory | Contains the python scripts to perform specific cleaning & validation of data specific to the csv_type            |
| csv_processors/__init__.py            | Python    | Initializes the common libraries needed for data cleaning and validation                                          |
| csv_processors/utils.py               | Python    | Contains the common utility scripts needed for data cleaning & validation for all csv_types                       |
| csv_processors/mrclean_processor.py | Python    | Used to initiate cleaning & validation specific to csv_type = "mrclean"                                         |
| routes                                | Directory | Contains Python files defining Flask routes                                                                       |
| routes/__init__.py                    | Python    | Initializes the routes module                                                                                     |
| routes/auth_routes.py                 | Python    | Routes for user login, registration, and password recovery                                                        |
| routes/profile_routes.py              | Python    | Routes for user profile management                                                                                |
| routes/process_csv_routes.py          | Python    | Initial Route for processing CSV data. Processing continues using the csv_processor according to the csv_type     |
| routes/upload_csv_routes.py           | Python    | Route for uploading all types of CSV files and inserting data into the generic stock_lt landing table.            |
| services/                             | Directory | Provides a centralized location for business logic and shared utilities                                           |
| services/auth_service.py              | Python    | Contains user authentication-related logic                                                                        |
| services/email_service.py             | Python    | Contains logic for sending emails                                                                                 |
| services/user_service.py              | Python    | For user management operations                                                                                    |
| services/utils.py                     | Python    | For shared helper service functions                                                                               |
| static/                               | Directory | Contains code or text files to support the application either with styling (style.css) or reference               |
| static/css                            | Directory | Location to store the css styling sheets                                                                          |
| static/css/style.css                  | CSS       | Main styling sheet for the web pages                                                                              |
| static/images/                        | Directory | Location to store images or icons for use on the application's web pages                                          |
| static/js                             | Directory | Location to store any supporting javascript for the applications                                                  |
| templates                             | Directory | Contains the html files to support the web page applications                                                      |
| templates/index.html                  | HTML      | Landing webpage for the application                                                                               |
| templates/home.html                   | HTML      | Main page to navigate from once the user has logged in                                                            |
| templates/layout.html                 | HTML      | Provides the framework for the web application consisting of a header, a collapsable left panel and body          |
| templates/process_csv.html            | HTML      | The page used by the user to process their uploaded csv files                                                     |
| templates/upload_csv.html             | HTML      | The page used by the user to initiate uploade of their csv files into the mySQL database and stock_lt table       |
| tests/                                | Directory | Location for scripts that support testing of the application and its environment                                  |
| uploads/                              | Directory | Location where csv files are saved before being uploaded into the mySQL database. Only .csv files will be here    |
| venv/                                 | Directory | Contains the configuration files to support the virtual environment                                               |
| docs/                                 | Directory | Contains documentation related to the project                                                                     |                   
| .env                                  | File      | Environmental variables to support the application                                                                |
| .gitignore                            | GIT       | GIT Ignore file for the mrclean project to exclude unnecessary files from version control.                      |
| config.py                             | Python    | Contains the primary constants and configuration information for the application                                  |
| database.sql                          | Python    | Contains the SQL code for the initial build of database objects and the initial load of reference data            |
| db.py                                 | Python    | An application startup script to initialize the database                                                          |
| requirements.txt                      | File      | Contains the python library of modules that need to be loaded to support the application                          |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

