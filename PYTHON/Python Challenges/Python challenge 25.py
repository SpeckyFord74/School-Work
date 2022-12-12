w = open("Form.txt", "w")

firstName = input("Please enter your first name: ")
lastName = input("Please last name: ")
gender = input("Please enter your gender: ")
form = input("Please enter your form: ")

w.write("First name: " + firstName)
w.write("\nLast name: " + lastName)
