
# title is used for to make each word capital in a sentence
# and capital is does just first letter of the sentence
  
print("👋 Welcome to the Greet Bot!")

def greet(name):
    return f"Hello, {name}!"

while True:
    name_input = input("Enter your Name: ").strip().title()
    
    if name_input == "":
        print("⚠️ Please enter your name.")
        continue  # Goes back to ask for a name again

    print(greet(name_input))

    while True:
        another = input("Do you want to greet another person? (yes/no): ").strip().lower()
        
        if another == "yes":
            break  # Break this inner prompt and return to outer loop
        elif another == "no":
            print("😊 Like to meet you again, Bye!")
            exit()  # Ends the entire program
        else:
            print("⚠️ Please enter 'yes' or 'no'.")
