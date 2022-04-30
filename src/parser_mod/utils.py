from typing import Generator


class QuestionPair:
    def __init__(self, question: list[str], answer: list[str]) -> None:
        self.question = question
        self.answer = answer


class String:
    @staticmethod
    def get_nonempty_lines(string: str) -> Generator:
        for line in string.splitlines():
            line = line.strip(' \t\r\n')
            if len(line):
                yield(line)
