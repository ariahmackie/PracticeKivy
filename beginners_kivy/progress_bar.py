from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('progress.kv')

class MyLayout(Widget):
        def press_it(self):
            # grab current progress bar value
            current = self.ids.my_progress_bar.value
            # start over if number gets above 100%
            if current == 1:
                    current = 0
            # increment by 0.25
            current += .25
            # update the progress bar
            self.ids.my_progress_bar.value = current
            # update the lavel
            self.ids.my_label.text = f'{int(current * 100)} % Progress'

class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
