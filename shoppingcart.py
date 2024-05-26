import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ShoppingCart:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Bookstore Shopping Cart")
        self.root.configure(bg="#800080")
        self.items = []
        self.total = 0

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

        self.total_label = tk.Label(root, text="Total: 0 Francs", bg="#800080", fg="#FFFFFF", font=("times new roman", 14, "bold"))
        self.total_label.pack()

        self.save_button = tk.Button(root, text="Save Cart", command=self.save_cart, bg="#2196f3", fg="white", font=("times new roman", 12))
        self.save_button.pack()

    def add_book(self):
        book = self.item_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get() or 1

        if book and price:
            try:
                price = float(price)
                quantity = int(quantity)
                self.items.append((book, price, quantity))
                self.total += price * quantity
                self.total_label.config(text="Total: {:.2f} Francs".format(self.total))
                self.item_listbox.insert(tk.END, f"{book} - {price} Francs - Quantity: {quantity}")
                messagebox.showinfo("Success", "Book added to the cart.")
            except ValueError:
                messagebox.showerror("Error", "Invalid price or quantity.")
        else:
            messagebox.showerror("Error", "Please enter book title and price.")

        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def remove_book(self):
        selected_index = self.item_listbox.curselection()
        if selected_index:
            book = self.items[selected_index[0]]
            self.total -= book[1] * book[2]
            self.total_label.config(text="Total: {:.2f} Francs".format(self.total))
            self.item_listbox.delete(selected_index)
            self.items.pop(selected_index[0])
        else:
            messagebox.showerror("Error", "Please select a book to remove.")

    def save_cart(self):
        if self.items:
            try:
                with open("cart.txt", "w") as file:
                    for book in self.items:
                        file.write(f"{book[0]} - {book[1]} Francs - Quantity: {book[2]}\n")
                messagebox.showinfo("Success", "Cart saved to 'cart.txt'.")


                frm = tk.Toplevel(self.root)
                frm.title("Thank you for shopping with us here is your Order Summary")


                tree = ttk.Treeview(frm, columns=("Item", "Price", "Quantity"), show="headings")
                tree.heading("Item", text="Item")
                tree.heading("Price", text="Price (Frs)")
                tree.heading("Qty", text="Qty")
                tree.pack()


                for item in self.items:
                    tree.insert("", tk.END, values=(item[0], item[1], item[2]))


                total_label = tk.Label(frm, text="Total: {:.2f} Francs".format(self.total), font=("times new roman", 14, "bold"))
                total_label.pack()

            except Exception as e:
                messagebox.showerror("Error", f"Failed to save cart: {str(e)}")
        else:
            messagebox.showerror("Error", "The cart is empty please place an order.")
if __name__ == "__main__":
    root = tk.Tk()
    shopping_cart = ShoppingCart(root)
    root.mainloop()
