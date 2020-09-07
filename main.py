
def main():
    #Var
    v = "\n"
    var1 = input("Parameter number 1: ")
    var2 = input("Parameter number 2: ")
    var3 = input("Parameter number 3: ")
    """vars = input("how much parameters you need: ")
    var_number = 4

    vars = int(vars) + 3

    while int(var_number) <= int(vars):
        new_var = "var" + str(var_number)
        var_number = int(var_number) + 1
        print(new_var)"""

    #gen
    password1 = var1 + var2 + var3
    password2 = var1 + var3 + var2
    password3 = var2 + var1 + var3
    password4 = var2 + var3 + var1
    password5 = var3 + var1 + var2
    password6 = var3 + var2 + var1
    password7 = var1 + var2
    password8 = var1 + var3
    password9 = var2 + var1
    password10 = var2 + var3
    password11 = var3 + var1
    password12 = var3 + var2

    #set all in one var
    possible_passwords = password1 + v + password2 + v + password3 + v + password4 + v + password5 + v + password6 + v + password7 + v + password8 + v + password9 + v + password10 + v + password11 + v + password12 + v
    print(possible_passwords)
    #save passwords in a file
    with open("passwords.txt", "w") as f:
        f.write(possible_passwords)

try:
    main()
except:
    print("Error")