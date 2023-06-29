# Importing flask library and necessary modules
from flask import Flask
from flask import request
import datetime

app = Flask(__name__)

# Decorating a simple mfunction with flask route
@app.route("/") # "/" WIll be the route for home location.
def home():
    '''This function is at the home route. So this can be access with 'https://<app.public_url>/:5000'
    '''
    company_name = "ABC Corporation"
    location = "India"
    contact_detail = "999-999-9999"
    
    return f"Company Name: {company_name}<br>Location: {location}<br>Contact Detail: {contact_detail}"


@app.route("/sysdate")
def get_date():
    '''This function will return current system date when called 'https://<app.public_url>/:5000/date'
    '''
    return str(datetime.date.today())

@app.route("/input_url")
def user_input():
    user_input = request.args.get('x')
    return f"User input - {user_input}"

@app.route("/welcome")
def welcome():
    return "Welcome to ABC Corporation"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
