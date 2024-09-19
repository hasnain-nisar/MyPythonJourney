'''
Explore the 'Flask' module and create a web server using Flask & Python.
'''

from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return "Hello, World!"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
