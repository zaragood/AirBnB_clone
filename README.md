# 0x00. AirBnB clone - The console

# Overview
This project is designed to provide a flexible and powerful storage system that allows you to create, manage, and persist objects via a console/command interpreter. It aims to offer an abstraction layer between your application's data objects and the details of how they are stored and persisted. This abstraction simplifies development and enhances flexibility, allowing you to change the storage mechanism easily without the need for extensive codebase updates.

# AirBnB Clone - Command Line Interpreter
# Project Description
The AirBnB Clone Command Line Interpreter is a command-line tool designed to interact with and manage instances of various data models. This project is part of a larger AirBnB-like application and focuses on providing a user-friendly interface for creating, managing, and querying data models.

Command Interpreter
The Command Line Interpreter (CLI) allows you to perform the following actions:

Create new instances of supported data models.
Show information about existing instances.
Destroy (delete) instances.
Update attributes of instances.
List all instances of a specific data model.
Quit the program.

# How to Start It
1. Clone the project repository to your local machine:

https://github.com/wagzyAyo/AirBnB_clone.git

2. Navigate to the project directory:

cd AirBnB_clone

3. Start the command interpreter by running the following command:

./console.py

# How to Use It
Once the command interpreter is running, you can enter commands at the prompt (by default, (hbnb)).

The supported commands include:

create <class name>: Create a new instance of the specified class.
show <class name> <id>: Display information about an instance based on its class and ID.
destroy <class name> <id>: Delete an instance based on its class and ID.
update <class name> <id> <attribute name> "<attribute value>": Update an instance's attribute.
<class name>.all(): List all instances of a specific class.
quit or EOF: Exit the command interpreter.

# Examples
Here are some examples of how to use the AirBnB Clone Command Line Interpreter:

1. Creating a User:

(hbnb) create User

2. Showing a User:

(hbnb) show User 12345

3. Listing all Users:

(hbnb) User.all()

4. Updating a User's email:

(hbnb) update User 12345 email "newemail@example.com"

5. Quitting the program:

(hbnb) quit

# Key Features
1. Console Interface
Create a user-friendly command-line console that serves as a tool for interacting with your data objects.
The console allows users to perform various operations such as creating, updating, destroying, and more, all through text-based commands.
2. Data Model
Define a robust data model that represents the structure and attributes of the objects you intend to manage.
This model serves as a blueprint for creating and working with your objects.
3. Powerful Storage Engine
Implement a storage system that provides a powerful abstraction layer between your application and the underlying storage mechanisms.
This abstraction allows you to focus on your application logic without worrying about the intricacies of storage.
4. Data Persistence
Objects are stored and persisted to a file, typically in a JSON format.
This ensures that your data remains intact between application runs and can be easily loaded when needed.
5. Flexibility
The abstraction layer in the storage engine ensures that changes to the storage mechanism can be made without extensive code modifications.
This flexibility allows you to switch between storage types seamlessly, adapting to your project's evolving needs.
