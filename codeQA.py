import math

def bmi(data):
       
        #String Testing
        if isinstance(data[0], str):
            return False
    
        if isinstance(data[1], str):
            return False
    
        if isinstance(data[2], str):
            return False
        
        #Negative Testing
        if data[0] <= 0:
            return False
    
        if data[1] <= 0:
            return False
        
        if data[2] <= 0:
            return False
        
        
        # Step 1
        data[0] = data[0] * .45
        
        # Step 2
        data[1] = data[1] * 12
        data[2] = data[1] + data[2]
        data[2] = data[2] * .025
        
        # Step 3
        total_height = data[2] * data[2]
        
        # Step 4
        final = round(data[0] / total_height)
        
        return final 

def retirement(data):


    #String Testing
    if isinstance(data[0], str):
        return False
    
    if isinstance(data[1], str):
        return False
    
    if isinstance(data[2], str):
        return False
    
    if isinstance(data[3], str):
        return False
    
    #Negative Testing
    if data[0] <= 0:
        return False
    
    if data[1] <= 0:
        return False
        
    if data[2] <= 0:
        return False
        
    if data[3] <= 0:
        return False
    
    #Calculations
    spy = float(data[1] * data[2]) * 1.35
    years_to_goal = math.ceil(data[3] / spy)
    age_on_completion = data[0] + years_to_goal
    
    if age_on_completion >= 100:
        age_on_completion = 100
        
    return age_on_completion
    
def main():
    while True:
        print("1: BMI")
        print("2: Retirement")
        print("3: Exit")

        choice = int(input("Please select an option listed above: "))

        if choice == 1:
            print("BMI")
            height_feet = int(input("Please enter Height in Feet: "))
            height_inches = float(input("Please enter Height in Inches: "))
            weight = float(input("Please enter Weight in Pounds: "))
            
            data = [weight, height_feet, height_inches]
            imb = bmi(data)
            print("Your BMI = ", imb)  
            
        elif choice == 2:
            print("Retirement")
            age = int(input("Please enter current age: "))
            annual_salary = int(input("Please enter annual salary: "))
            percent_saved = float(input("Please enter percentage saved yearly: "))
            goal = int(input("Please enter savings goal: "))
            
            data = [age, annual_salary, percent_saved, goal]
            retireAge = retirement(data)
            
            if retireAge == 100:
                print("The goal will not be reached before you turn 100")
                
            elif retireAge < 100:
                print("You will be ", retireAge, " years old when you complete your goal") 

        elif choice == 3:
            print("You have Exited the application")
            break
        
    
if __name__ == "__main__":
    main()
    
    