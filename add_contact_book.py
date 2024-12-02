import csv
import remove_contact, no_dublicate


def add_contact_book(all_contact):
     name = input("Enter Your Name: ")
     email = input("Enter Your Email: ")
     def safe_input(prompt):
         while True:
             vaild_number = input(prompt)
             try:
                 if no_dublicate.is_phone_new(vaild_number):
                    return int(vaild_number)
                 else:
                     print("Phone Number Already Exists")
             except ValueError:
                 print("Invalid input! Please enter a valid integer.")
     contact_number = safe_input("Enter Contact Number: ")
     address = input("Enter Your Address: ")

     file_name = 'data.csv'
     book = {
         "ID": remove_contact.get_id(file_name),
         "name": name,
         "email": email,
         "contact_number": contact_number,
         "address": address,
     }

     with open(file_name, mode='a', newline='', encoding='utf-8') as file:
         writer = csv.DictWriter(file, fieldnames=book.keys())

         if file.tell() == 0:
             writer.writeheader()

         writer.writerow(book)

     all_contact.update(book)

     print("Books Added Successully")

     return all_contact