def countWords(text):
   
    words = text.split()
    return len(words)

def main():

    user_input = input("Enter a text : ")
    
    if not user_input.strip():
        print("Input cannot be empty.")
        return
    
    word_count = countWords(user_input)
    
    print(f"Number of words in input: {word_count}")

if __name__ == "__main__":
    main()
