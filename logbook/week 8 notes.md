# Introduction to Programming
## Lab Worksheet – Week 8 (Theory Notes)

Topics covered:
Basics of Input and Output  
String Formatting  
File Handling  
Reading and Writing Files  
Random File Access  

Basics of Input and Output

All programs follow the same basic pattern: they take input, perform some processing, and produce output. Input can come from many sources such as users, files, networks, or other programs. Output can be displayed on the screen, written to a file, or sent to another system.

In command-line programs, user input is commonly taken through keyboard entry, and output is displayed in the console. In graphical applications, input may come from buttons, menus, and text fields. Input and output are not limited to user interaction and can include communication with files and network systems.

When producing output, it is often necessary to control the layout and appearance of the text. This may involve aligning text, limiting decimal places, or arranging values into columns. Python provides several powerful mechanisms to support output formatting.

String Formatting

String formatting is the process of embedding variable values or expressions inside strings in a controlled way. Python supports multiple formatting approaches, allowing values to be inserted into strings and displayed with specific alignment, precision, or layout.

Formatted strings can include expressions directly within them, allowing calculations and variable values to be displayed as part of a message. Formatting is especially useful when generating user-friendly output or when producing structured data for other systems to read.

Format Specifiers

Format specifiers are used to control how values appear when formatted. They can define the number of decimal places, minimum column width, alignment, and fill characters. Format specifiers allow precise control over how text and numbers are displayed.

Text values are typically aligned to the left, while numbers are aligned to the right by default. Alignment can be changed to left, right, or centre. Padding characters can also be customised. Format specifiers are commonly used to display tabular data neatly.

Different numeric bases such as binary and hexadecimal can also be displayed using format specifiers. This is useful in low-level programming, debugging, and data processing.

Alternative Formatting Approaches

Python supports more than one way to format strings. In addition to modern formatting methods, older approaches still exist and are widely seen in existing code. These allow values to be inserted into strings using positional or keyword-based replacement.

Manual formatting can also be achieved using string methods that align or pad text. Although these approaches are sometimes useful, dedicated formatting mechanisms are generally clearer and more powerful.

File Handling

File handling allows programs to store data permanently and retrieve it later. Files can contain text or binary data. Text files store readable characters, while binary files store raw bytes.

Python provides built-in support for opening, reading, writing, and closing files. External modules also exist to work with common file formats such as JSON, CSV, images, and spreadsheets.

Opening, Reading, and Closing Files

Before a file can be accessed, it must be opened. Opening a file creates a file object that represents the connection between the program and the file. Once opened, the file’s contents can be read or written.

After processing a file, it must be closed. Closing a file releases system resources and ensures that all data is properly saved. It is good practice to always close files after use.

Files can be read in full, read line by line, or processed using iteration. Reading line by line is often more efficient, especially for large files.

Modes of Operation

When opening a file, a mode must be specified to indicate how the file will be used. Common modes include reading, writing, appending, and reading with writing. Files can also be opened in binary mode.

If a file is opened for writing or appending and does not exist, it is created. If it is opened for reading and does not exist, an error occurs. Choosing the correct mode is essential to avoid data loss or errors.

Binary Files

Binary files contain raw byte data rather than text. They are used for images, audio, video, and other non-text formats. When working with binary files, data is handled as bytes rather than strings.

Binary file processing allows precise control over file contents and is commonly used in systems programming, multimedia processing, and network communication.

Writing to Files

Writing to files allows programs to store results, logs, or generated data. Files must be opened in a mode that supports writing before content can be added.

Text must be written as strings. Non-string values must be converted before writing. Writing can either overwrite existing content or append to the end of the file depending on the selected mode.

Random File Access

Files normally process data sequentially, from start to end. Random access allows a program to move directly to a specific position within a file. This is useful when working with large files or structured binary data.

The file position can be read and changed. This makes it possible to reread sections of a file or jump to specific locations. Random access is more reliable in binary files than in text files.

Exception Handling and Safe File Usage

File operations are prone to errors. A file may not exist, permissions may be missing, or hardware problems may occur. Python provides exception handling to deal with such situations gracefully.

It is important to ensure that files are always closed, even when errors occur. Python provides a structured way to manage files safely so that they are automatically closed when no longer needed. This prevents data corruption and resource leaks.

Key Terminology

f-string – A modern way to embed expressions inside strings.  
Format Specifier – A code used to control the appearance of formatted output.  
File Modes – Settings that define how a file is opened and used.  
Binary Files – Files that store raw byte data rather than text.  
Random Access – The ability to move directly to any position in a file.  
Exceptions – Run-time errors that can be detected and handled by a program.  

End of Week 8 Theory Notes
