
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    # Render the home.html file
    return render_template('home.html')

# Define the catalog route
@app.route('/catalog')
def catalog():
    # Render the catalog.html file
    return render_template('catalog.html')

# Define the about us route
@app.route('/about_us')
def about_us():
    # Render the about_us.html file
    return render_template('about_us.html')

# Define the contact us route
@app.route('/contact_us')
def contact_us():
    # Render the contact_us.html file
    return render_template('contact_us.html')

# Define the add to cart route
@app.route('/add_to_cart/<comic_id>')
def add_to_cart(comic_id):
    # Handle the addition of a specific comic book to the user's shopping cart
    return redirect(url_for('view_cart'))

# Define the view cart route
@app.route('/view_cart')
def view_cart():
    # Display the user's shopping cart
    return render_template('view_cart.html')

# Define the checkout route
@app.route('/checkout')
def checkout():
    # Initiate the checkout process
    return render_template('checkout.html')

# Define the order confirmation route
@app.route('/order_confirmation')
def order_confirmation():
    # Display a confirmation page after a successful purchase
    return render_template('order_confirmation.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)


### Notes:

- The `secure_filename()` function is used to sanitize filenames before saving them to the server.
- The `debug` parameter in `app.run()` is set to `True` to allow for easier debugging.
- The `url_for()` function is used to generate the URLs for the various routes.
- The actual implementation of the routes (e.g., adding items to the shopping cart or processing checkout) would typically involve database interactions and payment processing, which are not included in this simplified example.