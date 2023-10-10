# 0x00. AirBnB clone - The console

# Overview
This project is designed to provide a flexible and powerful storage system that allows you to create, manage, and persist objects via a console/command interpreter. It aims to offer an abstraction layer between your application's data objects and the details of how they are stored and persisted. This abstraction simplifies development and enhances flexibility, allowing you to change the storage mechanism easily without the need for extensive codebase updates.

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


# Usage
*Console Interaction*: Users can interact with your application through the console by entering commands to create, update, or delete objects.

*Data Model Definition*: Define your data model by specifying the attributes and structure of the objects you want to manage.

*Storage Configuration*: Customize the storage system to choose the most suitable storage mechanism for your project, and seamlessly change it if needed.

*Data Persistence*: Objects are automatically persisted to a JSON file, ensuring data integrity and availability across sessions.


