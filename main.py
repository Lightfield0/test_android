from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Merhaba Dünya', on_press=self.on_button_press)

    def on_button_press(self, instance):
        print('Düğmeye basıldı!')

if __name__ == '__main__':
    TestApp().run()
