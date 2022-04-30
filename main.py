import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock


from src.quiz import Quiz
from src.lernsets.lat import verba_prima


kivy.require('1.9.0')


class textinp(Widget):
    pass


class MainApp(App):

    def build(self):
        self.quiz = self.initialize_quiz()
        return textinp()

    def initialize_quiz(self):
        return Quiz(verba_prima, settings=dict())

    def generate_question(self):
        return self.quiz.new_question()

    def process(self):
        text = self.root.ids.input.text
        self.root.ids.input.text = ''
        Clock.schedule_once(self.set_focus, 0.2)

        if self.quiz.is_correct(text):
            print(f'correct! {text}')
            self.root.ids.question_label.text = self.generate_question()
        else:
            print(f'false: {text}')

    def set_focus(self, event):
        self.root.ids.input.focus = True


# Run the App
if __name__ == "__main__":
    MainApp().run()
