from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class MainInterface(GridLayout):
    def Test(self):
        print(self.ids.Red_Slider.value)


class CanvasApp(App):
    pass





if __name__ == "__main__":CanvasApp().run()