import bcrypt


# Generate a salt
salt = bcrypt.gensalt()

# Hash the password
password = 'allaolsmdjdndjdjd'
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

# Verify the password
entered_password = 'allaolsmdjdndjdjd'
if bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password):
    # Passwords match
    print('Authentication successful')
else:
    # Passwords do not match
    print('Authentication failed')
