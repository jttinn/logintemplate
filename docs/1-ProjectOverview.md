// File Name: mrclean\docs\1-ProjectOverview.md
// Version: 2.6
// Last Updated: 19-Feb-2025
// Description: Project overview for the mrclean project.


| Version | Date        | Change                                                                                                                                        |
| ------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0     | 25-Nov-2024 | Combined Section 1 & Section 2 into 1 document, version controlled once. Added .vscode directory to the standard directory structure in 2.6.1 |
| 2.1     | 25-Nov-2024 | README.md synced with GitHub at the project root. All other documentation will be added under docs/                                           |
| 2.2     | 26-Nov-2024 | In section 1.3, Rule 8 was changed to add the project directory name when referencing the name of the file and how to update versioning       |
| 2.3     | 27-Nov-2024 | Updated rule 5 in section 1.3 to provide guidance on how to make changes impacting design of this application. Added 2 new python modules to  |
|         |             | section 2.3.7, formatted the table in 2.6.1 to be more readable                                                                               |
| 2.4     | 04-Dec-2024 | Section 2.6.1 Added additional directory structure under static and sorted the table of files and directories for easy lookup                 |
| 2.5     | 18-Feb-2025 | Separated the documentation into manageable parts so the AI can contribute updates. The doc is too long for it to edit currently.             |
| 2.6     | 19-Feb-2025 | Added Apendix with Copilot AI's understanding and agreement to the content herein                                                             |

### **SECTION A: INTRODUCTION**

This document and others under the <workspace>/docs folder are meant to both provide requirement documentation for the application we wish to build AND be a reference document for the AI we are working with to continually reference with respect to groundrules we need to operate under during the development process. This document in particular sets the goals of the project, assumptions and how we want the AI to contribute to this development.

Under the current AI maturity level (as of the date above), the AI often "forgets" one or more of the rules specified in the section named "SECTION D: AI EXPECTATIONS & RULES TO FOLLOW DURING THIS DEVELOPMENT" and so asking the AI to review this section periodically or after restarting the development environment is often needed. 

This document will always be work in Progress due to the rapid expansion of AI capabilities and the need to provide more functionality to this template. 

### **SECTION B: GOALS AND OBJECTIVES**

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

5. ## Generic .CSV Upload to Database Capability ##
    The template will provide a generic way to upload data from a .csv file extracted from Excel into a landing table within a database. This will include the following features:
    - database software with the ability to easily connect to the python application environment
    - a web page and facility to take a user generated .csv file from their system and successfully load it into the database landing table so that queries can be generated
    - the ability to easily notify the user if there is any issue with the file or during its upload to clearly indicate the problem
    - an ability to reference the data loaded in the database and present reporting later

6. **Proof-of-Concept Design Philosophy**:  
    The framework is for proof-of-concept purposes and should remain simple. However, simplicity should not compromise foundational quality. The framework must incorporate structural components that encourage modularity, scalability, and extensibility to support future applications.

#### **SECTION C: PROJECT ASSUMPTIONS**

1. **Environment Scope**:  
    The template is limited to proof-of-concept development and does not require support for environments such as test, UAT, or production.
    
2. **Configuration Management**:
    
    - The Application  settings and constants must not be hardcoded or embedded within application logic.
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

#### **SECTION D: AI EXPECTATIONS & RULES TO FOLLOW DURING THIS DEVELOPMENT**

It is expected that the AI will contribute significantly to the development of this application. Much of the code will be provided by the AI in response to requirements provided in this document or through regular conversational feedback during the application development.  In order to make the communication and subsequent development effort as streamlined as possible, the AI must follow these rules of engagement during the development at all times:

1. **Rule 1: The Project Goals in SECTION B need to be adhered to whenever features are being proposed or modified**  
    The goals outlined in SECTION B: GOALS AND OBJECTIVES provide a general understanding of the application and development process. The AI may contribute to refining the goals to improve clarity for itself, but any deviations from the goals that have not been agreed to between AI and develper are not permitted. If a deviation becomes necessary during feature development, the AI must notify the user of this and provide a detailed reason for the change. If the change is mutually agreed to then Work will pause, the specific goals will be redefined, and completed work will be reviewed and updated before continuing with any development work.
    
