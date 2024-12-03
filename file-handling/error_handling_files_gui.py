import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class FileRenamer:
    """
    Handles file renaming logic with error handling for missing files.
    """

    def __init__(self, directory, naming_pattern):
        self.directory = directory
        self.naming_pattern = naming_pattern
        self.original_files = []
        self.renamed_files = []
        self.errors = []

    def get_files(self):
        """
        Gets a list of files in the selected directory.
        """
        try:
            self.original_files = [
                f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))
            ]
        except Exception as e:
            raise Exception(f"Error accessing directory: {e}")

    def preview_renaming(self):
        """
        Generates a preview of the renamed files based on the naming pattern.
        """
        if not self.original_files:
            return []
        self.renamed_files = [
            self.naming_pattern.replace("{n}", str(i + 1).zfill(3)) + os.path.splitext(file)[1]
            for i, file in enumerate(self.original_files)
        ]
        return list(zip(self.original_files, self.renamed_files))

    def execute_renaming(self):
        """
        Renames the files in the directory, handling errors gracefully.
        """
        self.errors = []  # Reset errors
        success_count = 0

        for original, renamed in zip(self.original_files, self.renamed_files):
            original_path = os.path.join(self.directory, original)
            renamed_path = os.path.join(self.directory, renamed)
            try:
                os.rename(original_path, renamed_path)
                success_count += 1
            except FileNotFoundError:
                self.errors.append(f"File not found: {original}")
            except Exception as e:
                self.errors.append(f"Error renaming {original}: {e}")

        return success_count, self.errors


class FileRenamerGUI:
    """
    Provides a GUI for the File Renaming Tool with error handling.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Bulk File Renamer with Error Handling")
        self.root.geometry("700x500")

        self.directory = tk.StringVar()
        self.naming_pattern = tk.StringVar(value="File_{n}")
        self.preview_data = []

        # Initialize Widgets
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the GUI components.
        """
        # Directory Selection
        self.directory_frame = ttk.LabelFrame(self.root, text="Select Directory", padding=10)
        self.directory_frame.pack(fill="x", padx=10, pady=10)

        self.directory_entry = ttk.Entry(self.directory_frame, textvariable=self.directory, state="readonly")
        self.directory_entry.pack(side="left", fill="x", expand=True, padx=5)

        self.browse_button = ttk.Button(self.directory_frame, text="Browse", command=self.browse_directory)
        self.browse_button.pack(side="left", padx=5)

        # Naming Pattern
        self.pattern_frame = ttk.LabelFrame(self.root, text="Naming Pattern", padding=10)
        self.pattern_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(
            self.pattern_frame,
            text="Use '{n}' as a placeholder for numbering (e.g., File_{n} will become File_001, File_002, ...).",
        ).pack(anchor="w")

        self.pattern_entry = ttk.Entry(self.pattern_frame, textvariable=self.naming_pattern)
        self.pattern_entry.pack(fill="x", padx=5, pady=5)

        # Preview Table
        self.preview_frame = ttk.LabelFrame(self.root, text="Preview", padding=10)
        self.preview_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.preview_tree = ttk.Treeview(self.preview_frame, columns=("Original", "Renamed"), show="headings")
        self.preview_tree.heading("Original", text="Original Filename")
        self.preview_tree.heading("Renamed", text="Renamed Filename")
        self.preview_tree.pack(fill="both", expand=True)

        # Action Buttons
        self.action_frame = ttk.Frame(self.root)
        self.action_frame.pack(fill="x", padx=10, pady=10)

        self.preview_button = ttk.Button(self.action_frame, text="Preview", command=self.preview_renaming)
        self.preview_button.pack(side="left", padx=5)

        self.rename_button = ttk.Button(self.action_frame, text="Rename Files", command=self.rename_files, state="disabled")
        self.rename_button.pack(side="left", padx=5)

    def browse_directory(self):
        """
        Opens a directory selection dialog.
        """
        directory = filedialog.askdirectory()
        if directory:
            self.directory.set(directory)

    def preview_renaming(self):
        """
        Generates a preview of the renaming.
        """
        if not self.directory.get():
            messagebox.showerror("Error", "Please select a directory.")
            return

        renamer = FileRenamer(self.directory.get(), self.naming_pattern.get())
        try:
            renamer.get_files()
            self.preview_data = renamer.preview_renaming()

            # Update Preview Table
            for row in self.preview_tree.get_children():
                self.preview_tree.delete(row)

            for original, renamed in self.preview_data:
                self.preview_tree.insert("", "end", values=(original, renamed))

            if self.preview_data:
                self.rename_button.config(state="normal")
            else:
                messagebox.showinfo("Info", "No files found in the selected directory.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def rename_files(self):
        """
        Executes the renaming process with error handling.
        """
        if not self.preview_data:
            messagebox.showerror("Error", "No renaming preview available.")
            return

        confirm = messagebox.askyesno("Confirm Rename", "Are you sure you want to rename the files?")
        if not confirm:
            return

        renamer = FileRenamer(self.directory.get(), self.naming_pattern.get())
        try:
            renamer.get_files()
            renamer.preview_renaming()
            success_count, errors = renamer.execute_renaming()

            # Display success and errors
            success_message = f"Files renamed successfully: {success_count}"
            error_message = "\n".join(errors) if errors else "No errors encountered."

            messagebox.showinfo("Summary", f"{success_message}\n\nErrors:\n{error_message}")

            # Refresh the preview after renaming
            self.preview_renaming()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to rename files: {e}")


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerGUI(root)
    root.mainloop()
