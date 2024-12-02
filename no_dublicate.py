import csv
file_name = 'data.csv'

def is_phone_new(phone_number):
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['contact_number'] == phone_number:
                    return False
        return True
    except FileNotFoundError:
        return True