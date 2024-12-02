import csv

def view_all_contact():
    file_name = 'data.csv'
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact_id = row['ID']
                name = row['name']
                email = row['email']
                phone_num = row['contact_number']
                address = row['address']
                print(f"{contact_id}. Name:{name}, Email: {email}, Phone number:{phone_num}, Address: {address}")
    except FileNotFoundError:
        print("NO FILE FOUND")