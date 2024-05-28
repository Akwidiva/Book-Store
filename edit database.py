import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class ShoppingCart:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Bookstore Shopping Cart")
        self.root.configure(bg="#800080")
        self.items = []
        self.total = 0

        # Create the SQLite database connection
        self.conn = sqlite3.connect('cart.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cart
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, book TEXT, price REAL, quantity INTEGER)''')

        self.item_label = tk.Label(root, text="Book Title:", bg="#800080", fg="#FFFFFF", font=("times new roman", 12))
        self.item_label.pack()
        self.item_entry = tk.Entry(root, font=("times new roman", 12))
        self.item_entry.pack()

        self.price_label = tk.Label(root, text="Price (in Francs):", bg="#800080", fg="#FFFFFF", font=("times new roman", 12))
        self.price_label.pack()
        self.price_entry = tk.Entry(root, font=("times new roman", 12))
        self.price_entry.pack()

        self.add_button = tk.Button(root, text="Add Book to cart", command=self.add_book, bg="#4caf50", fg="white", font=("times new roman", 12))
        self.add_button.pack()

        self.item_listbox = tk.Listbox(root, width=50, height=10, font=("times new roman", 12))
        self.item_listbox.pack()

        self.quantity_label = tk.Label(root, text="Quantity:", bg="#800080", fg="#FFFFFF", font=("times new roman", 12))
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(root, font=("times new roman", 12))
        self.quantity_entry.pack()

        self.remove_button = tk.Button(root, text="Remove Book from cart", command=self.remove_book, bg="#f44336", fg="white", font=("times new roman", 12))
        self.remove_button.pack()

        self.edit_button = tk.Button(root, text="Edit Book in cart", command=self.edit_book, bg="#ffa500", fg="white", font=("times new roman", 12))
        self.edit_button.pack()

        self.print_button = tk.Button(root, text="Print Cart", command=self.print_cart, bg="#2196f3", fg="white", font=("times new roman", 12))
        self.print_button.pack()

        self.total_label = tk.Label(root, text="Total: 0 Francs", bg="#800080", fg="#FFFFFF", font=("times new roman", 14, "bold"))
        self.total_label.pack()

        self.save_button = tk.Button(root, text="Save Cart", command=self.save_cart, bg="#2196f3", fg="white", font=("times new roman", 12))
        self.save_button.pack()

        self.view_button = tk.Button(root, text="View Cart", command=self.view_cart, bg="#2196f3", fg="white", font=("times new roman", 12))
        self.view_button.pack()

        self.load_cart()

    def add_book(self):
        book = self.item_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())
        self.items.append((book, price, quantity))
        self.total += price * quantity
        self.item_listbox.insert(tk.END, f"{book} - {price} Francs - Quantity: {quantity}")
        self.total_label.config(text="Total: {:.2f} Francs".format(self.total))
        self.cursor.execute("INSERT INTO cart (book, price, quantity) VALUES (?, ?, ?)", (book, price, quantity))
        self.conn.commit()
        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def remove_book(self):
        selected_index = self.item_listbox.curselection()
        if selected_index:
            book, price, quantity = self.items[selected_index[0]]
            self.total -= price * quantity
            self.item_listbox.delete(selected_index)
            self.items.pop(selected_index[0])
            self.total_label.config(text="Total: {:.2f} Francs".format(self.total))
            self.cursor.execute("DELETE FROM cart WHERE id = ?", (selected_index[0] + 1,))
            self.conn.commit()
        else:
            messagebox.showerror("Error", "Please select a book to remove.")

    def edit_book(self):
        selected_index = self.item_listbox.curselection()
        if selected_index:
            book, price, quantity = self.items[selected_index[0]]
            frm = tk.Toplevel(self.root)
            frm.title("Edit Book")

            book_label = tk.Label(frm, text="Book Title:", bg="#800080", fg="#FFFFFF", font=("times new roman", 12))
            book_label.pack()
            book_entry = tk.Entry(frm, font=("times new roman", 12))
            book_entry.insert(0, book)
            book_entry.pack()

            price_label = tk.Label(frm, text="Price (in Francs):", bg="#800080", fg="#FFFFFF", font=("times new roman", 12))
            price_label.pack()
            price_entry = tk.Entry(frm, font=("times new roman", 12))
            price_entry.insert(0, str(price))
            price_entry.pack()

            quantity_label = tk.Label(frm, text="Quantity:", bg="#800080", fg="#FFFFFF", font=("times new roman", 12))
            quantity_label.pack()
            quantity_entry = tk.Entry(frm, font=("times new roman", 12))
            quantity_entry.insert(0, str(quantity))
            quantity_entry.pack()

            save_button = tk.Button(frm, text="Save Changes", command=lambda: self.update_book(selected_index[0], book_entry.get(), float(price_entry.get()), int(quantity_entry.get())), bg="#2196f3", fg="white", font=("times new roman", 12))
            save_button.pack()
        else:
            messagebox.showerror("Error", "Please select a book to edit.")

    def update_book(self, index, book, price, quantity):
        self.total -= self.items[index][1] * self.items[index][2]
        self.items[index] = (book, price, quantity)
        self.total += self.items[index][1] * self.items[index][2]
        self.item_listbox.delete(index)
        self.item_listbox.insert(index, f"{book} - {price} Francs - Quantity: {quantity}")
        self.total_label.config(text="Total: {:.2f} Francs".format(self.total))
        self.cursor.execute("UPDATE cart SET book = ?, price = ?, quantity = ? WHERE id = ?", (book, price, quantity, index + 1))
        self.conn.commit()
        messagebox.showinfo("Success", "Book updated in the cart.")

    def print_cart(self):
        if self.items:
            try:
                frm = tk.Toplevel(self.root)
                frm.title("Cart Contents")

            tree = ttk.Treeview(frm, columns=("Title", "Price", "Quantity"))
            tree.heading("#1", text="Title")
            tree.heading("#2", text="Price")
            tree.heading("#3", text="Quantity")
            tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Add scrollbars to the Treeview
            yscrollbar = ttk.Scrollbar(frm, orient=tk.VERTICAL, command=tree.yview)
            yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            tree.configure(yscrollcommand=yscrollbar.set)