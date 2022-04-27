from . import token
from src.utils import QuestrionPair


settings_type = dict[str, str]


def nowhitespace(function):
    def wrapper(self, string: str, *args, **kwargs):
        stripped = string.strip(' \n')
        function.__name__(self, stripped, *args, **kwargs)
    return wrapper


# TODO: return types

class Parser:
    """ A class which is able to parse input files in different formats

    The first sector of the file (everything before the first '%%') can
    be used to tweak some settings for this Parser | Interpreter.
    This allows to parse different files differently, which can be useful
    if one import files or just for preference.

    If you want your questions and answers to be separated by a '='
    (rather than the default ':'), you could add the following on the first
    three lines of that file:
        word_definition_separator: =

        %%

    Note: There's currently no way to add comments in the settings sector.     # TODO

    Note: Even though that's a class, with fields and methods, many of those 'methods' are static.
            That's because I chose to use a quite functional | expression based code style. 
            This makes the 'methods' (should I say functions?) more independent - and
            in my personal opinion more clean and readable.
    """

    def __init__(self, filepath: str):
        self._file: str = filepath
        self._token_stream: list = []
        self.settings: settings_type = {'word_definition_separator': ':'}

    def get_question_pairs(self):
        with open(self._file, 'r') as f:
            src: str = f.read()
        return self._parse(src)

    def _parse(self, file_content: str):
        raw_settings, src = file_content.split('%%')
        settings = self._interpret_settings(raw_settings)
        return self._interpret(src, settings)

    def _interpret_settings(self, raw_settings: str) -> dict[str, str]:
        settings: dict[str, str] = dict()   ### TODO: check type hint
        for line in raw_settings.split('\n'):
            left, right = line.split(':')
            settings[left] = right         ### TODO: Raise error if invalid
        return settings

    def _interpret(self, src: str, settings: dict):
        question_pairs: set[dict[str, str]] = set()
        for line in src.split('\n'):
            questions, answers = line.split(settings['word_definition_separator'])
            questions, answers = (side.split(settings['std_separator']) for side in (questions, answers)) ### TODO: Neccessarily _that_ complicated..?
            question_pairs.add(QuestrionPair(question=questions, answer=answers))
        return question_pairs


"""
    def _tokenize_line(self, line: str):
        if self._next(2) == token.Token.SETTINGS_BEGIN:
            self._tokenize_settings()

        while 1:
            self.
            self._consume_whitespace(line)

    def _consume_whitespace(self, line: str):
        while line[self._i] in {' ', '\t'}:
            self._i += 1

    def _next():
        return line[i]

    def _get_setting_keyword(self):
        for keyword in token.Setting_keywords:
            if self._current_token == keyword:
                return keyword
"""
