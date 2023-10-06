# # hold the code defining a ChatBot class


import string
import random


def random_choice_from_list(phrases_list):
    return random.choice(phrases_list)


def make_list_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


def make_response_dictionary(lines):
    response_dict = {}
    for line in lines:
        keyword, response = line.split(',')
        response_dict[keyword.strip()] = response.strip()
    return response_dict  # 8


class ChatBot:
    def __init__(self, greetings, keywords, defaults):  # 1
        self.greetings = make_list_from_file(greetings)  # 2
        self.defaults = make_list_from_file(defaults)  # 9
        response_lines = make_list_from_file(keywords)  # 10
        self.keywords = make_response_dictionary(response_lines)

    def greet(self):
        return random_choice_from_list(self.greetings)

    def respond(self, human_text):
        human_text = human_text.lower()
        human_text = human_text.translate(str.maketrans('', '', string.punctuation))
        words = human_text.split()
        potential_response = []
        for word in words:
            if word in self.keywords:
                potential_response.append(self.keywords[word])
        if not potential_response:
            potential_response = self.defaults
        return random_choice_from_list(potential_response)
