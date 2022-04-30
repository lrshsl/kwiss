from src.utils import QuestionPair


class Quiz:
    def __init__(self, src, settings):
        self.src = src
        self.settings = settings
        self.pair = QuestionPair()

    def new_question(self):
        try:
            self.pair = next(self.src)
        except StopIteration:
            return 'You\'re thru!'
        return self.pair.question

    def is_correct(self, answer):
        if self.pair.answer == '':
            raise Exception('No answer. Please call a \'new_\' method firs')
        return answer in self.pair.answer
