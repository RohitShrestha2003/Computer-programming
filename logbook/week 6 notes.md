# Introduction to Programming
## Lab Worksheet – Week 6 (Theory Notes)

Topics covered:
Using List methods  
List Comprehensions  
Introduction to Tuples  
Packing and Unpacking  

Using List Methods

The List data type provides powerful functionality for storing and manipulating sequences of values. A list is an ordered collection that supports indexing, slicing, concatenation and iteration. Lists are mutable, meaning their contents can be changed after creation.

Lists are built directly into the Python language and are created using square brackets. Because lists are mutable and iterable, they are widely used in programs for storing collections of data.

Methods

A method is similar to a function but is always associated with a specific data type. When a method is called, it operates on the object it is attached to. Methods are accessed using dot notation, where the method name is preceded by the variable name.

Different data types provide different methods. Methods available for lists are not necessarily available for other data types.

Mutator Methods

Some list methods modify the contents of the list. These are called mutator methods. Examples include adding elements, removing elements, sorting, and reversing the list.

Appending adds a new element to the end of the list. Extending adds multiple elements from another sequence. Inserting adds an element at a specific position. Removing deletes a specific value from the list. Popping removes and returns an element. Clearing removes all elements. Sorting rearranges elements into order. Reversing flips the order of elements.

Accessor Methods

Some list methods do not change the list but return information about it. These are called accessor methods. Examples include finding the index of an element, counting occurrences of a value, and copying the list.

The copy method creates a shallow copy of the list. This is important because assigning one list to another variable does not create a new list, it only creates a new reference to the same list.

Deleting Elements

Elements can be removed from a list using built-in deletion mechanisms. This is more destructive than using methods because it can remove entire variables as well as individual elements.

List Comprehensions

List comprehensions provide a concise way to create lists. They are expressions that generate a list by evaluating an expression for each element in a sequence.

A list comprehension typically includes an expression, a loop, and optionally a condition. The loop defines the values to iterate over, and the expression defines what value is added to the list. The optional condition filters which values are included.

List comprehensions can replace longer loops and append statements, making code shorter and easier to read. They can also include multiple loops and conditions, although this can reduce readability if overused.

Introduction to Tuples

A tuple is a built-in data type similar to a list. It is an ordered sequence of values. The key difference between tuples and lists is that tuples are immutable. Once created, their contents cannot be changed.

Tuples are commonly used to group related pieces of data together. They often contain different types of values. Because they are immutable, tuples are safer to use when data should not be modified.

Tuples support indexing, slicing, concatenation, and iteration, just like lists and strings.

Tuple Packing

Tuple packing is the process of creating a tuple by placing multiple values together. This can be done with or without parentheses, although parentheses are usually used for clarity.

Tuple packing is often used to represent records or structured data.

Empty and Single-Element Tuples

An empty tuple contains no elements. A single-element tuple must include a trailing comma. Without the comma, Python treats the value as a normal variable rather than a tuple.

Sequence Unpacking

Sequence unpacking allows the values in a tuple to be assigned to multiple variables in a single statement. The number of variables on the left side must match the number of values in the tuple.

This is also known as multiple assignment. It is a convenient way to extract values from sequences.

Sequence unpacking can also be used with lists and strings, but it is most commonly used with tuples.

Returning Multiple Values

Tuples are often used to return multiple values from a function. The function packs values into a tuple, and the caller unpacks them into separate variables.

This is a powerful feature of Python and is widely used in practice.

Unpacking in Function Calls

Tuples can be unpacked when calling a function that takes multiple arguments. A special prefix causes the tuple elements to be passed as separate arguments.

This allows flexible argument passing and is useful when working with ranges or variable-length arguments.

Tuple Methods

Because tuples are immutable, they have very few methods. Only methods that do not modify the tuple are available. These include methods to count occurrences of a value and to find the index of a value.

Tuples do not support methods that change their contents, such as append, insert, or remove.

Key Terminology

Method – A function associated with an object.  
List Comprehension – A concise way to create lists using expressions.  
Tuple – An immutable ordered sequence of values.  
Tuple Packing – Combining multiple values into a tuple.  
Sequence Unpacking – Assigning tuple values to multiple variables.  

End of Week 6 Theory Notes
