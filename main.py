from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line, Rectangle


class MainInterface(GridLayout):
    Place_Shape = ""
    
    def Set_Shape(self,Shape:str):
        self.Place_Shape = Shape
    
    def Draw_Shape(self,pos):
        W = int(self.ids.Width_Slider.value)
        H = int(self.ids.Height_Slider.value)
        if self.Place_Shape == "Rectangle":Rectangle(pos=pos, size=(W,H))
    
    def on_touch_up(self, touch):
        Touch_x, Touch_y = touch.pos
        if self.ids.Canvas_Box.x < Touch_x < (self.ids.Canvas_Box.x + self.ids.Canvas_Box.width) and self.ids.Canvas_Box.y < Touch_y < (self.ids.Canvas_Box.y + self.ids.Canvas_Box.height):
            with self.ids.Canvas_Box.canvas:
                R = int(self.ids.Red_Slider.value)/100
                G = int(self.ids.Green_Slider.value)/100
                B = int(self.ids.Blue_Slider.value)/100
                A = int(self.ids.Alpha_Slider.value)/100
                Color(R, G, B, A)  
                if self.ids.Hollow_Checker.active:
                    pass
                else: self.Draw_Shape(touch.pos)


class CanvasApp(App):
    pass





if __name__ == "__main__":CanvasApp().run()