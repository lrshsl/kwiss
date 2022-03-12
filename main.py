import kivy
from kivy.app import App
from kivy.uix.widget import Widget

kivy.require('1.9.0')


class textinp(Widget):
    pass


class MainApp(App):

    def build(self):
        return textinp()

    def process(self):
        text = self.root.ids.input.text
        print(text)


# Run the App
if __name__ == "__main__":
    MainApp().run()
