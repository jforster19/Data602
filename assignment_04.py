#!/usr/bin/env python
# coding: utf-8

# 
# 

# Q1: Create a class called BankAccount that has four attributes: bankname, firstname, lastname, and balance.
# The default balance should be set to 0.
# In addition, create ...
# ● A method called deposit() that allows the user to make deposits into their balance.
# ● A method called withdrawal() that allows the user to withdraw from their balance.
# ● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
# in your withdrawal() method.
# ● Use the __str__() method in order to display the bank name, owner name, and current
# balance.
# ● Make a series of deposits and withdrawals to test your class.

# In[16]:


class BankAccount():
    def __init__(self,bankname,firstname,lastname,balance:float=0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
    def deposit(self,deposit_amount):
        try:
            dep_amt = float(deposit_amount)
        except:
            print('Please deposit a positive valid amount')
        else:
            if dep_amt < 0:
                print('Please provide a positive amount to deposit into your account')
            self.balance += deposit_amount
    def withdrawal(self,withdraw):
        try:
            withdrawal_amt = float(withdraw)
        except:
            print('Please input a positive withdrawal amount')
        else:
            if withdrawal_amt < 0:
                print('Please provide a positive amount to withdraw from your account')
            elif withdrawal_amt>self.balance:
                print(f'Your current balance is {self.balance:.2f} and you cannot withdraw more than this amount at this time')
            else:
                self.balance -= withdrawal_amt
    def __str__(self):
        return f"At {self.bankname} the account holder's name is {self.firstname} {self.lastname} and the current balance is {self.balance:.2f}"


# In[17]:


bank = BankAccount('BOA','John','Smith',5)
bank.deposit(deposit_amount=2200)
bank.deposit(deposit_amount=100)
bank.withdrawal(withdraw=500)
bank.withdrawal(withdraw=5000)
str(bank)


# Q2: Create a class Box that has attributes length and width that takes values for length and width upon construction (instantiation via the constructor).
# In addition, create...
# ● A method called render() that prints out to the screen a box made with asterisks of
# length and width dimensions
# ● A method called invert() that switches length and width with each other
# ● Methods get_area() and get_perimeter() that return appropriate geometric calculations
# ● A method called double() that doubles the size of the box. Hint: Pay attention to return
# value here.
# ● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
# their respective lengths and widths are identical.
# ● A method print_dim() that prints to screen the length and width details of the box
# ● A method get_dim() that returns a tuple containing the length and width of the box
# ● A method combine() that takes another box as an argument and increases the length
# and width by the dimensions of the box passed in
# ● A method get_hypot() that finds the length of the diagonal that cuts through the middle
# ● Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1, box2 and box3 respectively
# ● Print dimension info for each using print_dim()
# ● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
# screen accordingly
# ● Combine box3 into box1 (i.e. box1.combine())
# ● Double the size of box2
# ● Combine box2 into box1

# In[43]:


import numpy as np
class Box():
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def render(self):
        for l in range(self.length):
            #print(l*"*")
            #for w in range(self.width):
            print(self.width*"*")
            #print('\n')
    def invert(self):
        self.width = self.length
        self.length = self.width
    def get_area(self):
        return self.length * self.width
    def get_perimeter(self):
        return 2*self.length * self.width
    def double(self):
        self.length = 2 * self.length
        self.width = 2 * self.width
    def __eq__(self, other_box):
        if isinstance(other_box, Box):
            if other_box.width == self.width and other_box.length == self.length:
                return True
            else:
                return False
        return False
    def print_dim(self):
        print(f"Length: {self.length} and Width: {self.width}")
    def get_dim(self):
        return(self.length,self.width)
    def combine(self,new_box):
        if isinstance(new_box, Box):
            self.length += new_box.length
            self.width += new_box.width
        else:
            print('Please submit a valid box class as an input for new_box parameter')
    def get_hypot(self):
        return np.sqrt(self.length **2 + self.width **3)


# In[47]:


box1 = Box(width=5,length=10)
box2 = Box(width=3,length=4)
box3 = Box(width=5,length=10)

box2.render()
print('\n')
for b in [box1,box2,box3]:
    b.print_dim()
print('\n')
print(f"Are box1 and box2 of the same dimensions? {box1==box2}")
print(f"Are box1 and box3 of the same dimensions? {box1==box3}")
print('\n')
#if box1 == box2, and also evaluate if box1 == box3
box1.combine(box3)
print("Box 1 combined with Box 3")
box1.print_dim()
print('\n')
print('Box 2 is doubled in size')
box2.double()
box2.print_dim()
print('\n')
print("Box 1 combined with Box 2")
box1.combine(box2)
box1.print_dim()


# In[ ]:




