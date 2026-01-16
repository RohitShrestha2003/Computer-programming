# Introduction to Programming
## Lab Worksheet – Week 5 (Theory Notes)

Topics covered:
Writing code in files  
Executing program files  
Accessing command line arguments  
Writing and importing modules  
The modules search path  

Writing Code in Files

Python programs can be written and executed in two main ways: interactively using the interpreter in Read-Evaluate-Print Loop (REPL) mode, or by writing code into text files and executing those files as programs. REPL mode is mainly used for small experiments and learning, while larger programs are written in files.

When code is stored in files, it can be edited, saved, and executed multiple times. This makes it possible to develop larger and more complex programs over time. Python files are plain text files and must use the `.py` file extension.

When running code from a file, results of expressions are not automatically printed to the screen. Output must be explicitly produced using the `print()` function. This is different from interactive mode, where expression results are displayed automatically.

Storing code in files also allows functions and classes to be defined and reused across different programs. This supports modular design and code reuse.

Choosing an Editor

Because Python files are plain text, they can be written using any text editor. This includes simple editors as well as more advanced development environments.

Many programmers use Integrated Development Environments (IDEs). IDEs provide additional features such as syntax highlighting, auto-completion, error detection, debugging tools, and integrated execution. These tools make development faster and reduce errors, but they are not required to write Python programs.

Understanding how to write and execute programs without an IDE is important because it helps build a deeper understanding of how Python works.

Executing a Script

A Python script is executed by passing the filename to the Python interpreter. The interpreter loads the file, reads the code, and executes it line by line. For this to work, the file must exist and contain valid Python code.

It is common practice to organise Python files into directories and run programs from the directory where they are stored. This makes file management and execution easier.

Comments are often added to code in files to explain what the program does. As programs grow larger, comments become important for readability and maintenance.

Command Line Arguments

Programs often need input in order to perform their tasks. One way of providing input is through command line arguments. These are values provided after the program name when it is executed from the command line.

Command line arguments are useful for utility programs and automated processes because they allow programs to run without user interaction. The values provided as command line arguments are treated as input to the program.

Python stores command line arguments in a list. The first element is always the name of the program itself, and the remaining elements are the values passed by the user. These values are stored as strings and must be converted if numeric processing is required.

Writing Modules

Any Python file can act as a module. A module is simply a file that contains Python definitions and statements. Modules are used to organise code into reusable components.

Modules often contain related functions, variables, and constants. They can be imported into other programs, allowing the same code to be shared across multiple projects. This supports modular programming and reduces duplication.

When a module is imported, the code inside the module is executed. This is often used to initialise values or set up resources. For this reason, modules should be written carefully to avoid unwanted side effects when imported.

A collection of modules is commonly referred to as a library. Python provides many built-in modules, and programmers can also create their own modules.

Methods of Importing

There are several ways to import modules and their contents into a program. Importing an entire module makes all its contents available using the module name as a prefix. Importing specific elements from a module allows direct access to those names without using the module prefix.

It is also possible to import all contents of a module into the current namespace. This is generally discouraged because it increases the risk of name clashes and makes code harder to read.

Each module has its own symbol table, which stores the names defined within it. This prevents name conflicts between different modules. The way a module is imported determines how its names are added to the current program’s symbol table.

Import Aliases

An alias can be assigned to a module or imported element during import. This allows a shorter or more convenient name to be used in the program. Aliases are useful for avoiding name conflicts and improving readability.

Using aliases is common when working with modules that have long names or when multiple modules define functions with the same name.

Listing Symbol Table Names

Python provides a way to list the names defined in the current symbol table or in a module’s symbol table. This is useful for exploring modules and understanding what functions and variables they contain.

This feature is mainly used in interactive mode for learning and debugging.

The Module Search Path

When a module is imported, Python searches for it in specific locations. It first checks the built-in modules, then searches a list of directories known as the module search path.

The module search path is stored in a list that is initialised when the program starts. It includes the directory of the running script and other system-defined locations.

The search path can be modified, but hard-coding paths into programs is not recommended. Instead, environment variables can be used to add directories to the search path in a portable way.

Writing a Script and a Module

A single Python file can be written so that it can act as both a standalone script and a reusable module. This allows the file to be executed directly or imported by other programs.

Python provides a special variable that indicates how a file is being used. By checking this variable, a program can decide whether to run certain code only when it is executed directly, and not when it is imported.

This technique is commonly used to include test code or example usage in a file without affecting programs that import it as a module.

Key Terminology

IDE – An Integrated Development Environment used for writing and debugging code.  
Module – A file containing Python definitions and statements.  
Command Line Arguments – Values passed to a program when it is executed.  
Symbol Table – A structure that stores names and their associated objects.  
Search Path – The list of locations Python checks when importing modules.  

End of Week 5 Theory Notes
