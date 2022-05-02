import random

from src.utils import QuestionPair, String


class Quiz:
    def __init__(self, src, settings=dict()):
        src = list(src)
        random.shuffle(src)
        self.src = src
        self.src_generator = (pair for pair in self.src)
        self.nb_questions = len(self.src)
        self.settings = settings
        self.pair = QuestionPair()

    def new_question(self):
        try:
            self.pair = next(self.src_generator)
        except StopIteration:
            self.pair = QuestionPair(
                'You\'re thru!\nRestart?',
                'yeah!'
            )
        return self.pair.question

    def is_correct(self, answer):
        if self.pair.answer == '':
            raise Exception('No answer. Please call a \'new_\' method firs')
        answer = answer.strip(' \t\n\r')
        return answer in self.pair.answer
