Here is the current status of our development exercise for logintemplate project.  The document below is our agreement on: 
- the goals of the project
- the rules by which the AI and I will proceed through the design and development work
- the specifications of the tool set we will use and their configuration

Following the document are questions that need to be answered by the AI to confirm that the document is understood and we will proceed under the guidance of this document.    


Here is the document: 

----
#### Document Name and Version Information
**Document Title:** Login Template Specifications  
**Version:** 2.4  
**Version Date:** 4-Dec-2024
**Version History:**

| Version | Date        | Change                                                                                                                                        |
| ------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0     | 25-Nov-2024 | Combined Section 1 & Section 2 into 1 document, version controlled once. Added .vscode directory to the standard directory structure in 2.6.1 |
| 2.1     | 25-Nov-2024 | README.md synced with github at the project root. All other documentation will be added under docs/                                           |
| 2.2     | 26-Nov-2024 | In section 1.3, Rule 8 was changed to add the project directory name when referencing the name of the file and how to update versioning       |
| 2.3     | 27-Nov-2024 | Updated rule 5 in section 1.3 to provide guidance on how to make changes impacting design of this application. Added 2 new python modules to  |
|         |             | section 2.3.7, formatted the table in 2.6.1 to be more readable                                                                               |
| 2.4     | 04-Dec-2024 | Section 2.6.1 Added additional directory structure under static and sorted the table of files and directories for easy lookup                 |

----

### **SECTION 1: Project Overview**

#### **1.1 Goals**

1. **Framework for Application Development**:  
    The purpose of this template is to create a reusable framework that serves as the foundation for developing other applications. The framework must be designed for easy replication and must enable developers to build new applications efficiently by offering foundational functionalities.
    
2. **Portability and Deployment**:  
    The template must be portable across environments and simple to deploy, enabling straightforward setup for developers.
    
3. **Support for Modular Extensions**:  
    The framework must provide a structured approach to integrating additional modules by offering:
    
    - A pre-configured database connection.
    - A robust user registration and login system.
    - A central location for managing global application settings and configurations.
    - Documentation tailored to AI for enabling rapid feature development, including instructions for environment setup and foundational code generation.
4. **User Management Features**:  
    The template must include user-related functionalities:
    
    - User registration.
    - User login.
    - Password recovery.
    - A profile screen for user management.
5. **Proof-of-Concept Design Philosophy**:  
    The framework is for proof-of-concept purposes and should remain simple. However, simplicity should not compromise foundational quality. The framework must incorporate structural components that encourage modularity, scalability, and extensibility to support future applications.
    

---

#### **1.2 Project Assumptions**

1. **Environment Scope**:  
    The template is limited to proof-of-concept development and does not require support for environments such as test, UAT, or production.
    
2. **Configuration Management**:
    
    - Application settings and constants must not be hardcoded or embedded within application logic.
    - These values should be securely stored using a `.env` file. Examples include:
        - Database credentials (username, password, connection string).
        - API keys.
        - Debug mode toggle.
        - Constants such as numeric defaults or strings.  

3. **Security**:  
    While enhanced security measures are unnecessary for a proof-of-concept, the following exceptions must be implemented:
    
    - Passwords must be hashed and salted (further details will be defined in functional requirements).
    - Sensitive information in `.env` must be secured.
      
4. **Fallback Behaviors**:  
    Any fallback mechanisms necessary for application stability and usability will be defined during the feature specification phase.
    

---

#### **1.3 AI Expectations**

By following the goals, tools, and configurations outlined in this document, the AI is expected to adhere to the following rules:

1. **Rule 1: Goals as a Guideline**  
    The goals provide an understanding of the purpose of the final product. The AI may refine or rewrite the goals in a way that improves clarity for itself, but deviations from the goals are not permitted. If a deviation becomes necessary during feature development, the AI must notify the user. Work will pause, goals will be redefined, and completed work will be reviewed and updated before continuing.
    
2. **Rule 2: Consistency in Tools and Configurations**  
    Tools and configurations define the development framework. During development, the AI must assume these specifications are complete. If additional tools or changes to configurations are required, the AI must notify the user, stop feature development, and update the specifications before proceeding.
    
