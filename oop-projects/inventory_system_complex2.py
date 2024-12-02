# inventory_system.py

# Features and Functionality:
# - Object-Oriented Design:
#   Implements classes for Product and Inventory.
# - Inventory Management:
#   Add, update, and delete products.
#   Search and view inventory.
# - GUI with Tkinter:
#   Provides a graphical interface for managing the inventory.
# - Preloaded Mock Data:
#   Includes a few sample products to view and manage in the GUI.

import tkinter as tk
from tkinter import ttk, messagebox


class Product:
    """
    Represents a product in the inventory.
    """
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"[{self.product_id}] {self.name} - ${self.price:.2f} (Qty: {self.quantity})"


class Inventory:
    """
    Manages the inventory of products.
    """
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """
        Adds a new product to the inventory.
        """
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists.")
        self.products[product.product_id] = product

    def update_product(self, product_id, name=None, price=None, quantity=None):
        """
        Updates an existing product in the inventory.
        """
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} not found.")
        product = self.products[product_id]
        if name is not None:
            product.name = name
        if price is not None:
            product.price = price
        if quantity is not None:
            product.quantity = quantity

    def delete_product(self, product_id):
        """
        Deletes a product from the inventory.
        """
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError(f"Product ID {product_id} not found.")

    def get_product(self, product_id):
        """
        Retrieves a product by ID.
        """
        return self.products.get(product_id)

    def list_products(self):
        """
        Lists all products in the inventory.
        """
        return list(self.products.values())


class InventoryGUI:
    """
    Provides a graphical interface for the inventory management system.
    """
    def __init__(self, root, inventory):
        self.root = root
        self.inventory = inventory
        self.root.title("Inventory Management System")
        self.root.geometry("800x500")

        # Product Form
        self.form_frame = ttk.LabelFrame(root, text="Product Form", padding=10)
        self.form_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(self.form_frame, text="Product ID:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.product_id_entry = ttk.Entry(self.form_frame)
        self.product_id_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(self.form_frame, text="Name:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = ttk.Entry(self.form_frame)
        self.name_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(self.form_frame, text="Price:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.price_entry = ttk.Entry(self.form_frame)
        self.price_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(self.form_frame, text="Quantity:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.quantity_entry = ttk.Entry(self.form_frame)
        self.quantity_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.add_button = ttk.Button(self.form_frame, text="Add Product", command=self.add_product)
        self.add_button.grid(row=4, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.form_frame, text="Update Product", command=self.update_product)
        self.update_button.grid(row=4, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.form_frame, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=4, column=2, padx=5, pady=5)

        # Inventory List
        self.list_frame = ttk.LabelFrame(root, text="Inventory", padding=10)
        self.list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.inventory_list = ttk.Treeview(self.list_frame, columns=("ID", "Name", "Price", "Quantity"), show="headings")
        self.inventory_list.heading("ID", text="Product ID")
        self.inventory_list.heading("Name", text="Name")
        self.inventory_list.heading("Price", text="Price")
        self.inventory_list.heading("Quantity", text="Quantity")
        self.inventory_list.pack(fill="both", expand=True)

        self.refresh_inventory_list()

    def refresh_inventory_list(self):
        """
        Refreshes the inventory list in the GUI.
        """
        for row in self.inventory_list.get_children():
            self.inventory_list.delete(row)

        for product in self.inventory.list_products():
            self.inventory_list.insert("", "end", values=(product.product_id, product.name, product.price, product.quantity))

    def add_product(self):
        """
        Adds a new product to the inventory.
        """
        try:
            product_id = int(self.product_id_entry.get())
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
            product = Product(product_id, name, price, quantity)
            self.inventory.add_product(product)
            self.refresh_inventory_list()
            messagebox.showinfo("Success", "Product added successfully!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_product(self):
        """
        Updates an existing product in the inventory.
        """
        try:
            product_id = int(self.product_id_entry.get())
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
            self.inventory.update_product(product_id, name, price, quantity)
            self.refresh_inventory_list()
            messagebox.showinfo("Success", "Product updated successfully!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_product(self):
        """
        Deletes a product from the inventory.
        """
        try:
            product_id = int(self.product_id_entry.get())
            self.inventory.delete_product(product_id)
            self.refresh_inventory_list()
            messagebox.showinfo("Success", "Product deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Initialize inventory and add mock products
def initialize_inventory_with_mock_data(inventory):
    inventory.add_product(Product(1, "Apple", 0.5, 100))
    inventory.add_product(Product(2, "Banana", 0.3, 150))
    inventory.add_product(Product(3, "Orange", 0.7, 120))
    inventory.add_product(Product(4, "Milk", 1.2, 50))
    inventory.add_product(Product(5, "Bread", 1.5, 30))


# Run the GUI
if __name__ == "__main__":
    inventory = Inventory()
    initialize_inventory_with_mock_data(inventory)  # Preload mock data
    root = tk.Tk()
    app = InventoryGUI(root, inventory)
    root.mainloop()
