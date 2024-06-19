import csv
import json

with open('users.json', 'r') as user_file:
    users = json.load(user_file)

books = []
with open('books.csv', 'r') as book_file:
    csv_reader = csv.DictReader(book_file)
    for row in csv_reader:
        books.append(row)

for user in users:
    user['books'] = []

book_index = 0

for i in range(len(books) // len(users)):
    for user in users:
        user['books'].append(books[book_index])
        book_index += 1

for i in range(len(books) % len(users)):
    users[i]['books'].append(books[book_index])
    book_index += 1

with open('result.json', 'w') as result_file:
    json.dump(users, result_file, indent=2)
