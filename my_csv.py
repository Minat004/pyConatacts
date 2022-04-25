import csv
data_values = []
try:
    with open('contacts.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)
            print(f'{row["name"]}, {row["surname"]}, {row["number"]}')
            data_values.append([row['name'], row['surname'], row['number']])
except Exception as ex:
    print(ex)

print(data_values)

with open('contacts.csv', mode='a', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['sasha', 'black', '123456789'])
    csv_writer.writerow(['masha', 'black', '987654321'])