from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line, Rectangle,Ellipse,Quad,Triangle

class MainInterface(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.Resize_Drawings)
    Place_Shape = ""
    Line_Placements = [(),()]
    Triangle_Placements = [(),(),()]
    Quad_Placements = [(),(),(),()]
    Shapes = []
    Shapes_points = []
    Lined_Shapes = []
    Old_Window_size = []
    Old_Color = None

    
    def Set_Shape(self,Shape:str):
        self.Place_Shape = Shape
    
    def Draw_Shape(self,pos):
        W = int(self.ids.Width_Slider.value)
        H = int(self.ids.Height_Slider.value)
        RADIUS = int(self.ids.Radius_Slider.value)
        center = (pos[0] - (W/2),pos[1] - (H/2))
        THICC = int(self.ids.Thickness_Slider.value)
        Shape = None
        Shape_points = None
        if self.Place_Shape == "Rectangle":Shape = Rectangle(pos=center, size=(W,H))
        elif self.Place_Shape == "Ellipse":Shape = Ellipse(pos=center, size=(W, H))
        elif self.Place_Shape == "Circle":Shape = Ellipse(pos=(pos[0] - RADIUS, pos[1] - RADIUS), size=(RADIUS * 2, RADIUS * 2), angle_start=0, angle_end=360)
        elif self.Place_Shape == "Line":
            if self.Line_Placements[0] == ():self.Line_Placements[0] = pos
            elif self.Line_Placements[1] == ():
                self.Line_Placements[1] = pos
                Shape_points = Line(points=(self.Line_Placements[0][0],self.Line_Placements[0][1],self.Line_Placements[1][0],self.Line_Placements[1][1]),width=THICC)
                self.Line_Placements = [(),()]
        elif self.Place_Shape == "Quad":
            if self.Quad_Placements[0] == ():self.Quad_Placements[0] = pos
            elif self.Quad_Placements[1] == ():self.Quad_Placements[1] = pos
            elif self.Quad_Placements[2] == ():self.Quad_Placements[2] = pos
            elif self.Quad_Placements[3] == ():
                self.Quad_Placements[3] = pos
                Shape_points = Quad(points=(*self.Quad_Placements[0],*self.Quad_Placements[1],*self.Quad_Placements[2],*self.Quad_Placements[3]))
                self.Quad_Placements = [(),(),(),()]
        elif self.Place_Shape == "Triangle":
            if self.Triangle_Placements[0] == ():self.Triangle_Placements[0] = pos
            elif self.Triangle_Placements[1] == ():self.Triangle_Placements[1] = pos
            elif self.Triangle_Placements[2] == ():
                self.Triangle_Placements[2] = pos
                Shape_points = Triangle(points=(*self.Triangle_Placements[0],*self.Triangle_Placements[1],*self.Triangle_Placements[2]))
                self.Triangle_Placements = [(),(),()]
        if Shape != None:self.Shapes.append((Shape,self.Old_Color))
        if Shape_points != None: self.Shapes_points.append((Shape_points,self.Old_Color))

    def Draw_Hollow_Shape(self,pos):
        W = int(self.ids.Width_Slider.value)
        H = int(self.ids.Height_Slider.value)
        RADIUS = int(self.ids.Radius_Slider.value)
        THICC = int(self.ids.Thickness_Slider.value)
        center = (pos[0] - (W/2),pos[1] - (H/2))
        Shape_points = None
        Lined_Shape = None
        if self.Place_Shape == "Rectangle":Lined_Shape = Line(rectangle=(center[0],center[1],W,H),width=THICC)
        elif self.Place_Shape == "Ellipse":Lined_Shape = Line(ellipse=(center[0], center[1], W,H),width=THICC)
        elif self.Place_Shape == "Circle":Lined_Shape = Line(circle=(pos[0], pos[1], RADIUS),width=THICC)
        elif self.Place_Shape == "Line":
            if self.Line_Placements[0] == ():self.Line_Placements[0] = pos
            elif self.Line_Placements[1] == ():
                self.Line_Placements[1] = pos
                Shape_points= Line(points=(self.Line_Placements[0][0],self.Line_Placements[0][1],self.Line_Placements[1][0],self.Line_Placements[1][1]),width=THICC)
                self.Line_Placements = [(),()]
        elif self.Place_Shape == "Quad":
            if self.Quad_Placements[0] == ():self.Quad_Placements[0] = pos
            elif self.Quad_Placements[1] == ():self.Quad_Placements[1] = pos
            elif self.Quad_Placements[2] == ():self.Quad_Placements[2] = pos
            elif self.Quad_Placements[3] == ():
                self.Quad_Placements[3] = pos
                Shape_points = Line(points=[*self.Quad_Placements[0],*self.Quad_Placements[1],*self.Quad_Placements[2],*self.Quad_Placements[3]],close=True,width=THICC)
                self.Quad_Placements = [(),(),(),()]
        elif self.Place_Shape == "Triangle":
            if self.Triangle_Placements[0] == ():self.Triangle_Placements[0] = pos
            elif self.Triangle_Placements[1] == ():self.Triangle_Placements[1] = pos
            elif self.Triangle_Placements[2] == ():
                self.Triangle_Placements[2] = pos
                Shape_points = Line(points=[*self.Triangle_Placements[0],*self.Triangle_Placements[1],*self.Triangle_Placements[2]],close=True,width=THICC)
                self.Triangle_Placements = [(),(),()]
        if Lined_Shape != None:self.Lined_Shapes.append((Lined_Shape,self.Old_Color,self.Place_Shape))
        if Shape_points != None: self.Shapes_points.append((Shape_points,self.Old_Color))
        
    def Clear_Canvas(self):
        self.ids.Canvas_Box.canvas.clear()
        self.Shapes = []
        self.Shapes_points = []
  
    def Resize_Drawings(self, *args):
        self.ids.Canvas_Box.canvas.clear()
        self.Resize_Shapes()
        self.Resize_Shapes_points()
        self.Resize_Lined_Shapes()
        self.Old_Window_size = [self.width,self.height]
    
    def Resize_Shapes(self):
        for i in range(len(self.Shapes)):
            ratio_x = self.Shapes[i][0].pos[0]/self.Old_Window_size[0]
            ratio_y = self.Shapes[i][0].pos[1]/self.Old_Window_size[1]
            new_x = self.width * ratio_x
            new_y = self.height * ratio_y
            self.Shapes[i][0].pos = (new_x,new_y)
            self.ids.Canvas_Box.canvas.add(self.Shapes[i][1])
            self.ids.Canvas_Box.canvas.add(self.Shapes[i][0])

    def Resize_Shapes_points(self):
        for i in range(len(self.Shapes_points)):
            for point in range(len(self.Shapes_points[i][0].points)):
                # print(1,self.Shapes_points[i][0].points)
                if point%2 == 0:
                    print("X",point)
                    ratio = self.Shapes_points[i][0].points[point]/self.Old_Window_size[0]
                    new_point = self.width * ratio
                else:
                    print("Y",point)
                    ratio = self.Shapes_points[i][0].points[point]/self.Old_Window_size[1]
                    new_point = self.height * ratio
                self.Shapes_points[i][0].points[point] = new_point
            # print(2,self.Shapes_points[i][0].points)
            self.ids.Canvas_Box.canvas.add(self.Shapes_points[i][1])
            self.ids.Canvas_Box.canvas.add(self.Shapes_points[i][0])
    
    def Resize_Lined_Shapes(self):
        for i in range(len(self.Lined_Shapes)):
            if self.Lined_Shapes[i][2] == "Rectangle":
                rect = self.Lined_Shapes[i][0].rectangle
                ratio_x = rect[0]/self.Old_Window_size[0]
                ratio_y = rect[1]/self.Old_Window_size[1]
                new_x = self.width * ratio_x
                new_y = self.height * ratio_y
                self.Lined_Shapes[i][0].rectangle = (new_x,new_y,*rect[2:])
            elif self.Lined_Shapes[i][2] == "Ellipse":
                ell = self.Lined_Shapes[i][0].ellipse
                ratio_x = ell[0]/self.Old_Window_size[0]
                ratio_y = ell[1]/self.Old_Window_size[1]
                new_x = self.width * ratio_x
                new_y = self.height * ratio_y
                self.Lined_Shapes[i][0].ellipse = (new_x,new_y,*ell[2:])
            elif self.Lined_Shapes[i][2] == "Circle":
                circ = self.Lined_Shapes[i][0].circle
                ratio_x = circ[0]/self.Old_Window_size[0]
                ratio_y = circ[1]/self.Old_Window_size[1]
                new_x = self.width * ratio_x
                new_y = self.height * ratio_y
                self.Lined_Shapes[i][0].circle = (new_x,new_y,*circ[2:])
            self.ids.Canvas_Box.canvas.add(self.Lined_Shapes[i][1])
            self.ids.Canvas_Box.canvas.add(self.Lined_Shapes[i][0])

    def on_touch_up(self, touch):
        Touch_x, Touch_y = touch.pos
        if self.ids.Canvas_Box.x < Touch_x < (self.ids.Canvas_Box.x + self.ids.Canvas_Box.width) and self.ids.Canvas_Box.y < Touch_y < (self.ids.Canvas_Box.y + self.ids.Canvas_Box.height):
            with self.ids.Canvas_Box.canvas:
                R = int(self.ids.Red_Slider.value)/100
                G = int(self.ids.Green_Slider.value)/100
                B = int(self.ids.Blue_Slider.value)/100
                A = int(self.ids.Alpha_Slider.value)/100
                self.Old_Color = Color(R, G, B, A)  
                if self.ids.Hollow_Checker.active:self.Draw_Hollow_Shape(touch.pos)
                else: self.Draw_Shape(touch.pos)
                self.Old_Window_size = [self.width,self.height]

                

class CanvasApp(App):
    pass





if __name__ == "__main__":CanvasApp().run()