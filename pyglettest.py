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
        self.phase = random.uniform(0, 2*math.pi)
        self.opacity = random.randint(128, 255)
        self.speed = random.uniform(0.05, 0.35)

    def update(self, dt):
        self.phase = (self.phase + self.speed*dt)
        self.shape.opacity = (math.cos(0.2+self.phase/3) *
                              3*math.cos(self.phase*7)) * self.opacity
        self.shape.height = self.size*0.8 + 0.2 * \
            (self.size*(math.cos(self.phase*11)*math.sin(0.2*self.phase*3)))
        #self.shape.width = self.size/2 + self.size*math.cos(2+self.phase*7)/4



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


for i in range(80):
    color = COLOR_RED if random.random() > 0.92 else COLOR_GREEN
    add_flicker(random.randrange(10, window.width-10),
                random.randrange(10, window.height-10),
                color)

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