3. **Rule 3: Simplicity Over Complexity**  
    In line with GOAL 5, the AI must balance simplicity with the need for foundational quality. For proof-of-concept purposes, overengineering and excessive security measures are unnecessary, as the data in this template is not confidential or sensitive.
    
4. **Rule 4: Consensus Before Development**  
    The AI must ensure clarity on the goals, tools, and configurations before starting feature discussions or coding. No progress should be made until the user confirms these elements are finalized.
    
5. **Rule 5: Best-in-Class Recommendations**  
    The AI may suggest alternative methods, tools, or frameworks that align with the goals and offer advantages. However, any proposed changes to specifications or implementations require: 
    - development work needs to stop 
    - the AI must provide a review of the changes to documentation and work already performed to the developer
    - the AI and developer must determine whether the changes are necessary and improve the outcome of our GOALS and come to a concensus. (approval)
    - implement the changes required
    
6. **Rule 6: Beginner-Friendly Guidance**  
    The user is a beginner in Python, GitHub, and JavaScript. The AI must provide clear explanations, benefits, and examples to guide feature design and implementation while adhering to best practices.
    
7. **Rule 7: Documentation Requirements**  
    At the end of the project, the AI must generate:
    
    - A README file with step-by-step instructions for developers to install, configure, and adapt the template.
    - A READMEAI file with detailed instructions for AI systems to recreate the codebase, including placeholders for adding new features.
    
8. **Rule 8: File Versioning Standards**  
    The AI must include a header in every file containing:
    
    - the project directory and File name.  
    - Version number (format: 1.0, 1.1, etc.).
    - Last update date.
    - A brief description.  
        Example:
    
