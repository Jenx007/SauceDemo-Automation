# SauceDemo-Automation

# Project Overview
This project automates interactions with the [Sauce Demo](https://www.saucedemo.com/) website using Selenium. The script logs into the site, extracts product details, updates product information, and integrates with an external API to retrieve additional data. All actions are organized within a modular class structure.

# Features
- Automated Login: Logs into Sauce Demo using credentials stored in a JSON file.
- Product Extraction: Retrieves all product details (title, description, and price) and saves them to a JSON file.
- Data Update: Updates the price of the third product to $100 within the JSON file.
- API Integration: Makes an API call to JSON Placeholder to retrieve a title and save it in a separate JSON file.

# Project Structure
- `credentials.json`: Stores login credentials (username and password).
- `product_details.json`: Contains details of all products extracted from the site.
- `post_title.json`: Stores the title retrieved from the external API.
- `Main.py`: Main script implementing the automation in a modular class structure.

# Prerequisites
- **Python**: Python 3.x is required.
- **ChromeDriver**: Ensure ChromeDriver is installed and accessible from your system's PATH.
- **Libraries**:
  - `selenium`
  - `requests`
  - `json`


