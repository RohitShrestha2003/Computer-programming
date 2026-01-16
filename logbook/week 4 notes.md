# Introduction to Programming
## Lab Worksheet – Week 4 (Theory Notes)
Topics covered:
Importing and Using Functions  
Defining and Documenting Functions  
Default and keyword arguments  
Arbitrary Length Argument Lists  
Lambda Expressions  

Importing and Using Functions

Functions provide a mechanism for reusing existing code. Instead of writing the same code repeatedly, a function can be written once and called whenever required. Python includes many built-in functions such as print(), input() and range(), which can be used directly without any import.

In addition to built-in functions, Python provides access to many other functions stored in modules. A module is a file that contains related functions, constants and other elements. To use functions that are not built into the language, the relevant module must be imported.

The Python Standard Library contains a large collection of useful modules that are always available with Python. These modules provide functionality for mathematics, dates and times, file handling, and much more. Third-party modules can also be installed to extend Python’s capabilities, but these are not included by default.

Modules can be imported in different ways. An entire module can be imported, allowing access to all of its contents using the module name as a prefix. Individual functions can be imported from a module, allowing them to be used without the module prefix. It is also possible to import all contents of a module using a wildcard, although this is not recommended as it can cause name conflicts.

Modules can contain constants as well as functions. Constants are values that do not change and can be imported and used in the same way as functions.

Defining Functions

In addition to using existing functions, Python allows programmers to define their own functions. This allows commonly used code to be grouped into a single reusable block. Defining functions improves code organisation, readability, and maintainability.

Functions are defined using the def keyword, followed by the function name, a list of formal parameters in parentheses, and an indented block of code. The function name should describe what the function does.

Once defined, a function can be called multiple times from different parts of the program. This avoids repetition and makes programs easier to modify.

Docstrings

A docstring is a documentation string used to describe the purpose of a function. Docstrings are written using triple quotes and appear as the first statement inside the function definition. They should begin with a capital letter and end with a full stop. If the description spans multiple lines, the second line should be blank.

Docstrings are used by Python’s help system and are an important part of writing clear, professional code.

Formal and Actual Parameters

Formal parameters are the variable names listed in a function definition. They act as local variables inside the function. Actual parameters, also called arguments, are the values passed to the function when it is called.

Formal parameters and variables declared inside a function have local scope, meaning they can only be accessed inside that function. This prevents naming conflicts and helps keep code organised.

Returning Values from Functions

Functions can return values to the caller using the return statement. When a return statement is executed, the function ends immediately and control returns to the calling code along with the returned value.

If a function does not include a return statement, it automatically returns the special value None. Returning values allows functions to be used in expressions and assignments.

Default Arguments

Default arguments allow functions to be called with fewer arguments than defined. A default value is assigned to a formal parameter in the function definition. If no value is provided for that parameter in the call, the default value is used.

Default arguments make functions more flexible and easier to use. Parameters with default values must appear after parameters without default values in the function definition.

Keyword Arguments

Keyword arguments allow actual parameters to be passed by explicitly naming the formal parameter. This means the order of arguments in the function call does not need to match the order in the function definition.

Using keyword arguments improves readability and reduces errors, especially when functions have many parameters. Positional arguments must appear before keyword arguments in a function call.

It is possible to mix positional and keyword arguments in a single call, as long as positional arguments come first.

Arbitrary Length Argument Lists

Python allows functions to accept an arbitrary number of arguments. This means the number of arguments is not fixed. This is achieved using a special syntax that collects extra arguments into a tuple.

This feature is useful when the exact number of values is not known in advance. Arbitrary length argument lists are commonly used in built-in functions such as print().

Variadic arguments are usually placed at the end of the parameter list. They can be followed only by keyword-only parameters.

Lambda Expressions

A lambda expression is a small anonymous function defined using the lambda keyword. Unlike regular functions, lambda expressions do not have a name unless they are assigned to a variable. They are defined using a single expression and do not use a code block.

Lambda expressions are often used when a small, simple function is required for a short period of time, such as when passing a function as an argument to another function. They are commonly used with functions that process collections of data.

Lambda expressions can include formal parameters, default values, and variable-length arguments. They return the result of the expression automatically.

Because lambda expressions are concise, they are useful for writing compact and readable code, but they should not be used for complex logic.

Key Terminology

Module – A file containing Python definitions and statements.  
The Python Standard Library – A collection of modules included with Python.  
Formal Parameters – The variable names in a function definition.  
Actual Parameters – The values passed to a function when it is called.  
Default Arguments – Parameters that have predefined values.  
Keyword Arguments – Arguments passed using parameter names.  
Lambda Expression – A small anonymous function defined using the lambda keyword.  

End of Week 4 Theory Notes
