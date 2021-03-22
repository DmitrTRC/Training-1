"""
Создать программу - квест
пример:
Пользователь <name> как вы думаете:
Вопрос ( Человек был на луне ?)
Варианты ответов:
1) был
2) Не был
Если правильный ответ то напечатать - Молодец, правильно !
Если нет - Иди читай книжки ! Неправильно!
"""
import time


class Question:
    def __init__(self, quest, ans_arr, ans):
        self.question = quest
        self.answers = ans_arr
        self._answer = int(ans)

    def show(self):
        print(self.question, end='\n\n')
        time.sleep(1)
        for index, answer in enumerate(self.answers, 1):
            print(f'{index}. {answer}')
        print()

    def get_answer(self):
        return self._answer


def load_questions():
    questions_arr = [Question(
        'Speed of light is ? ', ['255 000 Km/h', '300 000 Km/s'], 2
    ), Question(
        'How many states in US ?', ['50', '53', '51'], 1
    ), Question(
        'The year of death A.S. Pushkin ?', ['1799', '1827', '1837'], 3
    )]
    return questions_arr


def main():
    questions = load_questions()
    wins = 0
    for question in questions:
        question.show()
        answer = int(input('Your answer -> '))
        if answer == question.get_answer():
            wins += 1
            print(f'Correct! Total WINS: {wins}', end='\n\n')
        else:
            print(f'OOPS... FAIL!', end='\n\n')
    print(f'You win {wins} points')


if __name__ == '__main__':
    main()
