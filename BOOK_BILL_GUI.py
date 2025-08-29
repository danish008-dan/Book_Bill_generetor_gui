#6 PROJECT GUI book  BILL GENERATOR

from tkinter import *
import pymysql

root = Tk()
root.title("Danish Book Depo")
root.geometry("400x300")
root.configure(bg="#fff8e7")


def open_owner_window():
    owner = Toplevel()
    owner.title("Danish Khatri")
    owner.geometry("450x400")
    owner.configure(bg="#e6f7ff")

    l1 = Label(owner, text="Danish Khatri", bg="#e6f7ff")
    l1.pack(pady=10)

    box = Text(owner, width=45, height=10)
    box.pack(pady=10)

    def show_books():
        db = pymysql.connect(host="localhost", user="root", password="", database="book_store")
        cur = db.cursor()
        cur.execute("SELECT * FROM book_price")
        data = cur.fetchall()
        box.delete(1.0, END)
        box.insert(END, "Books in Store:\n")
        for row in data:
            box.insert(END, f"{row[0]} - ₹{row[1]}/unit\n")
        db.close()

    def open_add_book_window():
        add_win = Toplevel(owner)
        add_win.title("Add New Book")
        add_win.configure(bg="#f0fff0")
        add_win.minsize(300, 200)

        l1 = Label(add_win, text="Book Name:", bg="#f0fff0")
        l1.pack()
        book_name_entry = Entry(add_win)
        book_name_entry.pack(pady=5)

        l2 = Label(add_win, text="Price:", bg="#f0fff0")
        l2.pack()
        price_entry = Entry(add_win)
        price_entry.pack(pady=5)

        def add_book():
            book_name = book_name_entry.get()
            price = price_entry.get()

            if book_name == "" or price == "":
                box.insert(END, "Error: Please enter both fields\n")
            else:
                db = pymysql.connect(host="localhost", user="root", password="", database="book_store")
                cur = db.cursor()
                cur.execute("INSERT INTO book_price VALUES (%s, %s)", (book_name, price))
                db.commit()
                db.close()
                box.insert(END, f"Book '{book_name}' added successfully!\n")
                add_win.destroy()

        Button(add_win, text="Add Book", bg="green", fg="white", command=add_book).pack(pady=10)

    b1 = Button(owner, text="Add Book", bg="#2E8B57", fg="white", width=20, command=open_add_book_window)
    b1.pack(pady=5)
    b2 = Button(owner, text="Show All Books", bg="#4682B4", fg="white", width=20, command=show_books)
    b2.pack(pady=5)


def open_buyer_window():
    buyer = Toplevel()
    buyer.title("Buyer")
    buyer.geometry("400x400")
    buyer.configure(bg="#f0f0f5")

    l1 = Label(buyer, text="BUYER", bg="#f0f0f5")
    l1.pack(pady=10)

    l2 = Label(buyer, text="Enter Book Name:", bg="#f0f0f5")
    l2.pack()
    book_entry = Entry(buyer, width=30)
    book_entry.pack()

    l3 = Label(buyer, text="Enter Quantity:", bg="#f0f0f5")
    l3.pack()
    qty_entry = Entry(buyer, width=30)
    qty_entry.pack(pady=5)

    bill_box = Text(buyer, width = 45, height=6)
    bill_box.pack()

    def generate_bill():
            book = book_entry.get().strip()
            qty = qty_entry.get().strip()

            if book == "" or qty == "":
                bill_box.delete(1.0, END)
                bill_box.insert(END, "Please fill all fields.\n")
            else:
                db = pymysql.connect(host="localhost", user="root", password="", database="book_store")
                cur = db.cursor()
                cur.execute("SELECT book_price_per_unit FROM book_price WHERE book_name = %s", (book,))
                row = cur.fetchone()
                db.close()

                if row:
                    price = int(row[0])
                    quantity = int(qty)
                    total = price * quantity

                    bill_box.delete(1.0, END)
                    bill_box.insert(END, "Your Bill Summary:\n")
                    bill_box.insert(END, "-------------------------\n")
                    bill_box.insert(END, f"Book Name     : {book}\n")
                    bill_box.insert(END, f"Quantity      : {quantity}\n")
                    bill_box.insert(END, f"Price per unit: ₹{price}\n")
                    bill_box.insert(END, f"Total Amount  : ₹{total}\n")
                    bill_box.insert(END, "-------------------------\n")
                    bill_box.insert(END, "Thank you for shopping!\n")
                else:
                    bill_box.delete(1.0, END)
                    bill_box.insert(END, "Book not found.\n")

    b1 = Button(buyer, text="Generate Bill", command=generate_bill, bg="#4682B4", fg="white", width=20)
    b1.pack(pady=5)


# Main GUI
l1 =Label(root, text="Welcome to Danish Book Store", bg="#fff8e7")
l1.pack(pady=10)

b1 = Button(root, text="Login as Buyer", bg="#4682B4", fg="white", width=20, command=open_buyer_window)
b1.pack(pady=10)
b2 = Button(root, text="Login as Owner", bg="#4682B4", fg="white", width=20, command=open_owner_window)
b2.pack(pady=10)


root.mainloop()