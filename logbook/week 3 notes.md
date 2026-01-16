# Introduction to Programming
## Lab Worksheet – Week 3 (Theory Notes
Topics covered:
Boolean Expressions  
Decision making using ‘if’  
Membership testing  
Logical operators  
Ternary operators  
Iteration using ‘while’ and ‘for’  
Breaking and continuing loops  


Boolean Expressions

Boolean expressions are often used in conjunction with control statements such as if and while to decide what action should be taken. A Boolean expression always evaluates to a Boolean value, either True or False. They are fundamental to decision making in programs.

Relational operators are commonly used in Boolean expressions to compare values. These operators compare numeric values, string values and even list values. When strings are compared, the comparison is done alphabetically. Capital letters are considered less than lowercase letters. Lists are compared element by element from left to right.

When using relational operators, both operands must be of the same data type or be convertible to the same data type. If incompatible types are used, a runtime error may occur. Equality operators are more forgiving and may return False instead of an error when types do not match. This can lead to logical errors that are difficult to detect.

Python is dynamically typed, meaning a variable’s data type can change at runtime. Because of this, expressions that work correctly in one situation may fail or behave unexpectedly in another. It is important to always be aware of the data types being used in expressions.

Logical Operators

Logical operators are used to combine multiple Boolean expressions into a single expression. Python provides three logical operators: and, or, and not.

The and operator returns True only if both conditions are True.  
The or operator returns True if at least one condition is True.  
The not operator reverses the result of a condition.

Logical operators can be combined in a single expression. Parentheses are often used to make the intended order of evaluation clear, even when operator precedence would give the same result. This improves code readability and reduces logical errors.

Chaining Relational Operators

Python allows relational operators to be chained together in a single expression. Operator chaining is equivalent to using the logical and operator. It provides a more readable way to check if a value lies within a specific range.

Membership Testing

Membership testing is used to check whether a value exists within a sequence such as a list or a string. Python provides the in and not in operators for this purpose.

When used with lists, membership testing checks whether an element exists in the list. When used with strings, it checks whether a substring exists within the string. Membership testing is often used in combination with relational and logical operators to build complex conditions.

Expressions – Important Points

Expressions are used throughout programs to calculate values and make decisions. Arithmetic expressions are used for calculations, while Boolean expressions are used for control flow. Operator precedence determines the order in which parts of an expression are evaluated. Parentheses should be used to make the intended logic clear.

Because Python is dynamically typed, the data type of a variable can change at runtime. This can cause expressions to behave differently depending on the current value of the variable. Careful design and clear conditions help reduce logical errors.

The if Statement

The if statement is used to perform decision making in programs. It executes a block of code only when a given condition evaluates to True. If the condition is False, the block is skipped.

Python uses indentation to define code blocks. All statements with the same level of indentation belong to the same block. Proper indentation is essential for correct program execution.

The else Clause

An if statement can include an else clause. The code in the else block executes when the condition in the if statement is False. When an if–else structure is used, exactly one of the two blocks will execute.

The elif Clause

The elif clause is used to check additional conditions if the previous conditions were False. Multiple elif clauses can be used. The else clause, if present, must always appear last. This structure is useful when only one out of many possible actions should be performed.

Non-Boolean Conditions

In Python, conditions do not have to be strictly Boolean. Numeric values can be used, where zero is treated as False and any non-zero value is treated as True. Sequences such as strings and lists can also be used as conditions. An empty sequence is treated as False, and a non-empty sequence is treated as True.

Although this is allowed, it is often clearer and safer to use explicit Boolean expressions.

The Ternary Operator

The ternary operator is a compact form of the if–else statement written on a single line. It evaluates a condition and returns one value if the condition is True and another value if the condition is False. Unlike a normal if statement, it does not execute code blocks but returns values.

The ternary operator always requires both the if and else parts. It is commonly used for simple decisions and within larger expressions.

Iteration

Iteration refers to the repeated execution of a block of code. Python supports iteration using while loops and for loops.

The while Loop

A while loop repeatedly executes a block of code while a given condition remains True. The condition is checked before each iteration. If the condition is False at the start, the loop body will not execute at all. Care must be taken to ensure that the condition eventually becomes False, otherwise an infinite loop may occur.

The for Loop

A for loop iterates over a sequence of values such as a list, string, or range. Each value in the sequence is processed one by one. The for loop is commonly used when the number of iterations is known in advance or when iterating through collections.

The range Function

The range function generates a sequence of numbers. It can take one, two, or three arguments. With one argument, it generates values from zero up to but not including the given value. With two arguments, it generates values between a start and end value. With three arguments, it also includes a step value, which controls the increment or decrement.

Breaking Out of Loops

The break statement is used to exit a loop immediately. When break is encountered, the loop stops executing and control moves to the next statement after the loop. This is useful when a condition occurs that makes further iteration unnecessary.

An optional else clause can be attached to loops. The else block executes only if the loop finishes normally and not because of a break statement.

Continuing Loops

The continue statement skips the remaining code in the current iteration and immediately starts the next iteration of the loop. It does not terminate the loop, only the current cycle. This is useful when certain values should be ignored during processing.

Key Terminology

Boolean Expression – An expression that evaluates to True or False.  
Relational Operator – An operator used to compare two values.  
Logical Operator – An operator used to combine or modify Boolean expressions.  
Operator Chaining – Linking multiple relational comparisons in a single expression.  
Ternary Operator – A one-line conditional expression.  
Iteration – Repeating a block of code.  
Nested Loop – A loop inside another loop.

End of Week 3 Theory Notes
