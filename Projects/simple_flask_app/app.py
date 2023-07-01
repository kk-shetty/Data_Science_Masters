from flask import Flask, request, render_template, jsonify, redirect, session
from db_ops import check_user, extract_pswd, extract_user_details, insert_record
from authentication import hash_password, validate_password

app = Flask(__name__)
app.secret_key = 'your-secret-key' #initiate the session and configure the secret key for session encryption and decryption. 

@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/login")
def login():
    render_message = request.args.get('message')
    error_message = request.args.get('error')
    return render_template('login.html', message = render_message, login_error = error_message)

@app.route("/signup")
def signup():
    error_message = request.args.get('error')
    return render_template('signup.html', signup_error = error_message)

@app.route("/user_home")
def user_home():
    return render_template('user_home.html', username = session['first_name'] + session['last_name'], state = session['state'] , city = session['city'])

@app.route("/validate_login", methods=['POST'])
def validate_login():
    if(request.method == 'POST'):
        email = request.form['email']
        pswd = request.form['pswd']
        if check_user(email):
            hash_pswd = extract_pswd(email)
            if validate_password(pswd, hash_pswd):
                session['first_name'], session['last_name'], session['state'], session['city'] = extract_user_details(email)
                return redirect('/user_home')
                # return render_template('user_home.html', username = username, state = state, city = city)
            else:
                # return render_template('login.html', login_error= "Invalid Email ID or Password. Please try Again.")
                render_message = "Invalid Email ID or Password. Please try Again."
                return redirect('/login?error=' + render_message)
        else:
            # return render_template('login.html', login_error= "User Doesn't Exist.")
            render_message = "User Doesn't Exist."
            return redirect('/login?error=' + render_message)
    else:
        # return render_template('login.html', login_error= "!Unknown Error!")
        render_message = "!Unknown Error!"
        return redirect('/login?error=' + render_message)

@app.route("/validate_signup", methods=['POST'])
def validate_signup():
    if(request.method == 'POST'):
        email = request.form['email']

        if check_user(email):
            # return render_template('login.html', redirect_message = "User Email ID already registered. Please login with same.")
            render_message = "User Email ID already registered. Please login with same."
            return redirect('/signup?error=' + render_message)
        else:
            hash_pswd = hash_password(request.form['password'])
            user_credential = {
                'email' : email,
                'password' : hash_pswd
            }
            insert_record(user_credential, 'login_credentials')
            user_detail = {
                'email' : email,
                'first_name' : request.form['first-name'],
                'last_name' : request.form['last-name'],
                'state' : request.form['state'],
                'city' : request.form['city']
            }
            insert_record(user_detail, 'user_details')
            render_message = "User created successfully. Please Login"
            return redirect('/login?message=' + render_message)
            # return render_template('login.html', redirect_message = "User Created Succesfully. Please login.")
    render_message = "Error creating user. Please try again."
    return redirect('/signup?error=' + render_message)
    # return render_template('signup.html', signup_error = "Error creating user. Please try again.")

if __name__ == '__main__':
    app.run(host="0.0.0.0")