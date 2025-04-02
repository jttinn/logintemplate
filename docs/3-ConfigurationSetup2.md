## File Name: mrclean\docs\3-ConfigurationSetup1.md
## Version: 2.6
## Last Updated: 19-Feb-2025
## Description: PART 2: The document describes how the framework described in 2-ApplicationArchitecture will be Configured and set up.

## 2.3 Password Hashing

- Utilize a minimum configuration for password hashing:

```
# Hash the user's password before storing it in the database.
passwordhash = hashpassword(user_input)
```

## 2.4 Configurations in config.py and .env

- the config.py file will be set up to support application constants and environment variables.
- for storing actual database access username, password, API Keys and other administration information that needs to be hidden, the .env file will be used as the repository with config.py pulling information to assemble the database connect string for example.
- . env will contain the secure database access username and password plus the database connection string that the template and future applications will utilize.
- .env will be initially structured as follows but will take on changes as the functional design is carried out:

```
SECRET_KEY=your_secret_key
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_NAME=ods
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
DB_NAME = os.getenv("DB_NAME", "ods")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

```

The python-dotenv library will load values from a .env file into your application’s environment variables.

## 2.5 Documentation

- documentation will be constructed following the functional design and development. Included within that documentation set will be the following:
    - README: which will contain the Installation and Configuration instructions to replicate the environment needed to utilize the template and guidelines on how to build applications on top of the template application
    - READMEAI: will be a copy of all sections within this specification document, giving the AI complete instruction on how the application is to be built. It is expected, that by reading this document, the AI will be able to produce:
        - the README file on its own
        - provide all the code to create a functional template using the specifications provided in the READMEAI document.
    - an outline for a user manual that the user can utilize to kickstart their application user manual once their application is ready to deploy. It will initially cover how to register a new user and log in.
    - test plan: following the design and development, the AI will generate a test plan utilizing best practices for testing each of the template functions thoroughly.

## 2.6 Standard Page Layout

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

## 2.7 Webpage Configuration

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
            

## 2.8 Provisions for Application Testing

- Since this is a Proof of Concept, any user account information or data collected using the template application will be considered test data
- database.sql will not contain any sample data for testing
- database.sql may contain data to populate look-up tables or other reference information. Those dependencies will be noted within the functional design in the next section.

## 2.9 Workspace Configuration**

To ensure that Visual Studio Code recognizes the `mrclean` package and uses the correct Python interpreter and environment variables, the following workspace-specific settings need to be configured:

## 2.9.1 **Create or Update `.vscode/settings.json`:**

   Add the following content to the `.vscode/settings.json` file to set the Python interpreter path and the `PYTHONPATH` environment variable:

   ```jsonc
   // File Name: mrclean\.vscode\settings.json
   // Version: 1.0
   // Last Updated: 17-Feb-2025
   // Description: Workspace-specific settings for the mrclean project.

   {
       "python.pythonPath": "C:\\PythonScripts\\mrclean\\venv\\Scripts\\python.exe",
       "terminal.integrated.env.windows": {
           "PYTHONPATH": "C:\\PythonScripts\\mrclean"
       }
   }

## 2.9.2 Create or Update launch.json:

Add the following content to the launch.json file to configure the launch settings for the Flask application:
// File Name: mrclean\.vscode\launch.json
// Version: 1.0
// Last Updated: 17-Feb-2025
// Description: Launch configuration for the mrclean project.

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

## 2.9.3 Update mrclean.code-workspace:

Ensure that the mrclean.code-workspace file references the workspace settings and configurations correctly:

// File Name: mrclean\.vscode\mrclean.code-workspace
// Version: 1.0
// Last Updated: 17-Feb-2025
// Description: Workspace-specific settings for the mrclean project.

{
    "folders": [
        {
            "path": ".."
        }
    ],
    "settings": {
        "python.pythonPath": "C:\\PythonScripts\\mrclean\\venv\\Scripts\\python.exe",
        "terminal.integrated.env.windows": {
            "PYTHONPATH": "C:\\PythonScripts\\mrclean"
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

#### 2.10 GitHub Config: 
To create a save point for all code under the `mrclean` workspace, you can use Git to commit the current state of your project. Here are the steps to do so:

2.10.1 **Initialize a Git Repository (if not already initialized):**
   Open a terminal in the root directory of your project and run:
   ```sh
   git init
   ```

2.10.2. **Add All Files to the Repository:**
   Add all files to the staging area:
   ```sh
   git add .
   ```

2.10.3. **Commit the Changes:**
   Commit the changes with a meaningful message:
   ```sh
   git commit -m "Save point: Template for other projects"
   ```

2.10.4. **Create a Tag (Optional):**
   You can create a tag to mark this specific save point:
   ```sh
   git tag -a v1.0 -m "Template for other projects"
   ```

### Example Commands
```sh
cd /c:/PythonScripts/mrclean
git init
git add .
git commit -m "Save point: Template for other projects"
git tag -a v1.0 -m "Template for other projects"
```

This will create a save point in your Git repository that you can use as a template for other projects. You can clone this repository and start development on top of this template for new projects.