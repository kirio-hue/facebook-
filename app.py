# app = Flask(__name__) 

# # Initialize a connection to the SQLite database
# conn = sqlite3.connect('users.db')
# from flask import Flask #type: ignore

# from flask import request
# # The rest of your app.py code

# c = conn.cursor()

# # Create the users table if it doesn't exist
# c.execute('''CREATE TABLE IF NOT EXISTS users
#              (email text, password text)''')

# @app.route('/receive_login', methods=['POST'])
# def receive_login():
#     # Get the email and password from the request
#     email = request.form['email']
#     password = request.form['password']

#     # Store the user data in the SQLite database
#     c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
#     conn.commit()

#     # Return the user data as a JSON object
#     return jsonify({'email': email, 'password': password})

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize a connection to the SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (email text, password text)''')

@app.route('/receive_login', methods=['POST'])
def receive_login():
    # Get the email and password from the request
    email = request.form['email']
    password = request.form['password']

    # Store the user data in the SQLite database
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()

    # Return the user data as a JSON object
    return jsonify({'email': email, 'password': password})

if __name__ == '__main__':
    app.run(debug=True)