2. **Rule 2: Comply with Change Management procedures and ensure Consistency in Tools and Configurations**  
    Tools and configurations define the development framework. These are fixed once the AI and developer have agreed and have been formally documented in the 2-ApplicationArchitecture.md file found in the docs/ directory. During development, the AI must assume these specifications are complete and No new tools or changes to existing ones are to be informally introduced without consultation with the developer. That also means that the AI will not give examples of commands, configurations or tools that are not relevant to the work already performed. For example, during development, the AI will not provide examples of commands that can only be executed in a UNIX or iOS environment when it is understood that the development environment the user has estabilshed utilizes a Microsoft Windows environment. All discussion of commands, configurations or tools must be within the constraints of the environment already established.
    
     If the AI believes that in order to simplify application development or add new features in the future, additional tools, software libraries or configurations should be made, then these proposals need to go through a change management process and discussed first before suddenly introducing them into new code or configuration files. However, to start that discussion, the AI must evaluate whether the change is still in compliance with the goals and objectives written in SECTION B: GOALS AND OBJECTIVES or would cause us to deviate from any of the rules of engagement written in this section. Changing goals or rules of engagement must be discussed first before any tools, libraries or configurations are proposed. If there are no impacts to rules of engagement, goals or objectives then the AI can make the proposal by following these Change Management steps: 
     
        2.1 the AI must pause all feature development work. DO not provide code that already utilizes new tools or configurations. This is to avoid confusion with which code the AI believes is current and what the development team believes is the current version. 
        2.2 the AI will introduce the proposed tool or configuration within the AI chat area by first identifying the communication with: ** PROPOSED CONFIGURATION CHANGE ** then add the description of the change or name of the tool. 
        2.3 along with the proposal, the AI needs to provide a reason why the change is needed and any impacts
        2.4 development work will be stopped until the developer has been given time to review the change
        2.5 If the developer has decided to reject the change, then development will continue without implementing the change and the AI will not continue to propose the same change impacting the same feature and/or section of code again. However if the tool or configuration change impacts a different feature being developed in the future then the change may be proposed again. 
        2.6 if the developer has decided to approve the change, the AI must recommend updates to the relevent sections of the 2-ApplicationArchitecture.md document and any other documentation under the docs directory that are impacted
        2.7 next, the AI will review code already written to determine impacts and suggest changes which incorporate the change. 
        2.8 the developer will assist with introducing the new tools and/or configration changes including any change to application code
        2.9 the AI will assist with any testing that needs to be repeated to ensure continutity
        2.10 the AI and developer will review all the changes and test results together. If changes are complete and testing has completed successfully, only then can new feature development be continued 
    
3. **Rule 3: Balance simplicity with structured programming methods, application security and proven software quality standards**  
    In line with GOAL 6 from the SECTION B: GOALS AND OBJECTIVES, the AI must balance simplicity with the need for structured programming and software quality. For proof-of-concept purposes, overengineering and excessive security measures are unnecessary as the data in this template is not confidential or sensitive. However, where possible, the AI needs to employ structured programming that allows the developer to easily improve quality and security of the application at a later date without having to perform a major re-write of the code. 
    
4. **Rule 4: AI and Developer must agree ALL sections of this document Before any Development**  
    The AI must be clear on all sections of this document and the document entitled 2-ApplicationArchitecture.md before starting any feature discussions or coding. Once the AI and developers agree on the goals, architecture and the rules of engagement, only then can development begin.
    
5. **Rule 6: Beginner-Friendly Guidance**  
    The AI must assume the user is a beginner in Python, GitHub, and JavaScript. The AI must provide clear explanations, benefits, and examples to guide feature design and implementation while adhering to best practices.
    
