def main():
    clasify(get_doc())
    
def get_doc():
    doc = input("File name: ")
    return doc

def clasify(file):
    if file.endswith(".gift") == True:
        print("image/ gift")
    elif file.endswith(".jpg") == True:
        print("image/ jpeg")
    elif file.endswith(".pdf") == True:
        print("application / pdf")
if __name__ == ("__main__"):
    main()