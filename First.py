#a=open("sample.txt","r")

def f(x):
    try:
        with open(x,"r") as a:
            for y in a:
                print(y.strip())
    except FileNotFoundError:
        print(f"The file '{x}' was not found.")

f("sample.txt")