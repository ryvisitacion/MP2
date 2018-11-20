import pyglet
import gametime
pyglet.resource.path = ['assets']
pyglet.resource.reindex()

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

class Button:
	def __init__(self, neutral, x, y):
		self.x = x
		self.y = y
		self.name = neutral
		self.neutral_image = pyglet.resource.image(neutral + '.png')
		self.pressed_image = pyglet.resource.image(neutral + 'P' + '.png')
		self.button_sprite = pyglet.sprite.Sprite(self.neutral_image, self.x, self.y)
		self.width = self.neutral_image.width
		self.height = self.neutral_image.height
	
	def drawButton(self):
		self.button_sprite.draw()
	
	def pressed(self):
		self.button_sprite.image = self.pressed_image
		self.button_sprite.draw()
		print('{} button pressed'.format(self.name))
	
	def revert(self):
		self.button_sprite.image = self.neutral_image
		self.button_sprite.draw()
		print('{} button released'.format(self.name))

buyBitcoinButton = Button("buyBitcoin", window.width // 2, window.height // 2)		

@window.event
def on_mouse_press(x, y, button, modifiers):
	if buyBitcoinButton.x <= x <= buyBitcoinButton.x + buyBitcoinButton.width and buyBitcoinButton.y <= y <= buyBitcoinButton.y + buyBitcoinButton.height:
		buyBitcoinButton.pressed()
@window.event
def on_mouse_release(x, y, button, modifiers):
	if buyBitcoinButton.x <= x <= buyBitcoinButton.x + buyBitcoinButton.width and buyBitcoinButton.y <= y <= buyBitcoinButton.y + buyBitcoinButton.height:
		buyBitcoinButton.revert()
		
@window.event
def on_draw():
	window.clear()
	buyBitcoinButton.drawButton()
	
pyglet.app.run()