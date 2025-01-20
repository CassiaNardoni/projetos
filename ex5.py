from tkinter import W


def reverse_string(string):
    inverted = ""
    for char in string:
        inverted = char + inverted
    return inverted

# String a ser invertida
input_string = input("Digite uma string: ")
print(f"String invertida: {reverse_string(input_string)}")
W