import pyglet
import gametime

#please remember that 0,0 is in the lower left for pyglet

'''
class Button:
	
	def __init__(x, y, width, height, label):
'''
time = gametime.gameTimeData(1, 1, 1, 1)
timelabel = "Day: {}\n Week: {}\n Month: {}\n Year: {}".format(time.day, 
time.week, time.month, time.year)

window = pyglet.window.Window(width = 1200, height = 900)	
timedisplay = pyglet.text.Label(
timelabel,
font_name = 'Times New Roman',
font_size = 36,
x = window.width // 2,
y = window.height // 2,
anchor_x = 'center',
anchor_y = 'center'
)	

def update(dt):
	time.addDay()
	timelabel = "Day: {}\n Week: {}\n Month: {}\n Year: {}".format(time.day, 
time.week, time.month, time.year)
	timedisplay.text = timelabel
	
pyglet.clock.schedule_interval(update, 2)	

@window.event
def on_draw():
	window.clear()
	timedisplay.draw()
	
pyglet.app.run()