from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('design.kv')


class MyGridLayout(Widget):
    name = ObjectProperty(None)
    food = ObjectProperty(None)
    color = ObjectProperty(None)

    def pressed(self):
        print(
            f"Hello {self.name.text},you like {self.food.text} to eat and {self.color.text} color")
        self.name.text = ''
        self.food.text = ''
        self.color.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
