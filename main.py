from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line, Rectangle


class MainInterface(GridLayout):
    Place_Shape = ""
    # def Test(self):
    #     print(self.ids.Red_Slider.value)
    
    def Set_Shape(self,Shape:str):
        self.Place_Shape = Shape
    
    def on_touch_down(self, touch):
        #Where I want to check if click is in canvas
        print("Mouse Down", touch)
        bottom_left = self.ids.Canvas_Box.pos
        top_left = (self.ids.Canvas_Box.x, self.ids.Canvas_Box.y + self.ids.Canvas_Box.height)
        bottom_right = (self.ids.Canvas_Box.x + self.ids.Canvas_Box.width, self.ids.Canvas_Box.y)
        top_right = (self.ids.Canvas_Box.x + self.ids.Canvas_Box.width, self.ids.Canvas_Box.y + self.ids.Canvas_Box.height)

        with self.ids.Canvas_Box.canvas:
            Color(1, 0, 0, 1)  
            Line(points=[*bottom_left, *top_left, *top_right, *bottom_right, *bottom_left])


class CanvasApp(App):
    pass





if __name__ == "__main__":CanvasApp().run()