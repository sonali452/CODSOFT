class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if name not in self.contacts:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            print(f"Contact '{name}' added successfully!")
        else:
            print(f"Contact with name '{name}' already exists. Choose a different name.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")

    def search_contact(self, query):
        results = []
        for name, details in self.contacts.items():
            if (
                query.lower() in name.lower() or
                query.lower() in details["address"].lower() or
                query in details["phone"]
            ):
                results.append((name, details))
        return results

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact with name '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact with name '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            query = input("Enter name, address, or phone number to search: ")
            results = contact_manager.search_contact(query)
            if results:
                print("\nSearch Results:")
                for name, details in results:
                    print(f"\nName: {name}")
                    print(f"Phone: {details['phone']}")
                    print(f"Email: {details['email']}")
                    print(f"Address: {details['address']}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_manager.update_contact(name, phone, email, address)

        elif choice == "5":
            name = input("Enter name to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

# from flask import Flask, render_template, request, redirect, url_for
# import os

# app = Flask(__name__)

# # Ensure the "templates" folder exists
# template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
# if not os.path.exists(template_folder):
#     os.mkdir(template_folder)

# class ContactManager:
#     def __init__(self):
#         self.contacts = {}

#     def add_contact(self, name, phone, email, address):
#         if name not in self.contacts:
#             self.contacts[name] = {"phone": phone, "email": email, "address": address}
#             return f"Contact '{name}' added successfully!"
#         else:
#             return f"Contact with name '{name}' already exists. Choose a different name."

#     def view_contacts(self):
#         if not self.contacts:
#             return "No contacts found."
#         else:
#             contact_list = []
#             for name, details in self.contacts.items():
#                 contact_list.append({"name": name, "phone": details['phone'], "email": details['email'], "address": details['address']})
#             return contact_list

#     def search_contact(self, query):
#         results = []
#         for name, details in self.contacts.items():
#             if (
#                 query.lower() in name.lower() or
#                 query.lower() in details["address"].lower() or
#                 query in details["phone"]
#             ):
#                 results.append({"name": name, "phone": details['phone'], "email": details['email'], "address": details['address']})
#         return results

#     def update_contact(self, name, phone, email, address):
#         if name in self.contacts:
#             self.contacts[name] = {"phone": phone, "email": email, "address": address}
#             return f"Contact '{name}' updated successfully!"
#         else:
#             return f"Contact with name '{name}' not found."

#     def delete_contact(self, name):
#         if name in self.contacts:
#             del self.contacts[name]
#             return f"Contact '{name}' deleted successfully!"
#         else:
#             return f"Contact with name '{name}' not found."

# contact_manager = ContactManager()

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/add_contact', methods=['POST'])
# def add_contact():
#     name = request.form['name']
#     phone = request.form['phone']
#     email = request.form['email']
#     address = request.form['address']
#     message = contact_manager.add_contact(name, phone, email, address)
#     return render_template('result.html', message=message)

# @app.route('/view_contacts')
# def view_contacts():
#     contacts = contact_manager.view_contacts()
#     return render_template('contacts.html', contacts=contacts)

# @app.route('/search_contact', methods=['POST'])
# def search_contact():
#     query = request.form['query']
#     results = contact_manager.search_contact(query)
#     return render_template('search_result.html', results=results)

# @app.route('/update_contact', methods=['POST'])
# def update_contact():
#     name = request.form['name']
#     phone = request.form['phone']
#     email = request.form['email']
#     address = request.form['address']
#     message = contact_manager.update_contact(name, phone, email, address)
#     return render_template('result.html', message=message)

# @app.route('/delete_contact', methods=['POST'])
# def delete_contact():
#     name = request.form['name']
#     message = contact_manager.delete_contact(name)
#     return render_template('result.html', message=message)

# if __name__ == '__main__':
#     app.run(debug=True)