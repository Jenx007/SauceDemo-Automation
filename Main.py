import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

class WebBot:
    def __init__(self, credentials_file):
        """Start the bot with login file."""
        self.credentials_file = credentials_file
        self.driver = webdriver.Chrome()
        self.product_details = {}  # Store product info

    def get_login_details(self):
        """Getting username and password"""
        try:
            with open(self.credentials_file, "r") as file:
                data = json.load(file)
            self.user = data["username"]
            self.pwd = data["password"]
        except FileNotFoundError:
            print("credentials.json file not found.")
            raise

    def login(self):
        """login to site."""
        try:
            url = "https://www.saucedemo.com/"
            self.driver.get(url)
            self.driver.find_element(By.ID, "user-name").send_keys(self.user)
            self.driver.find_element(By.ID, "password").send_keys(self.pwd)
            self.driver.find_element(By.ID, "login-button").click()
            print("Logged in successfully")
        except Exception as e:
            print("Error occurred during login:", e)
            raise

    def get_product_details(self):
        """Get all product details from site."""
        try:
            # Wait for page to load
            time.sleep(3)
            # Get all products
            products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            assert len(products) > 0, "No products found on the page."

            # Save each product's info
            for product in products:
                title = product.find_element(By.CLASS_NAME, "inventory_item_name").text
                description = product.find_element(By.CLASS_NAME, "inventory_item_desc").text
                price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
            #Store each product details in the dictionary
                self.product_details[title] = {
                    "description": description,
                    "price": price
                }
            # save to JSON file
            with open("product_details.json", "w") as file:
                json.dump(self.product_details, file, indent=4)
            print("Product details saved to product_details.json")
        except Exception as e:
            print("Error occurred while getting product details:", e)
            raise

    def update_price(self):
        """Update 3rd item price to $100."""
        try:
            # List of products
            names = list(self.product_details.keys())
            assert len(names) >= 3, "Not enough products found to update the 3rd item price."
            # Change price of third item
            third_item = names[2]
            self.product_details[third_item]["price"] = "$100.00"

            # Save changes
            with open("product_details.json", "w") as file:
                json.dump(self.product_details, file, indent=2)
            print("Updated the price of the 3rd product to $100")
        except Exception as e:
            print("Error occurred while updating the price:", e)
            raise

    def get_title(self):
        """Make API call to get a post title."""
        try:
            url = "https://jsonplaceholder.typicode.com/posts/1"
            response = requests.get(url)
            assert response.status_code == 200, "API request failed."
            post_data = response.json()
            post_title = post_data["title"]

            # Save the title
            with open("post_title.json", "w") as file:
                json.dump({"title": post_title}, file, indent=4)
            print("Saved a post title to post_title.json")
        except Exception as e:
            print("Error occurred while getting the post title:", e)
            raise

    def exit_browser(self):
        """Closes browser."""
        try:
            self.driver.quit()
            print("Process completed!")
        except Exception as e:
            print("Error occurred while closing the browser:", e)

# main func
if __name__ == "__main__":
    bot = WebBot("credentials.json")

    try:
        # Run all steps
        bot.get_login_details()      
        bot.login()                  
        bot.get_product_details()   
        bot.update_price()           
        bot.get_title()              
        bot.exit_browser()  
    except Exception as e:
        print("An error occurred during the execution:", e)