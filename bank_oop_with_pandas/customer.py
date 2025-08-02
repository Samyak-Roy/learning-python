class Customer:
    def __init__(self,name,d_o_b,gender,aadhar_number,address):
        self.__name = name
        self.__d_o_b = d_o_b
        self.__gender = gender
        self.__aadhar_number = aadhar_number
        self.__address = address

    @property
    def name(self):
        return self.__name
    @property
    def d_o_b(self):
        return self.__d_o_b
    @property
    def gender(self):
        return self.__gender
    @property
    def aadhar_number(self):
        return self.__aadhar_number
    @property
    def address(self):
        return self.__address
    
    def __str__(self):
        return f"Customer Name: {self.__name}, DOB: {self.__d_o_b}"
#testing
if __name__ == "__main__":
    customer1 = Customer("John Doe", "1990-01",'Male', '123456789012', '123 Elm Street')
    print(customer1.name)  # Output: John Doe
    print(customer1.d_o_b)  # Output: 1990-01
    print(customer1._Customer__aadhar_number)   # Output: 123456789012