"""In a file called bank.py, implement a program that prompts the user for a greeting.
 If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20.
   Otherwise, output $100.
 Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively."""

def main():
    money(get_great())

def get_great():
    great = input("Greeating: ")
    return great
def money(great):
    hola=list()
    hello=['h','e','l','l','o']
    Hello=['H','e','l','l','o']

    saludo = great.strip()
    for i in range(5):
        hola.append(saludo[i])

    if hola == hello or hola == Hello :
        print("$0")
    elif saludo[0] == 'h' or saludo[0] == 'H':
        print("$20")
    else:
        print('$100')
 
if __name__ == ("__main__"):
    main()