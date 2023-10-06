# This assignment is completed independently
# https://github.com/nekkovo/WordSpinner.py

from Spinner import Spinner


def preprocess_text(text):
    return ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)


def main():
    with open('essay.txt', 'r') as file:
        original_text = preprocess_text(file.read())

    spinner = Spinner('synonyms-simplified.txt')

    print(f"Original: {original_text}")
    for i in range(3):
        spun_text = spinner.spin_text(original_text, 50)
        print(f"Option {i + 1}: {spun_text}")


if __name__ == "__main__":
    main()
