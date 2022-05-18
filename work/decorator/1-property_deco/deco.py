from datetime import date
class Book:
    def __init__(self, isbn, title, author, date, price, edition):
        self.__isbn = isbn
        self.__title = title
        self.__authors = author
        self.__pub = date
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

    def get_authors(self):
        return self._authors

    def books_comparison(self, book=None, ISBN=None):
        if ISBN and book:
            return 'can\'t give all args'
            
        elif ISBN:
            return int(self._isbn) == int(ISBN)
             
        elif book: 
            return self._isbn == book._isbn
        
        else:
            return 'book ISBN or integer ISBN is missed!'
    
    def __str__(self):
        return f'ISBN: {self._isbn}\nTitle: {self._title}\nAuthor(s):{self._authors}\n\
            Date of publication: {self._pub}\nPrice: {self._price}\nEdition:{self._edition}'
    
    def promos(self, promo):
        return self._price * (100-promo)/100


def main():
    b1 = Book(
        '9781234567897', 
        'Agent Of Dread', 
        'Nida Rangel', 
        date(1966, 10, 12),
        23.88,
        'Ace Books' 
    )

    # print(b1.get_isbn())
    # b1.set_isbn(5781238567897)
    # print(b1.get_isbn())

    print(b1.isbn)
    b1.isbn = 5781238567897
    print(b1.isbn)

if __name__=='__main__':
    main()