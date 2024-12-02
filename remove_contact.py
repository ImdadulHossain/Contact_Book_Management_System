import csv

file_name = 'data.csv'

def remove_contact_book():
    def safe_input(prompt):
        while True:
            user_input = input(prompt)
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    delete_id = safe_input("Enter ID Number for delete info: ")
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        rows = [row for row in rows if row['ID'] != str(delete_id)]

        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Contact Info with ID {delete_id} has been deleted.")
    except FileNotFoundError:
        print("File not found.")


def get_id(file_name):
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            ids = [int(row['ID']) for row in reader]
            return max(ids) + 1 if ids else 1
    except FileNotFoundError:
        return 1

def make_id(all_contact):
    all_contact['ID'] = get_id(file_name)

    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['ID'] + list(all_contact.keys()))

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(all_contact)
        print(f"Data appended with ID: {all_contact['ID']}")