import json
import random
import os
import shutil


class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, answer):
        return self.correct_option == answer


class Questionnaire:
    def __init__(self):
        self.questions = []
        self.score = 0

    def load_questions_from_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            for question_data in data:
                question = Question(
                    question_data["text"], question_data["options"],
                    question_data["correct_option"]
                )
                self.questions.append(question)

    def display_question(self, index, question):
        print("Question %d: %s" % (index, question.text))
        for option_index, option in enumerate(question.options, start=1):
            print("   %d. %s" % (option_index, option))
        print()

    def get_user_input(self, num_options):
        while True:
            try:
                answer = int(input("Enter your answer: "))
                if 1 <= answer <= num_options:
                    return answer
                else:
                    print("Invalid input. Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def take_quiz(self):
        self.score = 0
        num_questions_to_ask = min(5, len(self.questions))

        # Shuffle the questions randomly
        shuffled_questions = random.sample(
            self.questions, num_questions_to_ask)

        for index, question in enumerate(shuffled_questions, start=1):
            self.display_question(index, question)
            answer = self.get_user_input(len(question.options))
            if question.is_correct(answer):
                self.score += 1
                print("Correct!\n")
            else:
                print("Incorrect.\n")
        self.display_results(num_questions_to_ask)

    def display_results(self, num_questions_asked):
        print("Quiz Completed!")
        score_percentage = (self.score / num_questions_asked) * 100
        print(
            "Your Score: %d/%d (%.2f%%)" % (
                self.score, num_questions_asked, score_percentage)
        )


def center_console():
    # Get the terminal width
    terminal_width, _ = shutil.get_terminal_size()

    # Calculate the left padding for centering
    left_padding = (terminal_width -
                    len("Welcome to the Geography Quiz!")) // 2

    # Print spaces to create padding
    print(" " * left_padding, end="")


def main():
    geography_questionnaire = Questionnaire()
    geography_questionnaire.load_questions_from_file(
        "geography_questions.json")

    while True:
        center_console()  # Center the output
        print("Welcome to the Geography Quiz!")
        geography_questionnaire.take_quiz()

        retake = input("Do you want to retake the quiz? (yes/no): ")
        if retake.lower() != "yes":
            print("Thank you for taking the quiz!")
            break
        else:
            print("Let's retake the quiz!\n")
            geography_questionnaire = Questionnaire()  # Reset the questionnaire


if __name__ == "__main__":
    main()
