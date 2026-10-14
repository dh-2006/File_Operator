
import os
from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    # Add a new journal entry
    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry:\n").strip()

            if entry == "":
                print("Entry cannot be empty. Please try again.")
                return

            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            file = open(self.filename, "a")
            file.write(f"[{date_time}]\n")
            file.write(entry + "\n\n")
            file.close()

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied. Cannot write to the file.")
        except OSError as e:
            print("Error while saving the entry:", e)

    # View all journal entries
    def view_entries(self):
        try:
            file = open(self.filename, "r")
            entries = file.read()
            file.close()

            if entries.strip() == "":
                print("No journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:")
                print("--------------------------------")
                print(entries.rstrip())

        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")
        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")
        except OSError as e:
            print("Error while reading the file:", e)

    # Search for a journal entry
    def search_entry(self):
        try:
            file = open(self.filename, "r")
            entries = file.read()
            file.close()

            if entries.strip() == "":
                print("No journal entries found. Start by adding a new entry!")
                return

            keyword = input("\nEnter a keyword or date to search: ").strip()

            if keyword == "":
                print("Search keyword cannot be empty.")
                return

            all_entries = entries.strip().split("\n\n")
            found_entries = []

            for entry in all_entries:
                if keyword.lower() in entry.lower():
                    found_entries.append(entry)

            if found_entries:
                print("\nMatching Entries:")
                print("--------------------------------")

                for entry in found_entries:
                    print(entry)
                    print()
            else:
                print("No entries were found for the keyword:")
                print(keyword + ".")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")
        except OSError as e:
            print("Error while searching the file:", e)

    # Delete all journal entries
    def delete_entries(self):
        try:
            file = open(self.filename, "r")
            entries = file.read()
            file.close()

            if entries.strip() == "":
                print("No journal entries to delete.")
                return

            confirm = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            elif confirm == "no":
                print("Deletion cancelled.")
            else:
                print("Invalid input. Please enter yes or no.")

        except FileNotFoundError:
            print("No journal entries to delete.")
        except PermissionError:
            print("Error: Permission denied. Cannot delete the file.")
        except OSError as e:
            print("Error while deleting the file:", e)


# Create object
journal = JournalManager()

# Display menu
while True:
    print("\nWelcome to Personal Journal Manager!")
    print("Please select an option:\n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        journal.add_entry()

    elif choice == "2":
        journal.view_entries()

    elif choice == "3":
        journal.search_entry()

    elif choice == "4":
        journal.delete_entries()

    elif choice == "5":
        print("\nThank you for using Personal Journal Manager.")
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option from the menu.")
