     # Import the Flask and OS Python modules
from flask import Flask, render_template, request, redirect, url_for
import os

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return render_template('Registration.html')

# Route to handle registration form submission
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':  # Check if the form was submitted
        name = request.form['name']  # Get name from form
        email = request.form['email']  # Get email from form
        password = request.form['password']  # Get password from form

        # Normally, you would store user data in a database or a file here
        # For now, we'll just render a success page
        return render_template('Success.html', name=name)

    return redirect(url_for('home'))  # In case of GET request, redirect to home

# Running the Flask app
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Get port from environment variable or default to 5000
    app.run(debug=True, host='0.0.0.0', port=port)
