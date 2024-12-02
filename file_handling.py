import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import time


class TextFileProcessor:
    """
    Handles text file processing.
    """

    def __init__(self, file_content):
        self.file_content = file_content
        self.rows = []
        self.processed_rows = []

    def process_file(self):
        """
        Processes file content and applies transformations.
        """
        self.rows = [line.strip().split(",") for line in self.file_content if line.strip()]
        header, *data = self.rows

        # Example transformations: Add a computed column "Total Value" (Price * Quantity)
        self.processed_rows = [header + ["Total Value"]]
        for row in data:
            try:
                price = float(row[1])
                quantity = int(row[2])
                total_value = price * quantity
                self.processed_rows.append(row + [f"{total_value:.2f}"])
            except ValueError:
                self.processed_rows.append(row + ["Error"])
        return self.rows, self.processed_rows

    def generate_summary(self):
        """
        Generates a summary based on the processed data.
        """
        if not self.processed_rows or len(self.processed_rows) <= 1:
            return {"Total Records": 0, "Average Total Value": "$0.00", "Unique Products": 0}

        data = self.processed_rows[1:]  # Exclude header
        total_records = len(data)
        total_values = [float(row[-1]) for row in data if row[-1] != "Error"]
        average_total_value = sum(total_values) / len(total_values) if total_values else 0
        unique_products = len(set(row[0] for row in data))
        return {
            "Total Records": total_records,
            "Average Total Value": f"${average_total_value:.2f}",
            "Unique Products": unique_products,
        }


class FileProcessingGUI:
    """
    GUI for file processing.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Text File Processing")
        self.root.geometry("900x600")

        self.file_content = []  # Stores file content
        self.processor = None

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # File Selection
        self.choice_frame = ttk.LabelFrame(self.root, text="Choose Data Source", padding=10)
        self.choice_frame.pack(fill="x", padx=10, pady=5)

        self.data_source = tk.StringVar(value="mock")

        ttk.Radiobutton(self.choice_frame, text="Mock Data", variable=self.data_source, value="mock", command=self.toggle_file_input).pack(side="left", padx=10)
        ttk.Radiobutton(self.choice_frame, text="Select File", variable=self.data_source, value="file", command=self.toggle_file_input).pack(side="left", padx=10)

        self.file_path_entry = ttk.Entry(self.choice_frame, state=tk.DISABLED, width=50)
        self.file_path_entry.pack(side="left", padx=10, fill="x", expand=True)

        self.browse_button = ttk.Button(self.choice_frame, text="Browse", command=self.browse_file, state=tk.DISABLED)
        self.browse_button.pack(side="left", padx=10)

        # File Actions
        self.file_label = ttk.Label(self.root, text="No data selected", wraplength=800)
        self.file_label.pack(pady=10)

        self.load_button = ttk.Button(self.root, text="Load Data", command=self.load_data)
        self.load_button.pack(pady=5)

        self.process_button = ttk.Button(self.root, text="Process Data", command=self.process_file, state=tk.DISABLED)
        self.process_button.pack(pady=5)

        # Data Display
        self.data_display_frame = ttk.LabelFrame(self.root, text="Data Display", padding=10)
        self.data_display_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.data_tree = ttk.Treeview(self.data_display_frame, columns=[], show="headings")
        self.data_tree.pack(fill="both", expand=True, padx=5)

        # Summary Label
        self.summary_label = ttk.Label(self.root, text="Summary will be displayed here", wraplength=800, anchor="center", justify="left")
        self.summary_label.pack(pady=10)

    def toggle_file_input(self):
        """
        Enables or disables the file path entry and browse button based on data source selection.
        """
        if self.data_source.get() == "file":
            self.file_path_entry.config(state=tk.NORMAL)
            self.browse_button.config(state=tk.NORMAL)
        else:
            self.file_path_entry.config(state=tk.DISABLED)
            self.browse_button.config(state=tk.DISABLED)

    def browse_file(self):
        """
        Opens a file dialog to select a file and updates the file path entry.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv")])
        if file_path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, file_path)

    def load_data(self):
        """
        Loads data based on the selected source (mock or file).
        """
        if self.data_source.get() == "mock":
            self.file_content = [
                "Product,Price,Quantity",
                "Apple,1.2,10",
                "Banana,0.5,20",
                "Orange,0.8,15",
                "Milk,2.5,5",
                "Bread,1.5,8",
                "Apple,1.2,12",
            ]
            self.file_label.config(text="Mock data loaded successfully.")
        elif self.data_source.get() == "file":
            file_path = self.file_path_entry.get()
            if not file_path:
                messagebox.showerror("Error", "Please provide a valid file path.")
                return
            try:
                with open(file_path, "r") as file:
                    self.file_content = file.readlines()
                self.file_label.config(text=f"Loaded file: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read file: {e}")
                return

        # Display pre-processed data
        self.display_data(self.file_content)
        self.process_button.config(state=tk.NORMAL)

    def display_data(self, data, processed=False):
        """
        Displays data in the data tree view.
        Handles both raw text data and processed structured data.
        """
        for column in self.data_tree["columns"]:
            self.data_tree.heading(column, text="")
        self.data_tree.delete(*self.data_tree.get_children())

        if isinstance(data[0], str):
            rows = [line.strip().split(",") for line in data if line.strip()]
        else:
            rows = data

        if not rows:
            return

        columns = rows[0]
        self.data_tree["columns"] = columns
        for col in columns:
            self.data_tree.heading(col, text=col)

        for row in rows[1:]:
            self.data_tree.insert("", "end", values=row)

        if processed:
            self.data_display_frame.config(text="Processed Data")
        else:
            self.data_display_frame.config(text="Pre-Processed Data")

    def process_file(self):
        """
        Processes the loaded data and displays results.
        """
        if not self.file_content:
            messagebox.showerror("Error", "No data to process.")
            return

        self.processor = TextFileProcessor(self.file_content)

        self.summary_label.config(text="")
        self.progress_label = ttk.Label(self.root, text="Processing in progress...")
        self.progress_label.pack(pady=5)
        self.root.update()
        time.sleep(2)

        original_data, processed_data = self.processor.process_file()
        self.display_data(processed_data, processed=True)

        summary = self.processor.generate_summary()
        summary_text = "\n".join(f"{key}: {value}" for key, value in summary.items())
        self.summary_label.config(text=summary_text)

        self.progress_label.config(text="Processing completed.")


# Main GUI Application
if __name__ == "__main__":
    root = tk.Tk()
    app = FileProcessingGUI(root)
    root.mainloop()
