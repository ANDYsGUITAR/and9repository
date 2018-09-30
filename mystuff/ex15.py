from sys import argv

script, filename = argv # uses argv to get the filename

txt = open(filename) #open this file

print(f"Here's your file {filename}") #just print
print(txt.read()) #read the content of the file and print it

print("Type the filename again:")
file_again = input("> ") #let user type the filename again and get the filename

txt_again = open(file_again) #open the file
print(txt_again.read()) # read the file and print it.
