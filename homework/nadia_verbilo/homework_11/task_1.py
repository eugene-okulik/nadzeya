class Book:
    material = 'paper'
    text = True
    ISBN = '123-456'

    def __init__(self, title, author, pages, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.reserved = reserved


book1 = Book('Idiot', 'Dostoevski', 500, True)
book2 = Book('Idiot', 'Dostoevski', 500, False)
book3 = Book('Idiot', 'Dostoevski', 500, False)
book4 = Book('Idiot', 'Dostoevski', 500, False)
book5 = Book('Idiot', 'Dostoevski', 500, False)


def print_book(book):
    if book.reserved:
        print(f'Title: {book.title}, author: {book.author}, '
              f'pages: {book.pages}, material: {book.material}, reserved')
    else:
        print(f'Title: {book.title}, author: {book.author}, pages: {book.pages}, material: {book.material}')


print_book(book1)
print_book(book2)
print_book(book3)
print_book(book4)
print_book(book5)


class SchoolBook(Book):
    tasks = True

    def __init__(self, title, author, pages, reserved, subject, class_number):
        super().__init__(title, author, pages, reserved)
        self.subject = subject
        self.class_number = class_number


schoolbook1 = SchoolBook('Algebra', 'Ivanov', 200, True, 'math', 9)
schoolbook2 = SchoolBook('Algebra', 'Ivanov', 200, False, 'math', 9)
schoolbook3 = SchoolBook('Algebra', 'Ivanov', 200, False, 'math', 9)
schoolbook4 = SchoolBook('Algebra', 'Ivanov', 200, False, 'math', 9)
schoolbook5 = SchoolBook('Algebra', 'Ivanov', 200, False, 'math', 9)


def print_schoolbook(schoolbook):
    if schoolbook.reserved:
        print(f'Title: {schoolbook.title}, author: {schoolbook.author}, pages: {schoolbook.pages}, '
              f'subject: {schoolbook.subject}, class: {schoolbook.class_number}, reserved')
    else:
        print(f'Title: {schoolbook.title}, author: {schoolbook.author}, pages: {schoolbook.pages}, '
              f'subject: {schoolbook.subject}, class: {schoolbook.class_number}')


print_schoolbook(schoolbook1)
print_schoolbook(schoolbook2)
print_schoolbook(schoolbook3)
print_schoolbook(schoolbook4)
print_schoolbook(schoolbook5)
