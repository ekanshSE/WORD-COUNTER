import os

def count_words(text):
    """
    Counts the number of words in the given text.

    :param text: String containing the text to count words in.
    :return: The number of words in the text.
    """
    if text.strip():
        words = text.split()
        return len(words)
    else:
        return "Error: No text provided. Please enter a sentence or paragraph."

def count_characters(text):
    """
    Counts the number of characters in the given text.

    :param text: String containing the text to count characters in.
    :return: The number of characters in the text.
    """
    return len(text)

def count_sentences(text):
    """
    Counts the number of sentences in the given text.

    :param text: String containing the text to count sentences in.
    :return: The number of sentences in the text.
    """
    # Assuming sentences end with '.', '!', or '?'
    sentences = text.split('.')
    return len(sentences)

def read_from_file(file_path):
    """
    Reads text from a given file.

    :param file_path: Path to the file to read from.
    :return: The text read from the file.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        return "Error: File does not exist."

def display_statistics(text):
    """
    Displays various statistics about the given text.

    :param text: String containing the text to analyze.
    """
    print(f"Text Analysis:")
    print(f"Word Count: {count_words(text)}")
    print(f"Character Count: {count_characters(text)}")
    print(f"Sentence Count: {count_sentences(text)}")

def main():
    predefined_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    
    while True:
        print("\nWord Counter Program")
        print("1. Use predefined text")
        print("2. Enter your text")
        print("3. Read text from a file")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            text_to_count = predefined_text
            print(f"\nPredefined text: {predefined_text}")
        elif choice == '2':
            text_to_count = input("\nEnter a sentence or paragraph to count words: ")
        elif choice == '3':
            file_path = input("\nEnter the file path: ")
            text_to_count = read_from_file(file_path)
            if text_to_count.startswith("Error"):
                print(text_to_count)
                continue
        elif choice == '4':
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice.")
            continue

        display_statistics(text_to_count)

if __name__ == "__main__":
    main()
