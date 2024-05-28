def count_words(text):
   
    words = text.split()
    return len(words)

def main():
    """
    Main function to run the word counter program.
    """
    user_input = input("Please enter a sentence or paragraph: ")
    
    if not user_input.strip():
        print("Error: Input cannot be empty.")
        return
    
    word_count = count_words(user_input)
    
    print(f"The number of words in the input is: {word_count}")

if __name__ == "__main__":
    main()
