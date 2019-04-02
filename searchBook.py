import json
import requests

userISBNinput = input('enter the ISBN for the book:')
books = requests.get(f'https://www.booknomads.com/api/v0/isbn/{userISBNinput}')

book_content = books.content
j = json.loads(book_content)

if 'error' in j.keys():
    print('book not found!')
else:
    print('Book Title is:',j['Title'])
