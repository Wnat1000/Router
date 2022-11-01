import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.network.urlrequest import UrlRequest
kivy.require('2.1.0')


class MWidget(Widget):
    angle = NumericProperty(0)
    increment = NumericProperty(1)

    def __init__(self, **kwargs):
        super(MWidget, self).__init__(**kwargs)
        self.angle = 0
        self.increment = 1

    def obrót(self, angle):
        new_angle = (self.angle + angle) % 360
        self.angle = new_angle if new_angle >= 0 else 360 - new_angle
        self.output_label.text = f"Kąt: {self.angle}"

        UrlRequest('http://localhost:5000/?angle=' + str(self.angle))  # GET Request

    def set_increment(self):
        try:
            self.increment = abs(int(self.increment_box.text))
        except ValueError:
            self.increment = 1


class MApp(App):
    def build(self):
        return MWidget()


if __name__ == '__main__':
    MApp().run()