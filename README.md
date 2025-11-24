# Airport-Manager-Project-Semester-1-CSE
Airport Management System (AMS)
Project Title
Airport Management System (AMS): CLI Data Management Solution
Overview of the Project
The Airport Management System (AMS) is a Console Line Interface (CLI) application developed in Python to simulate and manage essential airport data entities. The system provides authenticated users (Administrators) with a menu-driven interface to perform CRUD (Create, Read, Update, Delete) operations on key information regarding Airlines, Flights, Passengers, and Employees. It uses in-memory Python lists for data storage and the tabulate library for clean, table-based output, making it an effective demonstration of data management principles and functional programming.
Features
The system is built around four primary functional modules:
1. Airline Information: Add, remove, and display records for operating airlines, including their aircraft quantity and number of destinations.
2. Flight Information: Manage the active flight schedule, tracking details such as Flight Number, Gate assignment, departure/arrival times, and Status.
3. Passenger Information: Handle passenger records using PNR (Passenger Name Record) and link them to a specific Flight Number.
4. Employee Information & Reporting: Manage employee data (ID, name, salary, shift). Includes an Analytics Report to calculate and display the Average, Minimum, and Maximum salary across all records. 
Technologies/Tools Used
* Core Language: Python 3.x
* External Library: tabulate (Used for creating clean, grid-formatted tables in the console)
* Data Storage: Python In-memory Lists (Simulated database)
* Interface: Console Line Interface (CLI)
Steps to Install & Run the Project
Prerequisites
* Python 3.x installed on your system.
* The tabulate library must be installed.
Setup Instructions
1. Download the code: Clone the repository or download the source file: TEE PROJECT PYTHON AIRPORT MANAGER.py
2. Install the dependency: Open your terminal or command prompt and run:
3. pip install tabulate
4. Run the application: Execute the Python script:
5. python "TEE PROJECT PYTHON AIRPORT MANAGER.py"
Authentication Details
The system requires mandatory login upon startup:
* Username: admin
* Password: airport_admin_123


Instructions for Testing
The system can be tested manually by following the workflow:
1. Login Test: Attempt to log in successfully and verify the lock-out mechanism after 3 failed attempts.
2. CRUD Testing: For each of the four main modules (Airline, Flight, Passenger, Employee), test the following:
o Add: Enter new data and ensure it appears correctly on the Display screen.
o Remove: Successfully delete a record by its identifier (e.g., Flight Number, PNR) and confirm it is no longer displayed.
3. Validation Test: Test the custom input validation, specifically the Do you wish to continue... (yes/no): prompts, ensuring it only accepts 'y', 'n', 'yes', or 'no'.
4. Reporting Test: In the Employee module, add multiple employee records with varying salaries and verify that the Reports function accurately calculates the Average, Minimum, and Maximum salaries.

