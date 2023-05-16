from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    return render_template('home.html')

# Define the employee registration page route
@app.route('/registration')
def registration():
    return render_template('registration.html')

# Define the employee information page route
@app.route('/information')
def information():
    # Establish a connection to the MySQL database
    with mysql.connector.connect(
        host="localhost",
        user="flask",
        password="ubuntu",
        database="flask_db"
    ) as con:
        # Create a cursor object to execute SQL queries
        cur = con.cursor()
        
        # Create a table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT PRIMARY KEY,
                name VARCHAR(255),
                gender VARCHAR(255),
                phone VARCHAR(255),
                birthdate DATE
            )
        """)
        
        # Query the database to get all employees
        cur.execute("SELECT * FROM employees")
        employees = cur.fetchall()
    
    return render_template('information.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)



