from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line, Rectangle,Ellipse,Quad,Triangle


class MainInterface(GridLayout):
    Place_Shape = ""
    Line_Placements = [(),()]
    Triangle_Placements = [(),(),()]
    Quad_Placements = [(),(),(),()]
    
    def Set_Shape(self,Shape:str):
        self.Place_Shape = Shape
    
    def Draw_Shape(self,pos):
        W = int(self.ids.Width_Slider.value)
        H = int(self.ids.Height_Slider.value)
        RADIUS = int(self.ids.Radius_Slider.value)
        center = (pos[0] - (W/2),pos[1] - (H/2))
        THICC = int(self.ids.Thickness_Slider.value)
        if self.Place_Shape == "Rectangle":Rectangle(pos=center, size=(W,H))
        elif self.Place_Shape == "Ellipse":Ellipse(pos=center, size=(W, H))
        elif self.Place_Shape == "Circle":Ellipse(pos=(pos[0] - RADIUS, pos[1] - RADIUS), size=(RADIUS * 2, RADIUS * 2), angle_start=0, angle_end=360)
        elif self.Place_Shape == "Line":
            if self.Line_Placements[0] == ():self.Line_Placements[0] = pos
            elif self.Line_Placements[1] == ():
                self.Line_Placements[1] = pos
                Line(points=(self.Line_Placements[0][0],self.Line_Placements[0][1],self.Line_Placements[1][0],self.Line_Placements[1][1]),width=THICC)
                self.Line_Placements = [(),()]
        elif self.Place_Shape == "Quad":
            if self.Quad_Placements[0] == ():self.Quad_Placements[0] = pos
            elif self.Quad_Placements[1] == ():self.Quad_Placements[1] = pos
            elif self.Quad_Placements[2] == ():self.Quad_Placements[2] = pos
            elif self.Quad_Placements[3] == ():
                self.Quad_Placements[3] = pos
                Quad(points=(*self.Quad_Placements[0],*self.Quad_Placements[1],*self.Quad_Placements[2],*self.Quad_Placements[3]))
                self.Quad_Placements = [(),(),(),()]
        elif self.Place_Shape == "Triangle":
            if self.Triangle_Placements[0] == ():self.Triangle_Placements[0] = pos
            elif self.Triangle_Placements[1] == ():self.Triangle_Placements[1] = pos
            elif self.Triangle_Placements[2] == ():
                self.Triangle_Placements[2] = pos
                Triangle(points=(*self.Triangle_Placements[0],*self.Triangle_Placements[1],*self.Triangle_Placements[2]))
                self.Triangle_Placements = [(),(),()]

    def Draw_Hollow_Shape(self,pos):
        W = int(self.ids.Width_Slider.value)
        H = int(self.ids.Height_Slider.value)
        RADIUS = int(self.ids.Radius_Slider.value)
        THICC = int(self.ids.Thickness_Slider.value)
        center = (pos[0] - (W/2),pos[1] - (H/2))
        if self.Place_Shape == "Rectangle":Line(rectangle=(center[0],center[1],W,H),width=THICC)
        elif self.Place_Shape == "Ellipse":Line(ellipse=(center[0], center[1], W,H),width=THICC)
        elif self.Place_Shape == "Circle":Line(circle=(pos[0], pos[1], RADIUS),width=THICC)
        elif self.Place_Shape == "Line":
            if self.Line_Placements[0] == ():self.Line_Placements[0] = pos
            elif self.Line_Placements[1] == ():
                self.Line_Placements[1] = pos
                Line(points=(self.Line_Placements[0][0],self.Line_Placements[0][1],self.Line_Placements[1][0],self.Line_Placements[1][1]),width=THICC)
                self.Line_Placements = [(),()]
        elif self.Place_Shape == "Quad":
            if self.Quad_Placements[0] == ():self.Quad_Placements[0] = pos
            elif self.Quad_Placements[1] == ():self.Quad_Placements[1] = pos
            elif self.Quad_Placements[2] == ():self.Quad_Placements[2] = pos
            elif self.Quad_Placements[3] == ():
                self.Quad_Placements[3] = pos
                Line(points=[*self.Quad_Placements[0],*self.Quad_Placements[1],*self.Quad_Placements[2],*self.Quad_Placements[3]],close=True,width=THICC)
                self.Quad_Placements = [(),(),(),()]
        elif self.Place_Shape == "Triangle":
            if self.Triangle_Placements[0] == ():self.Triangle_Placements[0] = pos
            elif self.Triangle_Placements[1] == ():self.Triangle_Placements[1] = pos
            elif self.Triangle_Placements[2] == ():
                self.Triangle_Placements[2] = pos
                Line(points=[*self.Triangle_Placements[0],*self.Triangle_Placements[1],*self.Triangle_Placements[2]],close=True,width=THICC)
                self.Triangle_Placements = [(),(),()]
        

    def Clear_Canvas(self):
        self.ids.Canvas_Box.canvas.clear()

    def on_touch_up(self, touch):
        Touch_x, Touch_y = touch.pos
        if self.ids.Canvas_Box.x < Touch_x < (self.ids.Canvas_Box.x + self.ids.Canvas_Box.width) and self.ids.Canvas_Box.y < Touch_y < (self.ids.Canvas_Box.y + self.ids.Canvas_Box.height):
            with self.ids.Canvas_Box.canvas:
                R = int(self.ids.Red_Slider.value)/100
                G = int(self.ids.Green_Slider.value)/100
                B = int(self.ids.Blue_Slider.value)/100
                A = int(self.ids.Alpha_Slider.value)/100
                Color(R, G, B, A)  
                if self.ids.Hollow_Checker.active:self.Draw_Hollow_Shape(touch.pos)
                else: self.Draw_Shape(touch.pos)


class CanvasApp(App):
    pass





if __name__ == "__main__":CanvasApp().run()