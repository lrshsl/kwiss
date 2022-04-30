from typing import Generator

from src.parser_mod.utils import QuestionPair


class Quiz:
    def __init__(
            self,
            src: Generator[QuestionPair, None, None],
            settings: dict[str, str]
            ) -> None:
        self.src: Generator[QuestionPair, None, None] = src
        self.settings = settings
        self.pair: QuestionPair = QuestionPair()

    def new_question(self) -> str:
        try:
            self.pair = next(self.src)
        except StopIteration:
            return 'You\'re thru!'
        return self.pair.question

    def is_correct(self, answer: str) -> bool:
        if self.pair.answer == '':
            raise Exception('No answer. Please call a \'new_\' method firs')
        return answer in self.pair.answer