```
# File Name: app\main.py   
# Version: 1.0   
# Last Updated: 19-Nov-2025  
# Description: Entry point for the Login Template application.`  
```
    - when creating a new file, the AI will assign version 1.0 as the initial version and use the current date for the date displayed next to Last Updated 
    - when the AI is making a change and presenting a new version of an existing file, the AI will auto-increment the version number and use the current date for the date displayed next to Last Updated 
    
9. **Rule 9: Partial Code Updates**  
    When providing partial code for an existing file, the AI must include:
    
    - Clear instructions on where to insert or update the code.
    - Any necessary changes to the file header for versioning.
    
10. **Rule 10: Commenting Standards**  
    The AI must annotate key blocks of code with concise and clear comments. Comments should be placed above the relevant code, avoiding inline comments unless absolutely necessary. Multi-line comments are acceptable for documenting complex logic.
    

---

### **Additional Notes**

- The template is named `logintemplate`. All references to this project should use this name or its acronym, `LT`.
- As feature definitions progress, additional documentation and configuration formats (e.g., README file structures) will be addressed in subsequent sections.

## SECTION 2: Application Architecture


#### 2.1 Overview

- this simplified architecture utilizes a client-server configuration with a webpage front end on the client side and a windows based server running python and utilizing mySQL database on the server side.
- as this is a template for other applications to build on, this application will simply provide a basic framework that is fully functional with these main features:
    - complete instruction on configuring a working environment, composed of many applications and modules, and making them as simple as possible.
    - a webpage front end designed utilizing a fixed styling and layout composed of a panel for menu options on the right, a banner with title and user profile access and a body where the user applications will run.
- the template will already build in user registration and login features with the expectation that this feature will be a common requirement for all applications built utilizing this framework
- this design is not intended for production or migration to other databases or cloud platforms, however, if design decisions can be made that will help minimize possible rework of the solution and do not overcomplicate this proof-of-concept then this would be preferred.
- a troubleshooting guide will be provided following the release of the Proof-of-Concept and will not be the focus of this section.

#### 2.2 Software Requirements - Client

- Applications running on the Client side will utilize the following products and coding languages:
    
    - Internet Browser:
        - latest stable version of Google Chrome (Side note: My current version is: Windows 11 Version 130.0.6723.117 (Official Build) (64-bit))
        - latest stable version of Microsoft Edge (Side Note: My current version is: 130.0.2849.80 (Official build) (64-bit))
        - NOTE: this Proof-of-Concept configuration has only been optimized for Chrome v130+ and Edge v130+ .
        - This proof-of-concept will not undertake browser testing for compatibility. Compatibility with other versions or other browsers is not guaranteed.
    - Web Pages:
        - HTML for rendering web pages
        - Use **Vanilla JavaScript** for dynamic actions and form validations.
        - AJAX and Fetch API will handle dynamic client-server interactions, ensuring compatibility with modern practices.
        - style.css will managing the styling for the web pages and be created manually and served from the web server o/s
- Access to the proof-of-concept application will be through localhost using:
    
    ```
    http://127.0.0.1:5000/index.html
    ```
    

#### 2.3 Software Requirements - Server

- Applications and coding languages utilized for the server side application development, maintenance and user implementation are as follows:

##### 2.3.1 O/S:

- Windows 11 Home Version

##### 2.3.2 Webserver:

- FLASK

##### 2.3.3 IDE:

- Visual Studio Code
- Visual Studio Code will also be used for access to terminal command line options. For that reason, the integrated terminal (Ctrl+) must be enabled

##### 2.3.4 Database

- mySQL Community Server - GPL, Win64, version 8.0.39 or higher
- MySQL Workbench, version 8.0.38 build 4270059 CE (win64)
- the developer must have their own user account and will be granted full admin access to the database in order to create schemas and objects as required
- The name of the database for this application will be called 'ods' which stands for operational data store. 

##### 2.3.5 Version Control:

- Github
    
- the repository will be configured at:
    
    ```
    `jttinn/logintemplate`  
    ```
    
- access to the github repository from visual studio will be configured to make it easy for code access and version control
    

##### 2.3.6 Server-side development languages

- Python 3.12 or later
- SQL for creation and maintenance of database structures
- mySQL procedural SQL for database operations to be called as needed from the application or via database trigger events

##### 2.3.7 Python Modules

The following Python modules are required for the server-side application development:

- Flask: The lightweight web server framework for the application.
- mysql-connector-python: MySQL Connector for Python to enable database connectivity.
- SQLAlchemy: Object Relational Mapping (ORM) to manage database models.
- Werkzeug: Required for password hashing and general security utilities.
- python-dotenv: To manage environment variables securely.
- MarkupSafe: A Flask dependency, included explicitly to avoid version conflicts.
- Flask-SQLAlchemy: Extension for SQLAlchemy support in Flask applications.
- Flask-Longin: For user session management

##### 2.3.8 ORM (Object-Relational Mapping) tool

- sqlalchemy

#### 2.4 Software Installation and Configuration

- the software installation instructions and standard configuration will be provided in documentation generated after design and development have completed
- installation steps of each of the applications will not be required unless there are specific steps unique to environment we are setting up

#### 2.5 Virtual Environment

- all development work will be done under a virtual environment.
- once activated, the development will utilize the requirements.txt to ensure all the python modules are loaded and updated specifically for the application.

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

- for module updates, guidance on updating `requirements.txt` will be provided for adding or removing modules during development.
- When completing work in the virtual environment, deactivate it by running the `deactivate` command:
- after adding/removing modules, the command `pip freeze > requirements.txt` will be used to update the `requirements.txt` file.

#### 2.6 Custom Configurations

##### 2.6.1 Local Project folder Structure

- The following directory structure will be used for this project:  
    - Location:
    
    ```
    	C:\PythonScripts\logintemplate
    ```
    
    **Project Folder Structure**
    
    ```
    logintemplate/
    ├── .env
    ├── .vscode
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
    |──  database.sql
    |── tests/
    |── docs/
    	├── READMEAI.md
    	├── setup-guide.md
    	├── api-docs.md
    	├── troubleshooting.md
    ```
    
    Where:
    
--------------------------------------------------------------------------------------------------------------------------------------------
| NAME               |  TYPE     | DESCRIPTION                                                                                             |
| ------------------ | --------- | ------------------------------------------------------------------------------------------------------- |
| .env               | File      | Environmental variables to support the application                                                      |
| .vscode            | Directory | Contains Visual Studio Code workspace settings and files                                                |
| api-docs.md        | File      | contains the specifications for any API end-points developed for the application                        |
| app                | Directory | Contains all the python application files                                                               |
| auth_routes.py     | File      | Routes for user login, registration, and password recovery                                              |
| auth_service.py    | File      | Contains user authentication-related logic                                                              |
| config.py          | File      | Contains the constants and configuration information for the application                                |
| database.sql       | File      | Contains the SQL code for the initial build of database objects and the initial load of reference data  |
|                    |           | that is required before the application is run for the first time                                       |
| email_service.py   | File      | Contains logic for sending emails                                                                       |
| models             | Directory | Contains Python files defining the database schema and any associated logic using **SQLAlchemy** (the   |
|                    |           | chosen ORM tool). Each file will represent one or more related database tables as SQLAlchemy classes    |
|                    |           | (models)                                                                                                |
| models/__init__.py | File      | Initializes the models module and database connection                                                   |
| profile_model.py   | File      | Defines the Profile table and related logic. Represents additional user-related data stored in a        |
|                    |           | separate table (e.g., bio, avatar URL)                                                                  |
| profile_routes.py  | File      | Routes for user profile management                                                                      |
| README.md          | File      | the main project document containing information on the application and reference to other relevant     |
|                    |           | documentation                                                                                           |
| READMEAI.md        | File      | represents the documentation that has been refined with language that an AI may find easier to consume  |
|                    |           | in order to understand the specifications of this template and  recreate the code to specification      |
|                    |           | quickly with few iterations to get a working product                                                    |
| requirements.txt   | File      | Contains the python library of modules that need to be loaded to support the application                |
| routes             | Directory | Contains Python files defining Flask routes (e.g., `home`, `login`, `register`).                        |
| routes/__init__.py | File      | Initializes the routes module                                                                           |
| services           | Directory | provides a centralized location for business logic and shared utilities, improving the maintainability  |
|                    |           | and scalability of the application. Used to house **business logic**, **application services**, or      |
|                    |           | **utility functions** that are not directly tied to specific routes or models. It serves as a middle    |
|                    |           | layer between the **routes** (API endpoints) and **models** (database schema) in the application's      |
|                    |           | architecture. This directory helps keep the codebase modular, organized, and scalable.                  |
| setup-guide.md     | File      | contains the instructions on which development tools to install and specific configurations needed.     |
|                    |           | Installation steps and troubleshooting for the applications themselves will still need to be referenced |
|                    |           | from the source locations.                                                                              |
| static             | Directory | Contains code or text files to support the application either with styling (style.css) or reference     |
|                    |           | information.                                                                                            |
| static/css         | Directory | Location to store the css styling sheets                                                                |
| static/images      | Directory | Location to store images or icons for use on the web pages                                              |
| static/js          | Directory | Location to store any supporting javascript for the applications                                        |
| style.css          | File      | Main styling sheet for the application. User should create their own styling sheet when bolting on to   |
|                    |           | this application.                                                                                       |
| templates          | Directory | Contains the html files to support the web page applications                                            |
| tests              | Directory | location for scripts that support testing of the application and its environment                        |
| troubleshooting.md | File      | provides and FAQ list of issues that might come up and how to resolve them                              |
| user_model.py      | File      | Defines the User table and associated relationships. - Represents the User table in the database,       |
|                    |           | including fields like username, email, hashed password, and timestamps.                                 |
| user_service.py    | File      | For user management operations                                                                          |
| utils.py           | File      | for shared helper functions                                                                             |
--------------------------------------------------------------------------------------------------------------------------------------------



##### 2.6.2 Password Hashing

- Utilize a minimum configuration for password hashing:

```
# Hash the user's password before storing it in the database.
passwordhash = hashpassword(user_input)
```

##### 2.6.3 Configurations in config.py and .env

- the config.py file will be set up to support application constants and environment variables.
- for storing actual database access username, password, API Keys and other administration information that needs to be hidden, the .env file will be used as the repository with config.py pulling information to assemble the database connect string for example.
- . env will contain the secure database access username and password plus the database connection string that the template and future applications will utilize.
- .env will be initially structured as follows but will take on changes as the functional design is carried out:

```
SECRET_KEY=your_secret_key
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_NAME=logintemplate
DEBUG_MODE=True
```

- **Note** Ensure .env values are replaced with strong, secure credentials before any public or semi-public repository use. For additional security, we will prevent the .env file from uploading to GIThub using the .gitignore file with `.env` entered.
- We will use the .env file to store the actual environment variables with config.py accessing them through dotenv. As a minimum configuration, the config.py will be created with this initial information. Further additions are expected and will be detailed in the functional design that follows:

```
from dotenv import load_dotenv
import os

