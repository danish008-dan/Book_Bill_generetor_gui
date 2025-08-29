# Book_Bill_generetor_gui
This is a Book Store Billing Application built with Python Tkinter (GUI) and MySQL.

📌 Overview

This is a Book Store Billing Application built with Python Tkinter (GUI) and MySQL.
It provides two roles:

Owner → Can add new books and view all available books.

Buyer → Can purchase books by entering name & quantity, and generate a bill with total amount.

This project demonstrates Python GUI development, CRUD operations, and database integration.

🚀 Features

✔ Owner can add books with price
✔ Owner can view all available books in the store
✔ Buyer can select a book and quantity to generate a detailed bill
✔ Interactive Tkinter-based GUI
✔ MySQL database integration for storing book details

📂 Project Structure
BookStore-Bill-Generator/
│── book_store_app.py     # Main Python file (Tkinter GUI + logic)
│── README.md             # Documentation
│── book_store.sql        # Database schema + sample data

🗄️ Database Setup

Create Database

CREATE DATABASE book_store;
USE book_store;


Create Table

CREATE TABLE book_price (
    book_name VARCHAR(100) PRIMARY KEY,
    book_price_per_unit DECIMAL(10,2) NOT NULL
);


Insert Sample Data

INSERT INTO book_price (book_name, book_price_per_unit) VALUES
('Atomic Habits', 450.00),
('Rich Dad Poor Dad', 400.00),
('The Power of Subconscious Mind', 350.00),
('Sukoon', 300.00),
('Peer-e-Kamil', 399.00),
('Ikigai', 320.00),
('Think and Grow Rich', 370.00),
('Do Epic Shit', 280.00),
('Deep Work', 450.00),
('Wings of Fire', 300.00),
('The Mindset', 349.00),
('Can''t Hurt Me', 749.00);

🔧 Installation & Usage

Clone the repository

git clone https://github.com/<your-username>/bookstore-bill-generator.git
cd bookstore-bill-generator


Install required dependencies

pip install pymysql


Run the application

python book_store_app.py

🖥️ Example Workflow
Owner

Add new book with price

View all available books

Buyer

Enter book name and quantity

Bill is generated with total amount

Example Bill Output:

Your Bill Summary:
-------------------------
Book Name     : Atomic Habits
Quantity      : 2
Price per unit: ₹450.00
Total Amount  : ₹900.00
-------------------------
Thank you for shopping!

📚 Future Enhancements

Add multiple book purchase in a single bill

Owner authentication (login system)

Export bill to PDF or print option

Search books by category/author
