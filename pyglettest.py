import pyglet
import random
import math
from pyglet import shapes

COLOR_BG = (40, 42, 54)
COLOR_FG = (248, 248, 242)
COLOR_COMMENT = (98, 114, 164)
COLOR_CYAN = (139, 233, 253)
COLOR_GREEN = (80, 250, 123)
COLOR_ORANGE = (255, 184, 108)
COLOR_PINK = (255, 121, 198)
COLOR_PURPLE = (189, 147, 249)
COLOR_RED = (255, 85, 85)
COLOR_YELLOW = (241, 250, 140)


class Flicker:
    def __init__(self, x, y, color, batch):
        self.size = 10
        self.shape = shapes.Rectangle(
            x=x, y=y, width=self.size/2, height=self.size, color=color, batch=batch)
        self.shape.anchor_position = (self.size/2, self.size)
        self.phase = random.uniform(0, 2*math.pi)
        self.opacity = random.randint(128, 255)
        self.speed = random.uniform(0.05, 0.35)

    def update(self, dt):
        self.phase = (self.phase + self.speed*dt)
        self.shape.opacity = (math.cos(0.2+self.phase/3) *
                              3*math.cos(self.phase*7)) * self.opacity
        self.shape.height = self.size*0.8 + 2.2 * \
            abs(self.size*(math.cos(self.phase*11)*math.sin(0.2*self.phase*3)))


class Twizzler:
    def __init__(self, x, y, color, batch):
        self.size = 8
        self.lines = []
        for _ in range(30):
            scale = random.uniform(0.5*self.size, 1.5*self.size)
            line = shapes.Rectangle(
                x, y, scale, random.randrange(1, 3), color=color, batch=batch)
            line.rotation = random.uniform(0, 360)
            line.scale = scale
            line.phase = random.uniform(0, 2*math.pi)
            line.speed = random.uniform(10, 40)*random.choice([-1, 1])
            self.lines.append(line)

    def update(self, dt):
        for line in self.lines:
            line.phase = (line.phase + line.speed*dt)
            line.rotation += 5*line.speed*dt
            line.opacity = (math.cos(0.2+line.phase/30) *
                            3*math.cos(line.phase/70))*255
            line.width = line.scale*0.2*line.scale*math.cos(line.phase/10)


class Glooper:
    def __init__(self, x, y, color, batch):
        self.x = x
        self.y = y
        self.circles = []
        for _ in range(5):
            radius = random.uniform(10, 15)
            circle = shapes.Circle(
                x, y, radius, color=color, batch=batch)
            circle.scale = circle.radius
            circle.phase = random.uniform(0, 2*math.pi)
            circle.speed = random.uniform(1, 4)*random.choice([-1, 1])
            self.circles.append(circle)

    def update(self, dt):
        for circle in self.circles:
            circle.x = self.x + 4 * \
                (math.cos(circle.phase)+math.cos(0.2+0.3*circle.phase))
            circle.y = self.y + 3 * \
                (math.sin(circle.phase)+math.sin(0.2+0.3*circle.phase))
            circle.phase = (circle.phase + circle.speed*dt)
            circle.radius = (math.cos(0.2+0.42*circle.phase) +
                             math.cos(0.31*circle.phase))*circle.scale/2


class Mandala:
    def __init__(self, x, y, color, batch):
        self.x = x
        self.y = y
        self.shapes = []

        radius = random.uniform(25, 50)
        circle = shapes.Circle(
            x, y, radius, color=color, batch=batch)
        circle.scale = radius
        circle.phase = 0
        circle.opacity = 128
        self.shapes.append(circle)

        side = radius*math.sqrt(2)

        square2 = shapes.Rectangle(
            x, y, side, side, color=color, batch=batch)
        square2.anchor_position = (side/2, side/2)
        square2.rotation = 45
        square2.opacity = 128
        self.shapes.append(square2)

        square = shapes.Rectangle(
            x, y, side, side, color=COLOR_COMMENT, batch=batch)
        square.anchor_position = (side/2, side/2)
        square.opacity = 128
        self.shapes.append(square)

        radius = side/2
        circle2 = shapes.Circle(
            x, y, radius, color=color, batch=batch)
        circle2.scale = radius
        circle2.phase = 0
        circle2.opacity = 128
        self.shapes.append(circle2)

        side *= math.sqrt(2)/2
        square3 = shapes.Rectangle(
            x, y, side, side, color=COLOR_PURPLE, batch=batch)
        square3.anchor_position = (side/2, side/2)
        square3.rotation = 45
        square3.opacity = 128
        self.shapes.append(square3)

        radius = side/2
        circle3 = shapes.Circle(
            x, y, radius, color=color, batch=batch)
        circle3.scale = radius
        circle3.phase = 0
        circle3.opacity = 128
        self.shapes.append(circle3)

        for shape in self.shapes:
            shape.speed = random.uniform(1, 4)*random.choice([-1, 1])

    def update(self, dt):
        for shape in self.shapes:
            if type(shape) is shapes.Rectangle:
                shape.rotation = (shape.rotation + 45*shape.speed*dt)
            else:
                shape.phase= (shape.phase + 45*shape.speed*dt)

                shape.radius = 0.8*shape.scale+ 0.2*math.cos(0.2*shape.phase)
        pass


entities = []
window = pyglet.window.Window()
pyglet.gl.glClearColor(COLOR_BG[0]/255, COLOR_BG[1]/255, COLOR_BG[2]/255, 255)
batch = pyglet.graphics.Batch()

# counter = pyglet.text.Label('',
#                             font_size=16,
#                             color=COLOR_FG+(255,),
#                             x=10, y=window.height-10,
#                             anchor_y='top',
#                             batch=batch)


@ window.event
def on_draw():
    window.clear()
    batch.draw()


def update(dt):
    for e in entities:
        e.update(dt)


def add_flicker(x, y, color):
    entities.append(Flicker(x, y, color, batch))


def add_twizzler(x, y, color):
    entities.append(Twizzler(x, y, color, batch))


def add_glooper(x, y, color):
    entities.append(Glooper(x, y, color, batch))


def add_mandala(x, y, color):
    entities.append(Mandala(x, y, color, batch))


for i in range(5):
    color = COLOR_RED if random.random() > 0.92 else COLOR_GREEN
    add_mandala(random.randrange(10, window.width-10),
                random.randrange(10, window.height-10),
                color)
    add_flicker(random.randrange(10, window.width-10),
                random.randrange(10, window.height-10),
                color)
    add_twizzler(random.randrange(10, window.width-10),
                random.randrange(10, window.height-10),
                color)
    add_glooper(random.randrange(10, window.width-10),
                random.randrange(10, window.height-10),
                color)

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