Load the .env file
load_dotenv()

Application settings
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")  # Fallback to a default if not found
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "logintemplate")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

```

The python-dotenv library will load values from a .env file into your application’s environment variables.

##### 2.6.4 Documentation

- documentation will be constructed following the functional design and development. Included within that documentation set will be the following:
    - README: which will contain the Installation and Configuration instructions to replicate the environment needed to utilize the template and guidelines on how to build applications on top of the template application
    - READMEAI: will be a copy of all sections within this specification document, giving the AI complete instruction on how the application is to be built. It is expected, that by reading this document, the AI will be able to produce:
        - the README file on its own
        - provide all the code to create a functional template using the specifications provided in the READMEAI document.
    - an outline for a user manual that the user can utilize to kickstart their application user manual once their application is ready to deploy. It will initially cover how to register a new user and log in.
    - test plan: following the design and development, the AI will generate a test plan utilizing best practices for testing each of the template functions thoroughly.

##### 2.6.5 Standard Page Layout

- The standard page design will consist of 3 parts:
    - BANNER
        - Positioned at the top.
        - Contains the Title of the application, User Profile Access, and other top-level controls (e.g., Logout button).
    - MENU PANEL
        - Located on the left side of the screen.
        - Includes navigation links and actions (e.g., Home, Profile, Logout).
    - BODY AREA
        - Positioned on the **right side** of the layout and making up a large area of the page.
        - Used for displaying **main application content** like user registration forms, login pages, or dynamic content.
- A basic layout will look like this:

```
+------------------------------------------------------+
|                      BANNER                          |
| (Title / User Profile Access / Other Controls)       |
+------------------------------------------------------+
|                        |                             |
|    MENU PANEL          |         BODY AREA           |
| (Navigation Links,     | (Main Application           |
|  Actions)              |  View / Dynamic Content)    |
+------------------------------------------------------+

