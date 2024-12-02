import add_contact_book, view_all_contact, remove_contact, search_contact_info

all_contact = {}

print("Welcome to Contact Book Management System")

while True:
    print("0. Exit")
    print("1. Add Contact")
    print("2. View All Contact")
    print("3. Search Contact Info")
    print("4. Delete Contact Books")

    choice = input("Select any number: ")

    if choice == "0":
        print("Thanks for using Contact Book Management System ")
        break
    elif choice == "1":
        all_contact = add_contact_book.add_contact_book(all_contact)
    elif choice == "2":
        view_all_contact.view_all_contact()
    elif choice == "3":
        search_contact_info.search_contact_info()
    elif choice == "4":
        remove_contact.remove_contact_book()
    else:
        print("Choose a valid number")