def sozsay():
    filename =input("Enter the filename :")
    try:
        with open (f"./data/{filename}","r") as file :
            content = file.read()
            words = content.split()
            wordsum = len(words)
            return wordsum
    except FileNotFoundError :
        print("File not found")
        return None
        