```

##### 2.6.6 Webpage Configuration

- To maintain a consistent look and feel across all pages in the application, a layout.html file will be created and stored in the templates/ directory. This file will define the standard page layout, including the banner, menu panel, and body area as described in 2.1 Overview.
    
    - **_Purpose:_**
        
        - layout.html will act as the base template for all other pages in the application.
        - Any new pages (e.g., `register.html, login.html`) must extend this base layout to inherit the standard structure.
    - **_Usage_**
        
        - All new pages created for the application will include the following line at the top to inherit from layout.html:
            
            ```
            {% extends 'layout.html' %}
            ```
            
        - layout.html will include:
            
            - A header section for the banner.
            - A sidebar for the menu panel.
            - A main content block for the body area.
        - The main content of each page will be dynamically injected into the {% block content %} section defined in layout.html.
            
    - **_layout.html Structure_**
        
        - layout.html will define placeholders for dynamic content using Jinja2 templating blocks. For example:
        
        ```
        
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
            <title>{% block title %}My Application{% endblock %}</title>
        </head>
        <body>
            <header class="banner">
                <h1>Application Banner</h1>
                <div>User Profile / Logout</div>
            </header>
            <div class="container">
                <main class="body">
                    {% block content %}
                    <!-- Page-specific content will be injected here -->
                    {% endblock %}
                </main>
                <nav class="menu">
                    <ul>
                        <li><a href="/home">Home</a></li>
                        <li><a href="/profile">Profile</a></li>
                        <li><a href="/logout">Logout</a></li>
                    </ul>
                </nav>
            </div>
        </body>
        </html>
        ```
        
    - **_Example Page Using layout.html_**
        
        - For example, the register.html page for user registration will extend layout.html as follows:
            
            ```
            {% extends 'layout.html' %}
            
            {% block title %}Register{% endblock %}
            
            {% block content %}
            <h2>User Registration</h2>
            <form>
                <!-- Registration form fields go here -->
            </form>
            {% endblock %}
            ```
            
    - **_Documentation Note_**
        
        - The inclusion of this file ensures that:
            - All pages maintain a unified design.
            - Developers can focus on page-specific content without duplicating layout code.
            - Future changes to the layout (e.g., styling or menu updates) can be made centrally in layout.html, propagating across all pages.
    - **_Directory Placement_**
        
        - The layout.html file will be stored under the following path:
            
            ```
            templates/ 
            ├── layout.html 
            ├── index.html 
            ├── register.html
            ```
            

##### 2.6.7 Provisions for Application Testing

- Since this is a Proof of Concept, any user account information or data collected using the template application will be considered test data
- database.sql will not contain any sample data for testing
- database.sql may contain data to populate look-up tables or other reference information. Those dependencies will be noted within the functional design in the next section.

##### 2.6.8 Development Environment Validation

- the developer will perform a validation of the environment once all applications have been installed and configurations completed.
- the validation will be performed manually by the developer for this proof-of-concept and confirmation that all validations were conducted successfully will be sent to the AI before continuing with design and development
- validate the environment using the following checklist:
    
    ---
    
    > ### Development Environment Validation Checklist
    > 
    > #### **1. System Prerequisites**
    > 
    > These steps ensure that the operating system and required software are installed correctly.
    > 
    > - [ ]  Verify the operating system is **Windows 11 Home Version 23H2 Build 22631 4460** or later.
    > - [ ]  Confirm that **Google Chrome** (v130.0.6723.117 or higher) and **Microsoft Edge** (v130.0.2849.80 or higher) are installed and operational.
    > 
    > #### **2. Python and Virtual Environment Setup**
    > 
    > These steps validate that Python and the virtual environment are properly configured.
    > 
    > - [ ]  Confirm that **Python 3.12 or later** is installed:
    >     - Run: `python --version`.
    > - [ ]  Verify that **pip** (Python package manager) is installed:
    >     - Run: `pip --version`.
    > - [ ]  Create and activate a virtual environment:
    >     - Run: `python -m venv venv` to create the virtual environment.
    >     - Run: `venv\Scripts\activate` to activate the environment.
    >     - Verify the virtual environment is active (your terminal prompt should display `(venv)`).
    > 
    > #### **3. Python Modules**
    > 
    > - [ ]  Ensure that all essential modules listed in Section 2.3.7 are listed in `requirements.txt`
    > - [ ] Install all required Python modules listed in `requirements.txt`:
    >     - Run: `pip install -r requirements.txt`.
    > - [ ]  Confirm all required modules are installed:
    >     - Run: `pip list` and check that all modules listed in 2.3.7 are listed in the output.
    > 
    > #### **4. MySQL Database Setup**
    > 
    > These steps ensure the database server and schema are ready for the application.
    > 
    > - [ ]  Install **MySQL Community Server** (v8.0.39 or higher) and verify it is running.
    > - [ ]  Install **MySQL Workbench** (v8.0.38 build 4270059 CE or higher).
    > - [ ]  Start the MySQL server and log in using your credentials:
    >     - Run: `mysql -u [DB_USER] -p`.
    > - [ ]  Create the database for the application:
    >     - Run: `CREATE DATABASE logintemplate;`.
    > - [ ]  Load the `database.sql` schema into the database:
    >     - Use **MySQL Workbench** to execute the SQL script.
    > - [ ]  Verify that all tables and schema objects are created:
    >     - Query the database to list the tables:
    >         - Run: `SHOW TABLES;`.
    > - [ ]  Verify that the developer account has the necessary privileges
    >     - Run: SHOW GRANTS FOR 'developer_admin'@'localhost';
    > 
    > #### **5. Flask Web Server**
    > 
    > These steps confirm the Flask server is functional and accessible.
    > 
    > - [ ]  Verify that Flask is installed in the virtual environment:
    >     - Run: `python -c "import flask; print(flask.__version__)"`.
    > - [ ]  Start the Flask development server:
    >     - Run: `python -m flask run`.
    > - [ ]  Confirm the server output shows it is running on `http://127.0.0.1:5000`.
    > - [ ]  Open your browser and navigate to `http://127.0.0.1:5000/index.html`. Verify the page loads successfully.
    > 
    > #### **6. Client-Side Validation**
    > 
    > These steps validate that the client-side interface is rendered correctly and is interactive.
    > 
    > - [ ]  Verify the following elements are displayed on the page:
    >     - A **banner** with the application title.
    >     - A **right-hand menu panel** with navigation links.
    >     - A **body area** with placeholder content.
    > - [ ]  Perform a basic form validation test:
    >     - For example, enter an invalid email address on a sample form and confirm that appropriate error messages are displayed.
    > - [ ]  Validate an API endpoint to confirm connection to the server and the API are working.
    >     - Run: [http://127.0.0.1:5000/api/test](http://127.0.0.1:5000/api/test)
    >     - Output should give the success message "API is working correctly"
    >     - Use these instructions for validation setup. The response should be dynamically generated and returned directly by the Flask route when the `/api/test` endpoint is accessed.
    >     - The JSON response is defined inline within the Flask route code. Here’s the relevant part of the Flask implementation - as stored in routes/test_routes.py:
    > 
    > ```
    > from flask import Blueprint, jsonify 
    > 
    > test_routes = Blueprint('test_routes', __name__)
    > 
    > @app.route('/api/test', methods=['GET'])
    > def test_api():
    >     return jsonify({
    >         "status": "success",
    >         "message": "API is working correctly",
    >         "data": {
    >             "test_key": "test_value"
    >         }
    >     })
    > 
    > ```
    > 
    > Register the Blueprint: Ensure that this route is registered with the Flask app in the main application file (e.g., `app.py` or `main.py`):
    > 
    > ```
    > from flask import Flask 
    > from routes.test_routes import test_routes 
    > 
    > app = Flask(__name__) 
    > app.register_blueprint(test_routes) 
    > if __name__ == '__main__': 
    >     app.run(debug=True)
    > ```
    > 
    #### **2.6.9 Workspace Configuration**

To ensure that Visual Studio Code recognizes the `logintemplate` package and uses the correct Python interpreter and environment variables, the following workspace-specific settings need to be configured:

1. **Create or Update `.vscode/settings.json`:**

   Add the following content to the `.vscode/settings.json` file to set the Python interpreter path and the `PYTHONPATH` environment variable:

   ```jsonc
   // File Name: logintemplate\.vscode\settings.json
   // Version: 1.0
   // Last Updated: 17-Feb-2025
   // Description: Workspace-specific settings for the logintemplate project.

   {
       "python.pythonPath": "C:\\PythonScripts\\logintemplate\\venv\\Scripts\\python.exe",
       "terminal.integrated.env.windows": {
           "PYTHONPATH": "C:\\PythonScripts\\logintemplate"
       }
   }

   2. Create or Update launch.json:

Add the following content to the launch.json file to configure the launch settings for the Flask application:
// File Name: logintemplate\.vscode\launch.json
// Version: 1.0
// Last Updated: 17-Feb-2025
// Description: Launch configuration for the logintemplate project.

{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/app.py",
            "env": {
                "FLASK_APP": "app",
                "FLASK_ENV": "development"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "cwd": "${workspaceFolder}"
        }
    ]
}

3. Update logintemplate.code-workspace:

Ensure that the logintemplate.code-workspace file references the workspace settings and configurations correctly:

// File Name: logintemplate\.vscode\logintemplate.code-workspace
// Version: 1.0
// Last Updated: 17-Feb-2025
// Description: Workspace-specific settings for the logintemplate project.

{
    "folders": [
        {
            "path": ".."
        }
    ],
    "settings": {
        "python.pythonPath": "C:\\PythonScripts\\logintemplate\\venv\\Scripts\\python.exe",
        "terminal.integrated.env.windows": {
            "PYTHONPATH": "C:\\PythonScripts\\logintemplate"
        }
    },
    "launch": {
        "configurations": [
            {
                "name": "Python: Flask",
                "type": "python",
                "request": "launch",
                "program": "${workspaceFolder}/app.py",
                "env": {
                    "FLASK_APP": "app",
                    "FLASK_ENV": "development"
                },
                "args": [
                    "run",
                    "--no-debugger",
                    "--no-reload"
                ],
                "jinja": true,
                "cwd": "${workspaceFolder}"
            }
        ]
    }
}



    > #### **7. Configuration Validation**
    > 
    > These steps confirm that environment variables and configurations are loaded correctly.
    > 
    > - [ ]  Verify that the `.env` file exists in the project root and contains the following keys:
    > 
    > ```
    >     SECRET_KEY=your_secret_key 
    >     DB_USER=your_db_user 
    >     DB_PASSWORD=your_db_password 
    >     DB_HOST=localhost 
    >     DB_NAME=logintemplate 
    >     DEBUG_MODE=True`
    > ```
    > 
    > - [ ]  Confirm that `.env` is included in the `.gitignore` file to prevent it from being uploaded to GitHub.
    > - [ ]  Test `config.py` by adding a temporary debug print statement:
    >     
    >     > `print(f"Database Host: {DB_HOST}, Debug Mode: {DEBUG_MODE}")`
    >     
    >     - Run the Flask application and verify the correct values are printed in the console.
    > 
    > #### **8. Git Version Control**
    > 
    > These steps ensure that version control is set up correctly.
    > 
    > - [ ]  Verify that Git is installed:
    >     - Run: `git --version`.
    > - [ ]  Check the developer's commit access to the repository
    >     - Run: `git commit --allow-empty -m "Validation test"`
    > - [ ]  Clone the project repository:
    >     - Run: `git clone https://github.com/jttinn/logintemplate.git`.
    > - [ ]  Confirm the repository is up to date:
    >     - Run: `git pull origin main`.


GitHub Copilot: To create a save point for all code under the `logintemplate` workspace, you can use Git to commit the current state of your project. Here are the steps to do so:

1. **Initialize a Git Repository (if not already initialized):**
   Open a terminal in the root directory of your project and run:
   ```sh
   git init
   ```

2. **Add All Files to the Repository:**
   Add all files to the staging area:
   ```sh
   git add .
   ```

3. **Commit the Changes:**
   Commit the changes with a meaningful message:
   ```sh
   git commit -m "Save point: Template for other projects"
   ```

4. **Create a Tag (Optional):**
   You can create a tag to mark this specific save point:
   ```sh
   git tag -a v1.0 -m "Template for other projects"
   ```

### Example Commands
```sh
cd /c:/PythonScripts/logintemplate
git init
git add .
git commit -m "Save point: Template for other projects"
git tag -a v1.0 -m "Template for other projects"
```

This will create a save point in your Git repository that you can use as a template for other projects. You can clone this repository and start development on top of this template for new projects.
    > 
    > #### **9. Application Validation**
    > 
    > These steps ensure the application is functional and can execute key workflows.
    > 
    > - [ ]  Verify the user registration form:
    >     - Enter sample data and confirm the submission process works without errors.
    > 
    > #### **10. Troubleshooting and Documentation**
    > 
    > These steps ensure all validation findings are documented for reference.
    > 
    > - [ ]  Verify the project directory matches the documented structure indicated in section 2.6.1>
    > - [ ]  Document any issues encountered during validation in a troubleshooting section in the README.






SECTION 3: Client Application Web Page Design
3.1 Web Page Style
The web pages will utilize the Bootstrap framework for formatting the layout and text styles.

3.2 Web Page Components
There will be three main components displayed on the web page:

Sidebar: A menu of the user's application options.
Banner: The application header and user information.
Body: The main content area where users perform tasks.
3.3 Sidebar
The sidebar will be located on the left side of the page and will display a menu of options for the user to choose from.

Background Color: #88bbbe
Text Color: #333
The sidebar will contain the following application options:

Log In: A link to the Login Page (currently blank).
About: A link to the About Page (currently blank).
Help: A link to the Help Page (currently blank).
3.4 Sidebar Action
At the top of the sidebar, a small tab will provide the user the option to collapse or expand the sidebar. The rules for collapsing or expanding are as follows:

When the sidebar is fully visible, the tab should show "<".
When the sidebar is collapsed to the left, the tab should show ">".
Clicking "<" will dynamically collapse the sidebar to the left and replace the tab with ">".
Clicking ">" will dynamically expand the sidebar to fully show the content and replace the tab with "<".
3.5 Banner
The banner will appear across the top of the web page and extend 150px vertically from the top.

Primary Title: An H2 element, centered vertically and 20px from the left, with the text "Login Template". This title will be a link to the Home page.
Secondary Title: An H4 element, adjacent to the primary title and in italics, with the text "A Login Utility".
Background Color: #88bbbe
Text Color: #333
A round icon with a person's silhouette will be displayed on the banner, vertically centered at the far right. This icon will be linked to a popup menu. Below the icon, the word "Guest" will be displayed.

Clicking the person icon will display a popup menu with the following links:

Login: Links to the Login page.
Register: Links to the Registration page.
Settings: Links to the AppSettings page.
3.6 Body
The body will contain the application content where users perform tasks.

Background Color: #f3f4f7
Text Color: #4a536e
By default, the login page will be displayed within the body section.