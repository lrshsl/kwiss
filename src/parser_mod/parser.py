from typing import Generator, Iterable
from .utils import QuestionPair, String


settings_type = dict[str, str]


class Parser:
    """ A class which is able to parse input files in different formats

    The first sector of the file (everything before the first '%%') can
    be used to tweak some settings for parsing.
    This allows to parse different files differently, which can be useful
    if one import files or just for preference.

    If you want your questions and answers to be separated by a '='
    (rather than the default ':'), you could add the following two lines on
    the first lines of that file:

        word_definition_separator: =
        %%

    Note: There's currently no way to add comments in the settings sector.     # TODO

    Note: Even though this is a class, with fields and methods, many of
            those 'methods' are static.
            I chose to use this kind of functional | expression based
            code style, becouse it makes the 'methods' (should I say
            functions?) more independent and - in my personal opinion -
            more clean and readable.
    """

    def __init__(self) -> None:  # TODO: filepath parameter to get_question_pairs()
        self._token_stream: list = []
        self.settings: settings_type = {
            'body_begin': '{',
            'body_end': '}',
            'word_definition_separator': ':',
            'std_separator': ','
        }

    def get_question_pairs(
            self, source_file: str
            ) -> Generator[QuestionPair, None, None]:
        with open(source_file, 'r') as f:
            src: str = f.read()
        return self._parsed(src)

    def _parsed(self, file_content: str) -> Generator:
        if '%%' in file_content:
            raw_settings, src = file_content.split('%%', 1)
        self._parse_settings(raw_settings)
        return self._parse(src)

    def _parse_settings(self, raw_settings: str) -> None:
        lines = String.get_nonempty_lines(raw_settings)
        for line in lines:
            left, right = line.split(':', 1)
            right = right.strip(' \'')
            self.settings[left] = right         # TODO: Raise error if invalid

    def _parse(self, raw_src: str):
        lines = self._get_usable_lines(raw_src)
        return self._parse_pairs(lines)

    def _get_usable_lines(self, raw_src: str) -> Generator[str, None, None]:
        begin = self.settings['body_begin']
        end = self.settings['body_end']
        lines: list[str] = list(String.get_nonempty_lines(raw_src))
        in_body: bool = False
        for line in lines:
            if begin in line:
                in_body = True
                *_, usable = line.split(begin)
                yield(usable)
            elif in_body:
                yield(line)
            if end in line:
                in_body = False

    def _parse_pairs(
            self,
            src_lines:
            Iterable[str]
            ) -> Generator[QuestionPair, None, None]:
        w_d_separator = self.settings['word_definition_separator']
        for line in src_lines:
            if not (w_d_separator in line):
                print(f'wrong line: {line}')
                continue
            questions, answers = line.split(
                w_d_separator,
                1
            )
            _, answers = (
                side.split(
                    self.settings['std_separator']
                ) for side in (questions, answers)
            )  # TODO: Neccessarily _that_ complicated..?
            yield(
                QuestionPair(question=questions, answer=answers)
            )
