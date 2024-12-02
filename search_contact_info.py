import csv

file_name = 'data.csv'

def search_by_id(search_id):
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ID'] == str(search_id):
                    return row
            return None
    except FileNotFoundError:
        print("File not found.")
        return None

def search_contact_info():
    def safe_input(prompt):
        while True:
            user_input = input(prompt)
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
    search_id = safe_input('Enter your search id: ')
    result = search_by_id(search_id)
    if result:
        row = result
        contact_id = row['ID']
        name = row['name']
        email = row['email']
        phone_num = row['contact_number']
        address = row['address']
        print(f"{contact_id}. Name:{name}, Email: {email}, Phone number:{phone_num}, Address: {address}")
    else:
        print("No record found with ID:", search_id)
