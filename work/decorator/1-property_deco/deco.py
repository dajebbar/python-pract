class Book:
    def __init__(self, isbn, title, author, date, price, edition):
        self._isbn = isbn
        self._title = title
        self._authors = author
        self._pub = date
        self._price = price
        self._edition = edition
    
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