from utils import QuestionPair, String


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

    def __init__(self):  # TODO: filepath parameter to get_question_pairs()
        self._token_stream = []
        self.settings = {
            'body_begin': '{',
            'body_end': '}',
            'word_definition_separator': ':',
            'std_separator': ','
        }

    def get_question_pairs(
            self, source_file
            ):
        with open(source_file, 'r') as f:
            src = f.read()
        return self._parsed(src)

    def _parsed(self, file_content):
        if '%%' in file_content:
            raw_settings, src = file_content.split('%%', 1)
        self._parse_settings(raw_settings)
        return self._parse(src)

    def _parse_settings(self, raw_settings):
        lines = String.get_nonempty_lines(raw_settings)
        for line in lines:
            left, right = line.split(':', 1)
            right = right.strip(' \'')
            self.settings[left] = right         # TODO: Raise error if invalid

    def _parse(self, raw_src):
        lines = self._get_usable_lines(raw_src)
        return self._parse_pairs(lines)

    def _get_usable_lines(self, raw_src):
        begin = self.settings['body_begin']
        end = self.settings['body_end']
        lines = list(String.get_nonempty_lines(raw_src))
        in_body = False
        for line in lines:
            if begin in line:
                in_body = True
                *_, usable = line.split(begin)
                yield(usable)
            elif in_body:
                yield(line)
            if end in line:
                in_body = False

    def _parse_pairs( self, src_lines):
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
