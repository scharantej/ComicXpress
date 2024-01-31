## Flask Application Design for Comic Book Selling Website

### HTML Files

**1. home.html:**
- This file will serve as the landing page for the website, providing an overview of the comic books available for sale, along with links to explore different sections of the website.
- Content may include:
  - Welcome message and a brief introduction to the comic book store.
  - Featured comic books with images, titles, and short descriptions.
  - Navigation bar with links to other HTML files (e.g., catalog, about us, contact us).

**2. catalog.html:**
- This file will display the complete catalog of comic books available for purchase.
- Content may include:
  - A list of comic book categories (e.g., superheroes, sci-fi, horror) with links to filter the catalog accordingly.
  - Display comic book titles, authors, prices, and brief descriptions.
  - Allow users to add comic books to their shopping cart.

**3. about_us.html:**
- This file will provide information about the comic book store, its history, mission, and team members.
- Content may include:
  - Store's origin story, values, and commitment to customers.
  - Team members' profiles, including photos, names, and brief bios.
  - Contact information and social media links.

**4. contact_us.html:**
- This file will enable users to get in touch with the comic book store.
- Content may include:
  - Contact form with fields for name, email, phone number, and message.
  - Store's address, phone number, and email address.
  - Map or directions to the store's physical location.

### Routes

**1. Home:**
- Route: `/`
- Purpose: Displays the home page HTML file.

**2. Catalog:**
- Route: `/catalog`
- Purpose: Displays the catalog HTML file, showcasing all comic books for sale.

**3. About Us:**
- Route: `/about_us`
- Purpose: Displays the about us HTML file, providing information about the comic book store.

**4. Contact Us:**
- Route: `/contact_us`
- Purpose: Displays the contact us HTML file, allowing users to send inquiries to the comic book store.

**5. Add to Cart:**
- Route: `/add_to_cart/<comic_id>`
- Purpose: Handles the addition of a specific comic book to the user's shopping cart.

**6. View Cart:**
- Route: `/view_cart`
- Purpose: Displays the user's shopping cart, showing the selected comic books, quantity, and total cost.

**7. Checkout:**
- Route: `/checkout`
- Purpose: Initiates the checkout process, allowing users to provide their shipping and payment information to complete the purchase.

**8. Order Confirmation:**
- Route: `/order_confirmation`
- Purpose: Displays a confirmation page after a successful purchase, providing order details and a thank you message.