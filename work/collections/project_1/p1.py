class Vendor:
    def __init__(self, code, adress, commercial_name):
        self.__code = code
        self.__adress = adress
        self.__commercial_name = commercial_name
    
    def get_code(self):
        return self.__code
    def set_code(self, code):
        self.__code = code
    
    def get_adress(self):
        return self.__adress
    def set_adress(self, adress):
        self.__adress = adress
    
    def get_com(self):
        return self.__commercial_name
    def set_com(self, c):
        self.__commercial_name = c
    
    def __str__(self):
        return f'Code: {self.__code}\nAdress: {self.__adress}\nCommercial Name: {self.__commercial_name}\n'


class Computer:
    def __init__(self, code_c, brand, sell_date, price, vendor):
        self.__code_c = code_c
        self.__brand = brand
        self.__sell_date = sell_date
        self.__price = price
        self.__vendor = vendor
    
    def get_code(self):
        return self.__code_c
    def set_code(self, c):
        self.__code_c = c
    
    def get_brand(self):
        return self.__brand
    def set_brand(self, b):
        self.__brand = b
    
    def get_date(self):
        return self.__sell_date
    

    def get_price(self):
        return self.__price
    def set_price(self, p):
        self.__price = p
    
    def get_vendor(self):
        return self.__vendor
    def set_vendor(self, v):
        self.__vendor = v
    
    def vendor_compare(self, other):
        return self.get_code == other.get_code


def main():
    pass

if __name__=='__main__':
    main()

