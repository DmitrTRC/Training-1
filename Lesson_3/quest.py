import time
import requests
import random


class Question:
    COMPLEXITY = [
        'EASY',
        'MEDIUM',
        'HARD'
    ]

    def __init__(self, quest, ans_arr, ans):
        self.question = quest
        self.answers = ans_arr
        self._answer = ans

    def show(self):
        print(self.question, end='\n\n')
        time.sleep(1)
        for index, answer in enumerate(self.answers, 1):
            print(f'\n{index}. {answer}')
        print()

    def get_answer(self):
        return self._answer

    def get_complexity(self, num):
        return self.COMPLEXITY[num - 1]


def load_question(complexity=None):
    api_url = 'https://stepik.akentev.com/api/millionaire'
    params = {'complexity': complexity} if complexity else None
    response = requests.get(
        api_url, params=params
    ).json()
    answers = response.get('answers')
    answer = answers[0]
    random.shuffle(answers)

    return Question(response.get('question'), answers, answer)


def main():
    wins = 0
    name = input('Enter your name => ')
    questions_num = int(input('Enter how many questions do you like to get => '))
    complexity = 1
    for _ in range(questions_num):
        question = load_question(complexity=complexity)
        print(f'DIFFICULTY : {question.get_complexity(complexity)}')
        question.show()
        while True:
            user_answer = int(input('Enter your answer => '))
            if user_answer in range(1, len(question.answers) + 1):
                break

        if question.answers[user_answer - 1] == question.get_answer():
            print(f'\n{name} fine! Correct answer.\n')
            complexity += 1 if complexity < 3 else -3
            wins += 1
        else:
            print(f'\n{name} OOPS! You FAIL.\n')
            if complexity > 1: complexity -= 1

    print(f'{name} - You win {wins} points and that is {round(wins / questions_num * 100)} %')


if __name__ == '__main__':
    main()
