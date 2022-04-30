from typing import Generator, Iterable, Union


class QuestionPair:
    def __init__(
            self,
            question: str = '',
            answer: Union[str, Iterable[str]] = list()
            ) -> None:
        self.question: str = self._check_word(question)
        self.answer: Union[str, Iterable[str]] = self._check(answer)

    def _check(
            self, to_check: Union[str, Iterable[str]]
            ) -> Union[str, Iterable]:
        return self._check_word(to_check) if \
            isinstance(to_check, str) else self._check_iterable(to_check)

    def _check_iterable(self, iterable: Iterable) -> Iterable[str]:
        return [self._check_word(word) for word in iterable]

    def _check_word(self, word: str) -> str:
        new_word = word.strip()
        return new_word

    def __repr__(self) -> str:
        return f'QuestionPair({self.question}, {self.answer})'


class String:
    @staticmethod
    def get_nonempty_lines(string: str) -> Generator:
        for line in string.splitlines():
            line = line.strip(' \t\r\n')
            if len(line):
                yield(line)
