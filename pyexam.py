import web grabber and html parser
import gspread
import requests as web
from bs4 import BeautifulSoup as soup
import pandas as pd
import mysql.connector



# TASK 1
# i assign hello string to variable text and i to value of 1
text = "Hello"
i = 1
# added if statement if i is greater than 0 and
if i > 0:
    # the string value of text will be reverse and will be the new value of new variable reverse
    reverse = text[::-1]
    # this will print the reverse variable
    print(reverse)
# TASK 2
numbers = [5, 2, 8, 10, 1]
# created set from numbers
new_numbers = set(numbers)
# remove highest number from new_numbers
new_numbers.remove(max(new_numbers))
# prints the new highest number from new_numbers
print(max(new_numbers))

# TASK 3
list1 = [1, 2, 3, 2, 4, 1, 5, 4]
# Removing duplicates from the list
list2 = list(set(list1))
# Printing the value of list2
print(list2)

# TASK 4
# variable with the value of website link
response = web.get("http://books.toscrape.com/")
html = response.text

# calling BeautifulSoup for parsing the website
web_page = soup(html, "html.parser")
response.close()

# finding all and grabbing them all using html tag
all_books = web_page.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

for x in all_books:
    # collecting all book title
    Title = x.h3.a["title"]

    # collecting all book Author
    Author = x.h3.a["title"]

    # Availability
    Availability = x.h3.a["title"]

    # collect book price of all books
    price = x.find_all("p", {"class": "price_color"})
    Price = price[0].text.strip()

    Availability = x.find_all("p", {"class": "instock availability"})
    Availability = Availability[0].text.strip()

    print("Title of the book :" + Title)
    print("Price :" + Price)
    print("Author :" + Price)
    print("Availability :" + Availability)
    
    
response2 = web.get("https://infinite-scroll.com/demo/full-page/page3")
html2 = response2.text

# calling BeautifulSoup for parsing the website
web_page2 = soup(html, "html.parser")
response2.close()


all_titles = web_page2.find_all('h2', class_='entry-title')


filename2 = "data.csv"
f = open(filename2, "w")

headers2 = "Titles\n"
f.write(headers2)

for i in all_titles:
    # collecting all book title
    Title = i.find_all("h2", {"class": "entry-title"})
    
    print("Title :" + Title)
    
    f.write(Title)
f.close()


# Task 6


# TASK 7
# database connection
db = mysql.connector.connect(
    host="localhost", user="root", password="", database="mydatabase"
)

# created cursor object
mycursor = db.cursor()

# filter all customers who not place a order
mycursor.execute(
    "SELECT customers.customer_id, customers.customer_name FROM customers LEFT JOIN orders ON customers.customer_id = orders.customer_id WHERE orders.customer_id IS NULL"
)
not_placed_order = mycursor.fetchall()
a = "customer_id"
b = "customer_name"

for x in not_placed_order:
    a = x[0]
    b = x[1]
    print(a, b)
    
    
    
#Task 11: Google Sheets Automation


account = gspread.service_account(filename='pytechxam.json')
googlesheet = account.open('pytechxamsheet').sheet1



csv_file_path = 'data.csv'

 Load CSV data using pandas
csv_data = pd.read_csv(csv_file_path)


 Open the spreadsheet by name

 Select the first sheet
sheet = googlesheet.get_worksheet(0)

 Get the titles from the CSV data
titles = csv_data['title']

Append titles as new rows
for title in titles:
    sheet.append_row([title])
    print(title)
