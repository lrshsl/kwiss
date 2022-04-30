from typing import Generator, Iterable, Union


class QuestionPair:
    def __init__(self, question='', answer=list()):
        self.question = self._check_word(question)
        self.answer = self._check(answer)

    def _check( self, to_check):
        return self._check_word(to_check) if \
            isinstance(to_check, str) else self._check_iterable(to_check)

    def _check_iterable(self, iterable):
        return [self._check_word(word) for word in iterable]

    def _check_word(self, word):
        new_word = word.strip()
        return new_word

    def __repr__(self):
        return f'QuestionPair(\'{self.question}\', {self.answer})'


class String:
    @staticmethod
    def get_nonempty_lines(string):
        for line in string.splitlines():
            line = line.strip(' \t\r\n')
            if len(line):
                yield(line)
