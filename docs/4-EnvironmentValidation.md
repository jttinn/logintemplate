## **File Name: logintemplate\docs\4-EnvironmentValidation.md
## **Version: 2.5
## **Last Updated: 16-Feb-2024
## **Description: The document describes how to go about validating the framework once it has been set up and configured

##### SECTION A: OVERVIEW

- the developer will perform a validation of the environment once all applications have been installed and configurations completed.
- the validation will be performed manually by the developer for this proof-of-concept and confirmation that all validations were conducted successfully will be sent to the AI before continuing with design and development
- validate the environment using the following checklist:
    
##### SECTION B: ENVIRONMENT VERIFICATION CHECKLIST

    #### ** 1. System Prerequisites**
 
 These steps ensure that the operating system and required software are installed correctly.
 
 - [ ]  Verify the operating system is **Windows 11 Home Version 23H2 Build 22631 4460** or later.
 - [ ]  Confirm that **Google Chrome** (v130.0.6723.117 or higher) and **Microsoft Edge** (v130.0.2849.80 or higher) are installed and operational.
 
 #### **2. Python and Virtual Environment Setup**
 
 These steps validate that Python and the virtual environment are properly configured.
 
 - [ ]  Confirm that **Python 3.12 or later** is installed:
     - Run: `python --version`.
 - [ ]  Verify that **pip** (Python package manager) is installed:
     - Run: `pip --version`.
 - [ ]  Create and activate a virtual environment:
     - Run: `python -m venv venv` to create the virtual environment.
     - Run: `venv\Scripts\activate` to activate the environment.
     - Verify the virtual environment is active (your terminal prompt should display `(venv)`).
 
 #### **3. Python Modules**
 
 - [ ]  Ensure that all essential modules listed in Section 2.3.7 are listed in `requirements.txt`
 - [ ] Install all required Python modules listed in `requirements.txt`:
     - Run: `pip install -r requirements.txt`.
 - [ ]  Confirm all required modules are installed:
     - Run: `pip list` and check that all modules listed in 2.3.7 are listed in the output.
 
 #### **4. MySQL Database Setup**
 
 These steps ensure the database server and schema are ready for the application.
 
 - [ ]  Install **MySQL Community Server** (v8.0.39 or higher) and verify it is running.
 - [ ]  Install **MySQL Workbench** (v8.0.38 build 4270059 CE or higher).
 - [ ]  Start the MySQL server and log in using your credentials:
     - Run: `mysql -u [DB_USER] -p`.
 - [ ]  Create the database for the application:
     - Run: `CREATE DATABASE logintemplate;`.
 - [ ]  Load the `database.sql` schema into the database:
     - Use **MySQL Workbench** to execute the SQL script.
 - [ ]  Verify that all tables and schema objects are created:
     - Query the database to list the tables:
         - Run: `SHOW TABLES;`.
 - [ ]  Verify that the developer account has the necessary privileges
     - Run: SHOW GRANTS FOR 'developer_admin'@'localhost';
 
 #### **5. Flask Web Server**
 
 These steps confirm the Flask server is functional and accessible.
 
 - [ ]  Verify that Flask is installed in the virtual environment:
     - Run: `python -c "import flask; print(flask.__version__)"`.
 - [ ]  Start the Flask development server:
     - Run: `python -m flask run`.
 - [ ]  Confirm the server output shows it is running on `http://127.0.0.1:5000`.
 - [ ]  Open your browser and navigate to `http://127.0.0.1:5000/index.html`. Verify the page loads successfully.
 
 #### **6. Client-Side Validation**
 
 These steps validate that the client-side interface is rendered correctly and is interactive.
 
 - [ ]  Verify the following elements are displayed on the page:
     - A **banner** with the application title.
     - A **right-hand menu panel** with navigation links.
     - A **body area** with placeholder content.
 - [ ]  Perform a basic form validation test:
     - For example, enter an invalid email address on a sample form and confirm that appropriate error messages are displayed.
 - [ ]  Validate an API endpoint to confirm connection to the server and the API are working.
     - Run: [http://127.0.0.1:5000/api/test](http://127.0.0.1:5000/api/test)
     - Output should give the success message "API is working correctly"
     - Use these instructions for validation setup. The response should be dynamically generated and returned directly by the Flask route when the `/api/test` endpoint is accessed.
     - The JSON response is defined inline within the Flask route code. Here’s the relevant part of the Flask implementation - as stored in routes/test_routes.py:
 
 ```
 from flask import Blueprint, jsonify 
 
 test_routes = Blueprint('test_routes', __name__)
 
 @app.route('/api/test', methods=['GET'])
 def test_api():
     return jsonify({
         "status": "success",
         "message": "API is working correctly",
         "data": {
             "test_key": "test_value"
         }
     })
 
 ```
 
 Register the Blueprint: Ensure that this route is registered with the Flask app in the main application file (e.g., `app.py` or `main.py`):
 
 ```
 from flask import Flask 
 from routes.test_routes import test_routes 
 
 app = Flask(__name__) 
 app.register_blueprint(test_routes) 
 if __name__ == '__main__': 
     app.run(debug=True)
 ```
 #### **7. Configuration Validation**

These steps confirm that environment variables and configurations are loaded correctly.

- [ ] Verify that the [.env](http://_vscodecontentref_/1) file exists in the project root and contains the following keys:

```plaintext
SECRET_KEY=your_secret_key 
DB_USER=your_db_user 
DB_PASSWORD=your_db_password 
DB_HOST=localhost 
DB_NAME=logintemplate 
DEBUG_MODE=True

#### **8. Git Version Control**

These steps ensure that version control is set up correctly.

- [ ] Verify that Git is installed:
    - Run: `git --version`.
- [ ] Check the developer's commit access to the repository:
    - Run: `git commit --allow-empty -m "Validation test"`.
- [ ] Clone the project repository:
    - Run: `git clone https://github.com/jttinn/logintemplate.git`.
- [ ] Confirm the repository is up to date:
    - Run: `git pull origin main`.

#### **9. Application Validation**

These steps ensure the application is functional and can execute key workflows.

- [ ] Verify the user registration form:
    - Enter sample data and confirm the submission process works without errors.
- [ ] Verify the user login form:
    - Enter valid credentials and confirm successful login.
    - Enter invalid credentials and confirm appropriate error messages are displayed.
- [ ] Verify the password recovery process:
    - Enter a registered email address and confirm the recovery email is sent.
    - Enter an unregistered email address and confirm appropriate error messages are displayed.
- [ ] Verify the profile management functionality:
    - Update user profile information and confirm the changes are saved correctly.
- [ ] Verify the CSV upload functionality:
    - Upload a sample CSV file and confirm the data is correctly imported into the database.
    - Upload an invalid CSV file and confirm appropriate error messages are displayed.

#### **10. Troubleshooting and Documentation**

These steps ensure all validation findings are documented for reference.

- [ ] Verify the project directory matches the documented structure indicated in section 2.6.1.
- [ ] Document any issues encountered during validation in a troubleshooting section in the README.
- [ ] Provide detailed steps to reproduce any issues and the corresponding solutions.
- [ ] Update the documentation to reflect any changes made during the validation process.