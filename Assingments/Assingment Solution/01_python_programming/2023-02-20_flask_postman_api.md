#### <span style="color:magenta"> Q1. Explain GET and POST methods.</span>

GET and POST are two commonly used HTTP methods in web development for communication between clients (such as web browsers or mobile apps) and servers. 

* **GET Method**

GET is used to request data from a specified resource. It can retrieve any visible data to a client, such as HTML documents, images, and videos:
To send a GET request, a client needs to specify the URL of the resource it wants to retrieve. The request is then sent to the server, which processes the request and sends the requested data back to the client.

* **POST Method**

The POST sends data to a server to create or update a resource. For example, it is often used to submit an HTML form to a server:
To send a POST request, a client needs to specify the URL of the resource to which it wants to send data and the data itself. The request is then sent to the server, which processes the request and sends a response back to the client.
The POST method is often used to submit forms or upload files to a server.

These are the main difference between them:

1. *Visibility* - When using GET, data parameters are included in the URL and visible to everyone. However, when using POST, data is not displayed in the URL but in the HTTP message body.

2. *Security* - GET is less secure because the URL contains part of the data sent. On the other hand, POST is safer because the parameters are not stored in web server logs or the browser history.

3. *Cache* - GET requests can be cached and remain in the browser history, while POST requests cannot. This means GET requests can be bookmarked, shared, and revisited, while POST requests cannot.

4. *Server State* - GET requests are intended to retrieve data from a server and do not modify the server’s state. On the other hand, POST requests are used to send data to the server for processing and may modify the server’s state.

5. *Amount of Data* - The GET method is limited to a maximum number of characters, while the POST method has no such limitation. This is because the GET method sends data through the resource URL, which is limited in length, while the POST method sends data through the HTTP message body, which has no such limitation.

6. *Data Type* - The GET method supports only string data types, while the POST method supports different data types such as string, numeric, binary, and so on.
___

#### <span style="color:magenta"> Q2. Why is request used in Flask?</span>

* The `request` object in Flask is a crucial component that allows us to access incoming client requests made to our Flask application. It provides a way to retrieve and manipulate data sent by clients in the form of *HTTP requests*.

* The request object provides methods and attributes to access various aspects of the incoming request. We can retrieve data from the request's URL parameters, headers, form data, cookies, and more.

* The request object allows us to handle different HTTP methods (such as GET, POST, PUT, DELETE) used by clients to interact with our Flask application. It provides attributes like `request.method` to determine the current HTTP method used in the request, allowing us to customize our application's behavior accordingly.

* request object supports handling file uploads. We can access uploaded files using the request.files attribute and perform operations like saving the file to the server or processing its contents.
___

#### <span style="color:magenta"> Q3. Why is redirect() used in Flask?</span>

* The `redirect()` function in Flask is used to perform a redirect from one URL to another. It is a convenient way to redirect clients to a different route or external URL in response to a request.

* When a client sends a request to a specific route in our Flask application, we may want to redirect them to a different route. This can be useful for handling specific conditions or implementing URL routing logic. For example, after processing a form submission on one route, we may want to redirect the user to a different page to display the result or prevent form resubmission.

* Flask's redirect() function also allows us to perform URL generation dynamically. Instead of hard-coding URLs in your application, we can use Flask's route names and URL rules to generate URLs dynamically and pass them as arguments to redirect(). This makes our application more flexible and helps avoid issues with maintaining hardcoded URLs.
___

#### <span style="color:magenta"> Q4. What are templates in Flask? Why is the render_template() function used?</span>

##### In Flask, templates are files that contain the structure and layout of our web pages. They allow us to separate the presentation logic from the application logic, making it easier to manage and modify the user interface of our Flask application.
##### Templates allow us to define the structure, layout, and placeholders for dynamic content in our web pages. By using templates, we can maintain a consistent design across our application and reuse common elements (such as headers, footers, navigation menus) across multiple pages.

##### The `render_template()` function is a built-in function in Flask that is used to render templates and generate HTML content dynamically. The `render_template()` function is used to render these templates and generate the final HTML content to be sent back to the client.
___

#### <span style="color:magenta"> Q5. Create a simple API. Use Postman to test it.</span>

```python
# pip install flask

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/age_cal', methods = ['POST'])
def test_api():
    if request.method == 'POST':

        name = request.json['name']
        yob = int(request.json['year'])

        if yob > datetime.now().year:
            result = "Error, year of birth cannot be higher than current year"
        else:
            age = datetime.now().year - yob
            result = f"Hi, {name} 👋!! You are {age} years old"
        
        return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
```
![postman_api](/Assingments/Assingment%20Solution/screenshots/postman_api_testing.png) 
___