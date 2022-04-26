import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from src.utils import QuestionPair

kivy.require('1.9.0')


class textinp(Widget):
    pass


class MainApp(App):

    def build(self):
        self.question_pair = QuestionPair(
            question="Who are you?",
            answer="Null")
        return textinp()

    def get_question(self) -> str:
        return self.question_pair.question

    def process(self):
        text = self.root.ids.input.text
        self.root.ids.input.text = ''
        Clock.schedule_once(self.set_focus, 0.2)

        if text == self.question_pair.answer:
            print(f'correct! [{text}]')
        else:
            print(f'false: {text}')

    def set_focus(self, event):
        self.root.ids.input.focus = True


# Run the App
if __name__ == "__main__":
    MainApp().run()
