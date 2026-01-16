# Introduction to Programming
## Lab Worksheet – Week 2 (Theory Notes)

Topics covered:
Working with Variables  
Data Types  
Calling Built-in Functions  
Using Single, Double and Triple Quotes  
Indexing and Slicing  
Introduction to Lists  

Working with Variables

Variables are used to store values for later use in a program. Each variable has a name, also known as an identifier, which is chosen by the programmer. Variable names are usually meaningful nouns that describe what the value represents.

In Python, variable names are case-sensitive and can contain letters, digits, and underscores, but they cannot begin with a digit. Different capitalisations represent different variables, even if the names look similar.

Variables are created and assigned values using the assignment operator. The value on the right-hand side of the assignment is evaluated first and then stored in the variable on the left-hand side. A variable cannot be used before it is assigned a value.

Variables can be reassigned at any time, and the new value replaces the old one. Python also supports augmented assignment, which is a shorthand way of updating a variable using its own value. This makes code shorter and often clearer.

Data Types

Every value in Python has a data type. The data type defines what kind of value it is and what operations can be performed on it. For example, numbers can be added or multiplied, while text values can be joined together.

The most common primitive data types in Python are integers, floats, booleans, and strings. Integers store whole numbers. Floats store numbers with decimal places. Booleans store True or False values. Strings store text.

Python is a dynamically typed language, which means that the data type of a variable is determined by the value assigned to it. A variable can change type during the execution of a program. This provides flexibility but can also lead to unexpected errors if not handled carefully.

The data type of a value determines how operators behave. For example, the addition operator adds numbers but joins strings together. Understanding data types is essential for correct program behaviour.

Calling Built-in Functions

Python provides many built-in functions that perform common tasks. These functions are already written and can be used directly without any extra setup. Examples include functions for displaying output, reading input, finding lengths, and determining data types.

Functions are called by writing the function name followed by parentheses. Values passed into the parentheses are called arguments. Some functions take no arguments, some take one, and others take many.

Some functions return a value, which can be stored in a variable or used as part of an expression. Other functions perform an action but do not return a value.

Functions can be nested, meaning one function call can be used as an argument to another function. In such cases, the inner function is evaluated first.

Getting Input from the User

Programs often need to accept input from users. This input is typically entered through the keyboard. User input is returned as text, even if the user types numbers.

Because input is returned as text, it often needs to be converted into a numeric type before mathematical operations can be performed. This conversion ensures that arithmetic operations work correctly.

Understanding the difference between text input and numeric data is important to avoid logical and runtime errors.

Single, Double and Triple Quotes

Strings in Python can be written using either single quotes or double quotes. Both forms are equivalent and can be used interchangeably. This flexibility allows quotes to be included inside strings without causing errors.

Escape sequences allow special characters to be included in strings. These include new lines, tabs, and quote characters. Escape sequences are written using a backslash followed by a special character.

Triple-quoted strings allow text to span multiple lines and can include both single and double quotes without the need for escaping. They are commonly used for multi-line messages and documentation.

Indexing and Slicing

Strings are sequences of characters. Individual characters within a string can be accessed using indexing. Index positions start at zero, meaning the first character is at position zero.

Negative indices can be used to count from the end of the string. This makes it easy to access characters relative to the right-hand side.

Slicing allows multiple characters to be extracted from a string. A slice is defined by a start position and an end position. The start position is included, and the end position is excluded.

Slicing is flexible and allows omission of start or end positions to indicate the beginning or end of the string. Out-of-range values do not cause errors but are safely ignored.

Introduction to Lists

A list is a collection of values stored in a specific order. Lists can contain values of any data type and can mix different types, although this is usually avoided for clarity.

Lists are written using square brackets with values separated by commas. The same value can appear multiple times in a list.

Like strings, lists support indexing, slicing, concatenation, and repetition. This means elements can be accessed, sublists can be created, and lists can be joined together.

Mutable and Immutable Types

Lists are mutable, which means their contents can be changed after they are created. Elements can be replaced, removed, or inserted at any position.

Strings are immutable, meaning once a string is created, its characters cannot be changed. Any operation that appears to modify a string actually creates a new string.

Understanding the difference between mutable and immutable types is very important. It affects how values behave when passed to functions or assigned to new variables.

Because lists are mutable, they provide more flexibility for storing and modifying collections of data.

Key Terminology

Assignment – Storing a value in a variable.  
Data Type – The classification of a value.  
Argument – A value passed to a function.  
Indexing – Accessing a single element in a sequence.  
Slicing – Accessing a range of elements in a sequence.  
Mutable – A value that can be changed.  
Immutable – A value that cannot be changed.  

End of Week 2 Theory Notes.