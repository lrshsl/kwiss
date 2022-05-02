import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty, Property
from kivy.clock import Clock


from src.quiz import Quiz
from src.lernsets.lat import verba_prima
from src.utils import Color


kivy.require('1.9.0')


class MainActivity(BoxLayout):
    current_question = StringProperty("No question available")
    label_color = Property(Color.white)
    textinput_focused = BooleanProperty(False)
    score = Property(0)
    progress = Property(0)

    def __init__(self, **kwargs):
        self.initialize_quiz()
        self.generate_question()
        super().__init__(**kwargs)
        self.first_guess = True

    def initialize_quiz(self):
        self.quiz = Quiz(verba_prima)

    def generate_question(self):
        self.current_question = self.quiz.new_question()

    def on_text(self, text_input):
        if len(text_input.text) and text_input.text[-1] == '\n':
            self.on_enter(text_input.text)
            text_input.text = ''
        return 100

    def on_enter(self, answer):
        print('enter')
        correct = self.quiz.is_correct(answer)
        self.update_on(correct)
        Clock.usleep(1000)
        self.label_color = Color.white

    def update_on(self, result):
        if result is True:  # Ik, it's just for readablility
            self.label_color = Color.green
            self.generate_question()
            self.progress += 100 / self.quiz.nb_questions + 1
            if self.first_guess:
                self.score += 1
            else:
                self.first_guess = True
        else:
            self.label_color = Color.red
            self.first_guess = False

    def set_focus(self):
        self.textinput_focus = True


class MainApp(App):

    def build(self):
        return MainActivity()


"""
    def build(self):
        self.quiz = self.initialize_quiz()
        return Widget()

    def on_text_validate(self):
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
"""


# Run the App
if __name__ == "__main__":
    MainApp().run()
