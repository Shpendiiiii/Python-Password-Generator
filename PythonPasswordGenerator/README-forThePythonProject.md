# Quotable API Quote Generator

A simple Python script to generate random quotes from the Quotable API

## **Getting started**
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### **Prerequisites**
You will need to have Python 3 and the requests library installed on your machine.

### **Installing**

To install the requests library, you can use the following command in your terminal:
* pip install requests

### **Running the script**
Clone or download this repository and navigate to the directory in your terminal. Run the script using the following command:
* python quote_generator.py

## Built With
* Python 3
* Requests library
* Json library
* Quotable API
<br><br><br>
## Deatiled explanation of the code
This is a basic Python script that allows you to generate random quotes using the Quotable API (apiUrl = "https://api.quotable.io/").

When the script runs, it prompts the user to enter either "r" for a random quote or "c" to see the categories.

If the user enters "r", the script sends a GET request to the Quotable API endpoint for a random quote (apiUrl += "random"), and if the response is successful (response.status_code == requests.codes.ok), it prints the content of the quote.

If the user enters "c", the script sends a GET request to the Quotable API endpoint for categories (apiUrl += 'tags'), and if the response is successful, it prints the list of categories. The user is then prompted to enter the name of the desired category. The script then sends a GET request to the Quotable API endpoint for a random quote from the chosen category (catApiUrl = f"https://api.quotable.io/random?tags={userInputCat}"), and if the response is successful, it prints the content of the quote.

In the case of any error, the script prints the error code and message.