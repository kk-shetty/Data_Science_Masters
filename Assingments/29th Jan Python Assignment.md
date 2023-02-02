##### 1. Who developed Python Programming Language?
>Guido van Rossum developed the Python programming language.

##### 2. Which type of Programming does Python support?
>Python supports multiple programming paradigms, including procedural, object-oriented, functional, and aspect-oriented programming.

##### 3. Is Python case sensitive when dealing with identifiers?
>Yes, Python is case sensitive when dealing with identifiers, such as variable names, function names, and class names. For example, the names "foo" and "Foo" would be treated as two different identifiers in Python.

##### 4. What is the correct extension of the Python file?
>The correct file extension for a Python source file is ".py". However, the extension of python notebook such as jupyter notebook is ".ipynb"

##### 5. Is Python code compiled or Interpreted?
>Python code is interpreted, not compiled. The Python interpreter reads and executes the source code line by line, rather than compiling it into machine code and executing the compiled code.

##### 6. Name a few blocks of code used to define in Python language?
>In Python, blocks of code are defined using indentation. Some of the blocks of code used in Python include:
> - Conditional statements: "if", "elif", and "else" statements
> - Functions: defined using the "def" keyword
> - Loops: "for" and "while" loops
> - Classes: defined using the "class" keyword

##### 7. State a character used to give single- line comments in Python?
>In Python, the symbol "#" is used to give single-line comments. Everything to the right of a "#" symbol in a line of code is ignored by the Python interpreter and is only there for human readability. For example:
> 
> ```
>   # This is a single-line comment in Python
>   x = 42 # This is also a comment, inline with codeS
>```

##### 8. Mention functions which can heip us to find the version of python that we are currently working on
>There are several built-in functions in Python that can be used to determine the version of Python you are working with:
>
>1. sys.version: This returns a string containing the version information of the Python interpreter.
>2. sys.version_info: This returns a named tuple of version information about the Python interpreter.
>3. platform.python_version(): This returns a string that contains the version of the Python interpreter you are using.

##### 9. Python supports the creation of anonymous functions at runtime, using a construct called
>"lambda". The lambda keyword is used to create anonymous functions, which are functions without a name. These functions can have any number of arguments, but can only have one expression. The expression is evaluated and returned when the function is called.
>
>Lambda functions are useful when you need to pass a small function as an argument to another function, or when you need to define a function in a single line. Here's an example:
>
>
>``` 
>    # A simple lambda function to add two numbers
>    add = lambda x, y: x + y
>    print(add(3, 4)) # Output: 7S
>```

##### 10. What does pip stand for python?
>"pip" stands for "Pip Installs Packages". It is a package management system used to install and manage packages for the Python programming language. It makes it easy to install, upgrade, and remove Python packages, and it can be used to search for and download packages from the Python Package Index (PyPI).
>
>it can be used from the command line by typing "pip" followed by the desired command. For example, to install a package, you would run `pip install <package_name>`.

##### 11. Mention a few built- in functions in python?
>Here are some of the most commonly used built-in functions in Python:
>
>1. `print()`: used to display output on the screen.
>2. `len()`: returns the length of an object (such as a string, list, or tuple).
>3. `str()`: converts a value to a string.

##### 12. What is the maximum possible length of an identifier in Python?
>There is no specific limit to the length of an identifier in Python. However, it is recommended to keep identifiers short and descriptive for the sake of code readability. In practice, the maximum length of an identifier is determined by the amount of memory available to the Python interpreter. In general, we should avoid using extremely long identifier names, as they can make the code difficult to read and maintain.

##### 13. What are the benefits of using Python?
>There are several benefits of using Python as a programming language:
>
>1.Easy to learn and use: Python has a simple and straightforward syntax, which makes it easy to learn and use, even for people who have no prior programming experience.
>
>2. Versatile: Python is a general-purpose programming language, which means it can be used for a wide range of applications, including web development, scientific computing, data analysis, artificial intelligence, and more.
>
>3. Large community and ecosystem: Python has a large and active community of developers, who have created a wealth of libraries and tools that make it easier to build and deploy applications.
>
>4. Interoperability: Python can be easily integrated with other programming languages and tools, which makes it a good choice for projects that need to integrate with existing systems.
>
>5. High-level language: Python is a high-level language, which means that it provides a high level of abstraction from the underlying hardware and operating system. This makes it easier to write code that is portable and reusable.
>
>6. Readable and maintainable code: Python has a clear and concise syntax, which makes it easier to write and maintain code, even for complex projects.
>
>7. Dynamic and interpreted: Python is a dynamically-typed and interpreted language, which means that you can test and run your code incrementally, without having to compile the entire program.

##### 14. How is memory managed in Python?
>In Python, memory management is handled by the Python memory manager, which is responsible for allocating and freeing memory. The memory manager is part of the Python interpreter, and it automatically manages the memory used by Python objects.
>
>Python uses a garbage collector to automatically track and reclaim objects that are no longer being used. This makes it easy to write Python code that is free of memory leaks, and it reduces the risk of bugs related to memory allocation and deallocation.
>
>Python also provides several built-in tools for managing memory more explicitly, such as the del statement, which can be used to explicitly remove an object and free up its memory.
>
>Overall, Python's memory management is designed to be simple, efficient, and transparent to the programmer. This makes it a good choice for projects that require efficient and reliable memory management.

##### 15. How to install Python on Windows and set path variables?
>Here are the steps to install Python on Windows and set the path variables:
>
>1. Download the Python installer: Go to the official Python website (https://www.python.org/downloads/) and download the latest version of Python for Windows.
>
>2. Run the installer: Double-click the installer file that you downloaded and follow the instructions to install Python. Make sure to select the option to "Add Python to PATH" during the installation process.
>
>3. Verify the installation: Open a Command Prompt window and type python. If the installation was successful, you should see the Python prompt, which indicates that Python is installed and ready to use.
>
>4. Set the path variables: If the "Add Python to PATH" option was not selected during the installation, you will need to set the path variables manually. To do this, open the System Properties, go to the Advanced System Settings, and click the Environment Variables button. Under System Variables, find the Path variable, and click the Edit button. Add the location of the Python executable to the Path variable (e.g., C:\Python36).
>
>After completing these steps, Python should be installed and ready to use on your Windows machine. You should also be able to run Python scripts and use Python modules by simply typing python followed by the script name at the Command Prompt.

##### 16. Is indentation required in python?
>Yes, indentation is required in Python to define code blocks and control structures such as loops and functions. In Python, indentation is used instead of brackets or keywords to define code blocks, and it is important to ensure that your code is properly indented in order to avoid syntax errors.
