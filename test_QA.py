import unittest
from codeQA import *

class TestBMI(unittest.TestCase):
    #Passes
    def testValidInput(self):
        weight = 200
        height_feet = 5
        height_inches = 11
        data = [weight, height_feet, height_inches]
        result = bmi(data)
        self.assertEqual(result, 29)
    #Passes
    def testInvalidWeightString(self):
        weight = "seven"
        height_feet = 5
        height_inches = 11
        data = (weight, height_feet, height_inches)
        result = bmi(data)
        self.assertEqual(result, False)
    #Passes
    def testInvalidWeightNegative(self):
        weight = -1
        height_feet = 5
        height_inches = 11
        data = (weight, height_feet, height_inches)
        result = bmi(data)
        self.assertEqual(result, False)
    #Passes 
    def testInvalidHeightFeetString(self):
        weight = 200
        height_feet = "seven"
        height_inches = 11
        data = (weight, height_feet, height_inches)
        result = bmi(data)
        self.assertEqual(result, False)
    #Passes
    def testInvalidHeightFeetNegative(self):
        weight = 200
        height_feet = -5
        height_inches = 11
        data = (weight, height_feet, height_inches)
        result = bmi(data)
        self.assertEqual(result, False)
    #Passes
    def testInvalidHeightInchesString(self):
        weight = 200
        height_feet = 5
        height_inches = "seven"
        data = (weight, height_feet, height_inches)
        result = bmi(data)
        self.assertEqual(result, False)
    #Passes
    def testInvalidHeightInchesNegative(self):
        weight = 200
        height_feet = 5
        height_inches = -11
        data = (weight, height_feet, height_inches)
        result = bmi(data)
        self.assertEqual(result, False)
    
class TestRetirement(unittest.TestCase):
    #Passes
    def testValidInputOne(self):
        age = 25
        annual_salary = 65000
        percent_saved = 10
        goal = 1500000
        data = (age, annual_salary, percent_saved, goal)
        result = retirement(data)
        self.assertEqual(result, 27)
        
    #Passes
    def testValidInputTwo(self):
        age = 25
        annual_salary = 65000
        percent_saved = .10
        goal = 1500000
        data = (age, annual_salary, percent_saved, goal)
        result = retirement(data)
        self.assertEqual(result, 100)
        
    #Passes
    def testInvalidAgeString(self):
        age = "seven"
        annual_salary = 65000
        percent_saved = .10
        goal = 1500000
        data = (age, annual_salary, percent_saved, goal)
        result = retirement(data)
        self.assertEqual(result, False)
    
    #Passes
    def testInvalidAgeNegative(self):
        age = -25
        annual_salary = 65000
        percent_saved = .10
        goal = 1500000
        data = (age, annual_salary, percent_saved, goal)
        result = retirement(data)
        self.assertEqual(result, False)
        
    #Passes
    def testInvalidAnnualSalaryString(self):
        age = 25
        annual_salary = "thousand"
        percent_saved = .10
        goal = 1500000
        data = (age, annual_salary, percent_saved, goal)
        result = retirement(data)
        self.assertEqual(result, False)
        
    #Passes
    def testInvalidAnnualSalaryNegative(self):
        age = 25
        annual_salary = -65000
        percent_saved = .10
        goal = 1500000
        data = (age, annual_salary, percent_saved, goal)
        result = retirement(data)
        self.assertEqual(result, False)
        
    #Passes
    def testInvalidPercentSavedString(self):
        age = 25
        annual_salary = 65000
        percent_saved = "point 1"
        goal = 1500000
        data = (age, annual_salary, percent_saved, goal)
        result = retirement(data)
        self.assertEqual(result, False)
        
    #Passes    
    def testInvalidPercentSavedNegative(self):
        age = 25
        annual_salary = 65000
        percent_saved = -.10
        goal = 1500000
        data = (age, annual_salary, percent_saved, goal)
        result = retirement(data)
        self.assertEqual(result, False)
        
    #Passes 
    def testInvalidGoalString(self):
        age = 25
        annual_salary = 65000
        percent_saved = .10
        goal = "one fifty thousand"
        data = (age, annual_salary, percent_saved, goal)
        result = retirement(data)
        self.assertEqual(result, False)
        
    #Passes
    def testInvalidGoalNegative(self):
        age = 25
        annual_salary = 65000
        percent_saved = .10
        goal = -1500000
        data = (age, annual_salary, percent_saved, goal)
        result = retirement(data)
        self.assertEqual(result, False)
    
    
if __name__ == '__main__':
    unittest.main()
    
    
