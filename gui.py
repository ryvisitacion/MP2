import pyglet
import gametime
pyglet.resource.path = ['assets']
pyglet.resource.reindex()

#please remember that 0,0 is in the lower left for pyglet

time = gametime.gameTimeData(1, 1, 1, 1)
timeLabel = "Day: {}\n Week: {}\n Month: {}\n Year: {}".format(time.day, 
time.week, time.month, time.year)

startScreen = pyglet.window.Window(width = 400, height = 400)
window = pyglet.window.Window(width = 1200, height = 900)	
timeDisplay = pyglet.text.Label(
timeLabel,
font_name = 'Times New Roman',
font_size = 36,
x = window.width // 2,
y = window.height // 2,
anchor_x = 'center',
anchor_y = 'center'
)	

title_label = pyglet.text.Label('DROP',
		font_name ='Times New Roman',
		font_size = 36,
		x = window.width//4, y = window.height,
		anchor_x ='center', anchor_y = 'top')

def update(dt):
	time.addDay()
	timeLabel = "Day: {}\n Week: {}\n Month: {}\n Year: {}".format(time.day, 
time.week, time.month, time.year)
	timeDisplay.text = timeLabel
	
pyglet.clock.schedule_interval(update, 2)	

class Button:
	def __init__(self, name, x, y):
		self.x = x
		self.y = y
		self.name = name
		self.neutral_image = pyglet.resource.image(self.name + '.png')
		self.pressed_image = pyglet.resource.image(self.name + 'P' + '.png')
		#self.hovered_image = pyglet.resource.image(self.name + 'H' + '.png')
		self.button_sprite = pyglet.sprite.Sprite(self.neutral_image, self.x, self.y)
		self.width = self.neutral_image.width
		self.height = self.neutral_image.height
	
	def drawButton(self):
		self.button_sprite.draw()
	
	def pressed(self):
		self.button_sprite.image = self.pressed_image
		self.button_sprite.draw()
		print('{} button pressed'.format(self.name))
	
	def unpressed(self):
		self.button_sprite.image = self.neutral_image
		self.button_sprite.draw()
		print('{} button released'.format(self.name))
	
	def hovered(self):
		"""
		self.button_sprite.image = self.pressed_image
		self.button_sprite.draw()
		"""
		pass
	
	def unhovered(self):
		"""
		self.button_sprite.image = self.neutral_image
		self.button_sprite.draw()"""
		pass
	
	def cursorOnButton(self, mouseX, mouseY):
		if self.x <= mouseX <= self.x + self.width and self.y <= mouseY <= self.y + self.height:
			return True
		return False

x_button = window.width//8
y_button = window.height - 55

collectDataButton = Button("collectData", x_button, y_button)
cashInDataButton = Button("cashInData", x_button, y_button-55)
hireCollectorButton = Button("hireCollector", x_button, y_button-110)
hireLaundromatButton = Button("hireLaundromat", x_button, y_button-165)
buyBitcoinButton = Button("buyBitcoin", x_button, y_button-220)
sellBitcoinButton = Button("sellBitcoin", x_button, y_button-275)

buttonList = [collectDataButton, cashInDataButton, hireCollectorButton, hireLaundromatButton, buyBitcoinButton, sellBitcoinButton]

@window.event
def on_mouse_press(x, y, button, modifiers):
	for button in buttonList:
		if button.cursorOnButton(x, y):
			button.pressed()
@window.event
def on_mouse_release(x, y, button, modifiers):
	for button in buttonList:
		if button.cursorOnButton(x, y):
			button.unpressed()

@window.event
def on_mouse_motion(x, y, dx, dy):
	for button in buttonList:
		if button.cursorOnButton(x, y):
			button.hovered()
		else:
			button.unhovered()
		
@window.event
def on_draw():
	window.clear()
	title_label.draw()
	collectDataButton.drawButton()
	for button in buttonList[1:]:
		if gamestate.cashInData():
			cashInDataButton.drawButton()
		if gamestate.hireCollector():
			hireCollectorButton.drawButton()
		if gamestate.hireLaundromat():
			hireLaundromatButton.drawButton()
		if gamestate.buyBitcoin():
			buyBitcoinButton,drawButton()
		if gamestate.sellBitcoin():
			sellBitcoinButton.drawButton()
	
pyglet.app.run()
