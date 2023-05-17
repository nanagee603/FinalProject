from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    return render_template('home.html')

# Define the food ordering page route
@app.route('/order')
def order():
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
            CREATE TABLE IF NOT EXISTS food_orders (
                id INT PRIMARY KEY AUTO_INCREMENT,
                student_name VARCHAR(255),
                food_item VARCHAR(255),
                restaurant_name VARCHAR(255),
                location VARCHAR(255)
            )
        """)

    return render_template('order.html')

# Define the information page route
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

        # Execute a SELECT query to fetch the restaurants data
        cur.execute("SELECT restaurant_name, location FROM restaurants")

        # Fetch all the rows from the result set
        restaurants = cur.fetchall()

    return render_template('information.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run()