6. **Rule 7: Documentation Requirements**  
    At the end of the project, the AI must generate:
    
    - A README file with step-by-step instructions for developers to install, configure, and adapt the template.
    - A READMEAI file with detailed instructions for AI systems to recreate the codebase, including placeholders for adding new features.
    
7. **Rule 8: File Versioning Standards**  
    The AI must include a header in every file created for the application. including documentation that contains the following information: 
    
    - the project directory and File name.  
    - Version number (format: 1.0, 1.1, etc.).
    - The creation or Last update date.
    - A brief description.  

    Here is a sample:
    
```
# File Name: app/main.py   
# Version: 1.0   
# Last Updated: 19-Nov-2025  
# Description: Entry point for the Login Template application.`  
```
    - when creating a new file, the AI will assign version 1.0 as the initial version number and use the current date for the date displayed next to Last Updated 
    - when the AI is making a change to existing code then the AI will auto-increment the version number and update the Last Updated date to the current date
    - All files under the workspace folder MUST have this header and information present. 
    
9. **Rule 9: Make code changes easy for the developer to identify and apply the update**  
    When providing partial code for an existing file, the AI must provide:
    -  the entire content of the file even if it is one line
    - a description of the change 
    - an updated header showing the new version number and date updated
    
10. **Rule 10: Commenting Standards**  
    The AI must annotate key blocks of code with concise and clear comments. Comments should be placed above the relevant code, avoiding inline comments unless absolutely necessary. Multi-line comments are acceptable for documenting complex logic.
    
#### **SECTION E: OTHER DELIVERABLES **

##### **Additional Notes**

- This project is named `mrclean`. All references to this project should use this name or its acronym, `LT`.  In the convention used within the application development environment, the project name and workspace name will be the same. 
- As feature definitions progress, additional documentation and configuration formats (e.g., README file structures) will be addressed in subsequent sections.


## APPENDIX I: AI Agreement

#### Developer (Me): 
Do you understand the rules of engagement between you (the AI) and I (the developer) and are you able to follow these rules for all future engagement on this project?

#### Copilot AI:
Yes, I understand the rules of engagement between you (the developer) and me (the AI) as outlined in the 1-ProjectOverview.md document. I will follow these rules for all future engagements on this project. Here is a summary of the key rules and expectations:

Summary of Rules and Expectations
1. Adherence to Project Goals:
- Follow the goals outlined in SECTION B: GOALS AND OBJECTIVES.
- Notify the developer if any deviations are necessary and provide detailed reasons for the change.
Change Management Procedures:

2. Comply with the documented tools and configurations.
- Propose new tools or configurations through a formal change management process.
- Pause feature development work when proposing changes and await developer approval.

3. Balance Simplicity with Structured Programming:
- Employ structured programming methods and maintain software quality.
- Avoid overengineering and excessive security measures for proof-of-concept purposes.

4. Agreement on Documentation:
- Ensure clarity on all sections of the 1-ProjectOverview.md and 2-ApplicationArchitecture.md documents before starting feature discussions or coding.
- Beginner-Friendly Guidance:

5. Assume the user is a beginner in Python, GitHub, and JavaScript.
- Provide clear explanations, benefits, and examples.

6. Documentation Requirements:
- Generate a README file with step-by-step instructions for developers.
- Generate a READMEAI file with detailed instructions for AI systems.

7. File Versioning Standards:
- Include a header in every file with the project directory, file name, version number, creation or last update date, and a brief description.
- Auto-increment the version number and update the last update date when making changes.

8. Code Changes Identification:
- Provide the entire content of the file when making partial code changes.
- Include a description of the change and an updated header.

9. Commenting Standards:
- Annotate key blocks of code with concise and clear comments.
- Place comments above the relevant code and use multi-line comments for complex logic.

## Confirmation
I confirm that I understand these rules and will follow them for all future engagements on this project. If you have any further instructions or need clarification on any point, please let me know.