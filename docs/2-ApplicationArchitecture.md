**File Name: logintemplate\docs\2-ApplicationArchitecture.md
**Version: 2.6
**Last Updated: 19-Feb-2025
**Description: The document describes the Application Architecture to be utilized for the logintemplate application


| Version | Date        | Change                                                                                                                                        |
| ------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0     | 25-Nov-2024 | Combined Section 1 & Section 2 into 1 document, version controlled once. Added .vscode directory to the standard directory structure in 2.6.1 |
| 2.1     | 25-Nov-2024 | README.md synced with GitHub at the project root. All other documentation will be added under docs/                                           |
| 2.2     | 26-Nov-2024 | In section 1.3, Rule 8 was changed to add the project directory name when referencing the name of the file and how to update versioning       |
| 2.3     | 27-Nov-2024 | Updated rule 5 in section 1.3 to provide guidance on how to make changes impacting design of this application. Added 2 new python modules to  |
|         |             | section 2.3.7, formatted the table in 2.6.1 to be more readable                                                                               |
| 2.4     | 04-Dec-2024 | Section 2.6.1 Added additional directory structure under static and sorted the table of files and directories for easy lookup                 |
| 2.5     | 16-Feb-2024 | Initial version of the Application Architecture document                                                                                      |
| 2.6     | 19-Feb-2025 | Updated to include the latest review and confirmation of the architecture                                                                     |

#### SECTION A: OVERVIEW

- This simplified architecture utilizes a client-server configuration with a webpage front end on the client side and a Windows-based server running Python and utilizing MySQL database on the server side.
- As this is a template for other applications to build on, this application will simply provide a basic framework that is fully functional with these main features:
    - Complete instruction on configuring a working environment, composed of many applications and modules, and making them as simple as possible.
    - A webpage front end designed utilizing a fixed styling and layout composed of a panel for menu options on the right, a banner with title and user profile access, and a body where the user applications will run.
- The template will already build in user registration and login features with the expectation that this feature will be a common requirement for all applications built utilizing this framework.
- This design is not intended for production or migration to other databases or cloud platforms. However, if design decisions can be made that will help minimize possible rework of the solution and do not overcomplicate this proof-of-concept, then this would be preferred.
- A troubleshooting guide will be provided following the release of the Proof-of-Concept and will not be the focus of this section.

#### SECTION B: DEVELOPMENT INFRASTRUCTURE REQUIREMENTS 

## 1. Software Requirements - Client

- Applications running on the Client side will utilize the following products and coding languages:
    
### 1.1 Internet Browser:
- Latest stable version of Google Chrome (Side note: My current version is: Windows 11 Version 130.0.6723.117 (Official Build) (64-bit))
- Latest stable version of Microsoft Edge (Side Note: My current version is: 130.0.2849.80 (Official build) (64-bit))
- NOTE: this Proof-of-Concept configuration has only been optimized for Chrome v130+ and Edge v130+.
- This proof-of-concept will not undertake browser testing for compatibility. Compatibility with other versions or other browsers is not guaranteed.

### 1.2 Web Pages:
- HTML for rendering web pages
- Use **Vanilla JavaScript** for dynamic actions and form validations.
- AJAX and Fetch API will handle dynamic client-server interactions, ensuring compatibility with modern practices.
- style.css will manage the styling for the web pages and be created manually and served from the web server o/s

- Access to the proof-of-concept application will be through localhost using:
    
    ```
    http://127.0.0.1:5000/index.html
    ```

## 2. Software Requirements - Server

- Applications and coding languages utilized for the server-side application development, maintenance, and user implementation are as follows:

### 2.1 O/S:
- Windows 11 Home Version

### 2.2 Webserver:
- FLASK

### 2.3 IDE:
- Visual Studio Code
- Visual Studio Code will also be used for access to terminal command line options. For that reason, the integrated terminal (Ctrl+`) must be enabled

### 2.4 Database:
- MySQL Community Server - GPL, Win64, version 8.0.39 or higher
- MySQL Workbench, version 8.0.38 build 4270059 CE (win64)
- The developer must have their own user account and will be granted full admin access to the database in order to create schemas and objects as required
- The name of the database for this application will be called 'ods' which stands for operational data store.

### 2.5 Version Control:
- GitHub
- The repository will be configured at:
    
    ```
    jttinn/logintemplate
    ```
    
- Access to the GitHub repository from Visual Studio Code will be configured to make it easy for code access and version control

### 2.6 Server-side Development Languages:
- Python 3.12 or later
- SQL for creation and maintenance of database structures
- MySQL procedural SQL for database operations to be called as needed from the application or via database trigger events

### 2.7 Python Modules:
The following Python modules are required for the server-side application development:

- Flask: The lightweight web server framework for the application.
- mysql-connector-python: MySQL Connector for Python to enable database connectivity.
- SQLAlchemy: Object Relational Mapping (ORM) to manage database models.
- Werkzeug: Required for password hashing and general security utilities.
- python-dotenv: To manage environment variables securely.
- MarkupSafe: A Flask dependency, included explicitly to avoid version conflicts.
- Flask-SQLAlchemy: Extension for SQLAlchemy support in Flask applications.
- Flask-Login: For user session management

### 2.8 ORM (Object-Relational Mapping) Tool:
- SQLAlchemy