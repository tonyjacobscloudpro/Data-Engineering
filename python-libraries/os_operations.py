import os
import time


class OSOperations:
    """
    Demonstrates various functionalities of the 'os' library.
    """

    @staticmethod
    def list_directory(path="."):
        """
        Lists the contents of a directory.
        """
        try:
            contents = os.listdir(path)
            print(f"\nContents of '{path}':")
            for item in contents:
                print(f"- {item}")
        except Exception as e:
            print(f"Error listing directory contents: {e}")

    @staticmethod
    def change_directory(path):
        """
        Changes the current working directory.
        """
        try:
            os.chdir(path)
            print(f"Changed current directory to: {os.getcwd()}")
        except Exception as e:
            print(f"Error changing directory: {e}")

    @staticmethod
    def create_directory(path):
        """
        Creates a new directory.
        """
        try:
            os.makedirs(path, exist_ok=True)
            print(f"Directory '{path}' created successfully.")
        except Exception as e:
            print(f"Error creating directory: {e}")

    @staticmethod
    def remove_directory(path):
        """
        Removes a directory.
        """
        try:
            os.rmdir(path)
            print(f"Directory '{path}' removed successfully.")
        except Exception as e:
            print(f"Error removing directory: {e}")

    @staticmethod
    def rename_item(old_name, new_name):
        """
        Renames a file or directory.
        """
        try:
            os.rename(old_name, new_name)
            print(f"Renamed '{old_name}' to '{new_name}'.")
        except Exception as e:
            print(f"Error renaming item: {e}")

    @staticmethod
    def delete_file(file_path):
        """
        Deletes a file.
        """
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")

    @staticmethod
    def file_metadata(file_path):
        """
        Displays metadata of a file.
        """
        try:
            stats = os.stat(file_path)
            print(f"\nMetadata for '{file_path}':")
            print(f"- Size: {stats.st_size} bytes")
            print(f"- Last modified: {time.ctime(stats.st_mtime)}")
            print(f"- Created: {time.ctime(stats.st_ctime)}")
        except Exception as e:
            print(f"Error getting file metadata: {e}")


def display_menu():
    """
    Displays a menu of operations for the user.
    """
    print("\nOS Operations Menu")
    print("1. List Directory Contents")
    print("2. Change Directory")
    print("3. Create Directory")
    print("4. Remove Directory")
    print("5. Rename File/Directory")
    print("6. Delete File")
    print("7. Get File Metadata")
    print("8. Exit")


def main():
    """
    Main program loop for user interaction.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            path = input("Enter the directory path (or leave blank for current directory): ").strip() or "."
            OSOperations.list_directory(path)
        elif choice == "2":
            path = input("Enter the directory to navigate to: ").strip()
            OSOperations.change_directory(path)
        elif choice == "3":
            path = input("Enter the path for the new directory: ").strip()
            OSOperations.create_directory(path)
        elif choice == "4":
            path = input("Enter the path of the directory to remove: ").strip()
            OSOperations.remove_directory(path)
        elif choice == "5":
            old_name = input("Enter the current name of the file/directory: ").strip()
            new_name = input("Enter the new name: ").strip()
            OSOperations.rename_item(old_name, new_name)
        elif choice == "6":
            file_path = input("Enter the path of the file to delete: ").strip()
            OSOperations.delete_file(file_path)
        elif choice == "7":
            file_path = input("Enter the path of the file to get metadata: ").strip()
            OSOperations.file_metadata(file_path)
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
