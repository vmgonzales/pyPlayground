# -*- coding: utf-8 -*-
'''
Classes and Objects Notebook
============================

Big Idea: 


Topics Covered
==============

* Classes, objects.
* Solutions to related LeetCode problems.

Created on Wed May 11 13:56:21 2022

@author: vmgon
'''

#%% LeetCode 1603: Design Parkins System
'''
Notes:
    
* Notice initiation using self.big = big. This sets the parameter for the
instance being initiated

* In the method addCar, we use self.big to refer to the big attribute for that instance.

'''
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
            else: return False
        if carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
            else: return False
        if carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
            else: return False        
        
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)