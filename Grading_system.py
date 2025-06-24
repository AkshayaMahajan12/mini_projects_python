print("🎓 Welcome to the Grading System!")

while True:
    marks_input=input("Enter number of marks (between 0-100): ")
    if marks_input.isdigit():
        marks=int(marks_input)
        if(marks<0):
            print(" ⚠️ Marks Cannot be Negative.")
        elif(marks>100):
            print(" ⚠️ Marks Should not exceed 100.")
        else:
            print(f"✅ You scored {marks} marks.")
            break

    else:
        print(" ⚠️ Enter a  Number.")


def  get_grade(marks):
    if(90<=marks<=100):
       
        return "🎉 Your Grade is A+. Great Job!"
    elif(80<=marks<=89):
        
        return "🎉 Your Grade is A. Great Job!"
    elif(70<=marks<=79):
        
        return "🎉 Your Grade is B. Great Job!"
    elif(60<=marks<=69):
       
        return "🎉 Your Grade is C. Great Job!"
    elif(50<=marks<=59):
     
        return "🎉 Your Grade is D. Great Job!"
    elif(0<=marks<=49):
  
        return "Your Grade is F. Better Luck next time!"

grades=get_grade(marks)
print(grades)
print("📘 Thank you for using the Grading System. Goodbye!")
      