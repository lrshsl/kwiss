import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock


kivy.require('1.9.0')


class textinp(Widget):
    pass


class MainApp(App):

    def build(self):
        self.generate_question()
        return textinp()

    def get_question(self) -> str:
        return self.question_pair.question

    def process(self):
        text = self.root.ids.input.text
        self.root.ids.input.text = ''
        Clock.schedule_once(self.set_focus, 0.2)

        if text == self.question_pair.answer:
            print(f'correct! {text}')
        else:
            print(f'false: {text}')

    def set_focus(self, event):
        self.root.ids.input.focus = True


# Run the App
if __name__ == "__main__":
    MainApp().run()
