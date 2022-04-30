import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock


from src.quiz import Quiz
from src.parser_mod.parser import Parser


kivy.require('1.9.0')


class textinp(Widget):
    pass


class MainApp(App):

    def build(self) -> textinp:
        self.quiz: Quiz = self.initialize_quiz()
        return textinp()

    def initialize_quiz(self) -> Quiz:
        src_file: str = 'src/parser_mod/lernsets/lat_verba_prima.txt'
        question_pairs = Parser().get_question_pairs(src_file)
        return Quiz(question_pairs, settings=dict())

    def generate_question(self) -> str:
        return self.quiz.new_question()

    def process(self) -> None:
        text = self.root.ids.input.text
        self.root.ids.input.text = ''
        Clock.schedule_once(self.set_focus, 0.2)

        if self.quiz.is_correct(text):
            print(f'correct! {text}')
            self.root.ids.question_label.text = self.generate_question()
        else:
            print(f'false: {text}')

    def set_focus(self, event) -> None:
        self.root.ids.input.focus = True


# Run the App
if __name__ == "__main__":
    MainApp().run()
