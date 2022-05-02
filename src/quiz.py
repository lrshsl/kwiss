import random

from src.utils import QuestionPair, String


class Quiz:
    def __init__(self, src, settings=dict()):
        self.src = list(src)
        self.nb_questions = len(self.src)
        self.settings = settings
        self.pair = QuestionPair()
        self.count = 0

    def new_question(self):
        if self.count == self.nb_questions + 1:
            return 'You\'r through!\nRestart?'
        self.pair = random.choice(self.src)
        self.count += 1
        return self.pair.question

    def is_correct(self, answer):
        if self.pair.answer == '':
            raise Exception('No answer. Please call a \'new_\' method firs')
        answer = answer.strip(' \t\n\r')
        return answer in self.pair.answer
