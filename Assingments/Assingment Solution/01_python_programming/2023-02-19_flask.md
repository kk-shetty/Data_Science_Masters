#### Q1. <span style="color:magenta">What is Flask Framework? What are the advantages of Flask Framework?</span>
* **Flask Framework**
	Flask is a micro web framework for building web applications in Python known for its simplicity, flexibility, and minimalistic design. Micro-framework are normally framework with little to no dependencies to external libraries.

* **Advantages of Flask Framework**
1. *Lightweight and Easy to Use*: Flask is a lightweight framework with a simple and intuitive interface. It has a small core and modular design, allowing developers to choose the components they need. It is easy to understand and quick to get started with, making it ideal for beginners and small projects.
2. *Flexibility*: Flask provides great flexibility in terms of how you structure your application. It doesn't impose any specific project layout or database abstraction layer, giving you the freedom to use different libraries and tools according to your requirements.
3. *Extensibility*: Flask is highly extensible, thanks to its modular design. It supports a wide range of extensions that integrate seamlessly with the framework, providing additional functionality such as database integration, form validation, authentication, and more. These extensions allow you to add features as needed, without bloating your application.
4. *Built-in Development Server*: Flask comes with a built-in development server, which makes it easy to test and debug your application during the development phase. It provides a simple command-line interface to start the server, making the development process smoother and more efficient.
5. *Pythonic and Minimalistic*: Flask follows the Python philosophy of being "Pythonic" and emphasizes simplicity. It provides a minimalistic and straightforward approach to web development, focusing on writing clean and readable code. This makes it easier to understand and maintain Flask applications.
6. *Large Community and Active Ecosystem*: Flask has a large and active community of developers who contribute to its growth. This means you can find plenty of resources, tutorials, and third-party extensions to help you with your Flask projects. The extensive ecosystem ensures that you can find solutions to common problems and easily integrate with other tools and libraries.
7. *Well-Documented*: Flask has excellent documentation, which is one of its strengths. The official documentation is comprehensive, providing detailed explanations, examples, and code snippets. This makes it easier for developers to understand and use the framework effectively.
Overall, Flask's advantages lie in its simplicity, flexibility, extensibility, and the vibrant community surrounding it. These qualities make it a popular choice for building web applications, especially when you want a lightweight and customizable framework.

___

#### Q2. <span style="color:magenta">Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in Jupyter Notebook.</span>
```python
from flask import Flask

app = Flask(__name__)

@app.route("/") # "/" WIll be the route for home location.
def hello_world():
    return "Hello World!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
```
![HelloWorld!!](/Assingments/Assingment%20Solution/screenshots/hello_world.png)  

___

#### Q3. <span style="color:magenta">What is App routing in Flask? Why do we use app routes?</span>
In Flask, **app routing** refers to the process of mapping URLs to specific functions or view handlers in our web application. It allows us to define different routes or endpoints for our application, specifying what function should be executed when a particular URL is requested.

**App routes** are used in Flask to define the behavior of our web application and determine how it responds to different HTTP requests. Here's why we use app routes:
1. *URL Mapping*: App routes provide a way to map specific URLs to the corresponding functions in our Flask application. When a client sends a request to a particular URL, Flask matches the URL to the appropriate route and executes the associated function. This allows us to define the structure and behavior of our application's different pages or resources.

2. *Handling HTTP Methods*: App routes also handle different HTTP methods, such as GET, POST, PUT, DELETE, etc. By specifying the HTTP methods allowed for a route, we can define how our application responds to different types of requests. For example, we can use a GET route to fetch data, a POST route to submit data, and so on.

3. *Dynamic Routing*: Flask app routes support dynamic routing, where parts of the URL can be variable. We can define route patterns that include variables and capture those values to use within our view functions. This enables us to create dynamic URLs that can handle different parameters, such as user IDs, article slugs, or any other variable data.

4. *RESTful APIs*: If we're building a RESTful API with Flask, app routes are crucial. Each route can correspond to a specific API endpoint, defining the resources and operations available through the API. By using different routes, we can design a clear and structured API that follows the principles of REST.

5. *Code Organization*: App routes help in organizing our code by providing a clear separation of concerns. By mapping URLs to specific functions, we can easily locate and manage the logic related to different routes. This promotes modularity and maintainability in our Flask application.

Overall, app routes in Flask are essential for defining the URLs and associated functions that handle the various requests in your web application. They allow you to create a structured and organized codebase, handle different HTTP methods, support dynamic routing, and build RESTful APIs.

___

#### Q4. <span style="color:magenta">Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/” route to show the following details:</span>

* <span style="color:magenta">Company Name: ABC Corporation</span>
* <span style="color:magenta">Location: India</span>
* <span style="color:magenta">Contact Detail: 999-999-9999</span>

```python
from flask import Flask

app = Flask(__name__)

@app.route("/") # "/" WIll be the route for home location.
def home():
    company_name = "ABC Corporation"
    location = "India"
    contact_detail = "999-999-9999"
    
    return f"Company Name: {company_name}<br>Location: {location}<br>Contact Detail: {contact_detail}"

@app.route("/welcome")
def welcome():
    return "Welcome to ABC Corporation"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
```
![company1](/Assingments/Assingment%20Solution/screenshots/home_path_route_company.png)  
![company2](/Assingments/Assingment%20Solution/screenshots/welcome.png)  

___

#### Q5. <span style="color:magenta">What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the url_for() function.</span>

In Flask, the `url_for()` function is used for URL building. It generates a URL for a specified endpoint, allowing you to dynamically create URLs based on the view functions or routes defined in your application. This function takes the endpoint name as its first argument and can accept additional arguments to build URLs with variables.

```python
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/about')
def about():
    return 'This is the About Page.'

@app.route('/user/<username>')
def profile(username):
    return f'Hello, {username}!'

@app.route('/contact')
def contact():
    return 'Contact us at: contact@example.com'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
```

In the html part, the `url_for` is used like below
```html
<a href="{{ url_for('karthik') }}">Karthik</a>
```

![DynamicURL](/Assingments/Assingment%20Solution/screenshots/dynamic_url.png)  

___