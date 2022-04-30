import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

import random

from src.quiz import Quiz
from src.parser_mod.parser import Parser


kivy.require('1.9.0')


class textinp(Widget):
    pass


class MainApp(App):

    def build(self) -> textinp:
        self.question_pairs: list[QuestionPair] = list(
            Parser(
                "src/parser_mod/lernsets/lat_verba_prima"
            ).get_question_pairs()
        )
        if not len(self.question_pairs):
            raise Exception('Haven\'t got any intput')
        self.refresh_question_pair()
        return textinp()

    def refresh_question_pair(self) -> None:
        self.question_pair = random.choice(self.question_pairs)

    def get_question(self) -> str:
        print(f'Question: {self.question_pair.question}')
        return ' '.join(self.question_pair.question)

    def process(self) -> None:
        text = self.root.ids.input.text
        self.root.ids.input.text = ''
        Clock.schedule_once(self.set_focus, 0.2)

        if text in self.question_pair:
            print(f'correct! {text}')
        else:
            print(f'false: {text}')

    def set_focus(self, event) -> None:
        self.root.ids.input.focus = True


# Run the App
if __name__ == "__main__":
    MainApp().run()
