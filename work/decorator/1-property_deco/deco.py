from datetime import date
class Book:
    def __init__(self, isbn=None, title=None, author=None, date_pub=None, price=None, edition=None):
        self.__isbn = isbn
        self.__title = title
        self.__authors = author
        self.__pub = date_pub
        self.__price = price
        self.__edition = edition
    
    # def get_isbn(self):
    #     return self.__isbn
    # def set_isbn(self, i):
    #     self.__isbn = i
    
    @property
    def isbn(self):
        return self.__isbn
    @isbn.setter
    def isbn(self, i):
        self.__isbn = i
    
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, t):
        self.__title = t

    @property
    def authors(self):
        return self.__authors
    @authors.setter
    def authors(self, a):
        self.__authors = a
    
    @property
    def pub(self):
        return self.__pub
    @pub.setter
    def pub(self, d):
        self.__pub = d
    
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, p):
        self.__price = p
    
    @property
    def edition(self):
        return self.__edition
    @edition.setter
    def edition(self, e):
        self.__edition= e
    

    def books_comparison(self, book=None, ISBN=None):
        if ISBN and book:
            return 'can\'t give all args'
            
        elif ISBN:
            return int(self.__isbn) == int(ISBN)
             
        elif book: 
            return self.__isbn == book.__isbn
        
        else:
            return 'book ISBN or integer ISBN is missed!'
    
    def __str__(self):
        return f'ISBN: {self.__isbn}\nTitle: {self.__title}\nAuthor(s):{self.__authors}\n\
            Date of publication: {self.__pub}\nPrice: {self.__price}\nEdition:{self.__edition}'
    
    def promos(self, promo):
        return self.__price * (100-promo)/100


def main():
    b1 = Book(
        '9781234567897', 
        'Agent Of Dread', 
        'Nida Rangel', 
        date(1966, 10, 12),
        23.88,
        'Ace Books' 
    )

    b2 = Book()
    b2.isbn = 9781234567897
    b2.title = 'Lord of the rings'
    b2.authors = 'John Ronald Reuel Tolkien'
    b2.pub = date(1954, 7, 29)
    b2.price = 97
    b2.edition = 'HarperCollins'
    print(b2)
    # print(b1.get_isbn())
    # b1.set_isbn(5781238567897)
    # print(b1.get_isbn())

    # print(b1.isbn)
    # b1.isbn = 5781238567897
    # print(b1.isbn)

if __name__=='__main__':
    main()