def word_bank_program():
    words = []  # Initialize an empty list to store words

    while True:
        word = input("Enter a word: ")  # Ask for a word
        words.append(word)  # Store the word in the list

        # Ask if the user wants to continue
        try_again = input("Do you want to enter another word? (Y/y for Yes, N/n for No): ")
        
        if try_again.lower() == 'n':  # Check if the user wants to stop
            break  # Exit the loop if 'N' or 'n' is entered
        elif try_again.lower() != 'y':  # If input is not Y/y or N/n
            print("Invalid input. Please enter Y/y or N/n.")

    # Display the total number of words and the words entered
    print(f"\nTotal number of words: {len(words)}")
    print("Words entered:", ", ".join(words))

# Run the word bank program
word_bank_program()
