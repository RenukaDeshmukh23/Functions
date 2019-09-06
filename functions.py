from sys import argv #import argv functions of sys package
script,one,two,three=argv  #varibales for argv

def form(name,address,contact):             #defination of form()
    print(f" Name:{name}\n Address:{address}\n Contact:{contact}")
    print("\tThank you..")

print('\n"Please fill the followin details:"')
Name=input("Name:")
Address=input("Address:")
Contact=input("Contact:")

print('\n"Through argv"')       #print the line
print("script is called",script)        #print the name of program through script variable
form(one,two,three)                     #form()is called and argv values are passed

print('\n"direct values:"')
form("abcd","xyz","123456789")   #the values are directly passed

print('\n"Through temp variables"')
form(Name,Address,Contact)              #Input is taken from used in temp variables
