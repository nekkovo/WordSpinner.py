# contain a main function that has a user talk to a ChatBot object
# Part.1
# Write a main function that creates a ChatBot then loops

from ChatBot import ChatBot  # 5


def main():
    chatter = ChatBot("greetings.txt", "keywords.txt", "defaults.txt")

    print(chatter.greet())  # 6 print a random greetings line

    while True:
        human_text = input("You: ")

        if human_text == "stop":
            print("Copy that.Bye!")
            break

        print("ChatBot:", chatter.respond(human_text))  # 7


if __name__ == "__main__":
    main()
