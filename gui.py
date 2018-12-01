import pyglet
import gametime
import gamestate
pyglet.resource.path = ['assets']
pyglet.resource.reindex()

#please remember that 0,0 is in the lower left for pyglet

time = gametime.gameTimeData(1, 1, 1, 1)
timeLabel = "Day: {}\n Week: {}\n Month: {}\n Year: {}".format(time.day, 
time.week, time.month, time.year)

window = pyglet.window.Window(width = 1200, height = 900)	
timeDisplay = pyglet.text.Label(
timeLabel,
font_name = 'Arial',
font_size = 36,
x = window.width // 2,
y = window.height - 50,
anchor_x = 'center'
)	

currentGame = gamestate.GameState()

dataFileCountLabel = pyglet.text.Label(
	"Data Files: {}".format(currentGame.dataFileCount),
	font_name = 'Arial',
	font_size = 24,
	x = window.width - window.width // 2.5,
	y = window.height - 140)

cashCountLabel = pyglet.text.Label(
	"Cash: {}".format(currentGame.cashCount),
	font_name = 'Arial',
	font_size = 24,
	x = window.width - window.width // 2.5,
	y = window.height - 135 - 55)

collectorCountLabel = pyglet.text.Label(
	"Collection Rate: {} data files per day".format(currentGame.collectorCount),
	font_name = 'Arial',
	font_size = 18,
	x = window.width - window.width // 2.5,
	y = window.height - 135 - 110)

bitcoinCountLabel = pyglet.text.Label(
	"Bitcoins: {} BTC".format(currentGame.bitcoinCount),
	font_name = 'Arial',
	font_size = 18,
	x = window.width - window.width // 2.5,
	y = window.height - 135 - 220)

def labelUpdate():
	dataFileCountLabel.text = "Data Files: {}".format(currentGame.dataFileCount)
	cashCountLabel.text = "Cash: {}".format(currentGame.cashCount)
	collectorCountLabel.text = "Collection Rate: {} data files per day".format(currentGame.collectorCount)
	bitcoinCountLabel.text = "Bitcoins: {} BTC".format(currentGame.bitcoinCount)

def update(dt):
	time.addDay()
	timeLabel = "Day: {}\n Week: {}\n Month: {}\n Year: {}".format(time.day, 
time.week, time.month, time.year)
	timeDisplay.text = timeLabel
	currentGame.update()
	labelUpdate()
	
pyglet.clock.schedule_interval(update, 1)	

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
		buttonFunctions[self.name]()
		labelUpdate()
		#print('{} button pressed'.format(self.name))
	
	def unpressed(self):
		self.button_sprite.image = self.neutral_image
		self.button_sprite.draw()
		#print('{} button released'.format(self.name))
	
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
y_button = window.height - 150

collectDataButton = Button("collectData", x_button, y_button)
cashInDataButton = Button("cashInData", x_button, y_button-55)
hireCollectorButton = Button("hireCollector", x_button, y_button-110)
hireLaundromatButton = Button("hireLaundromat", x_button, y_button-165)
buyBitcoinButton = Button("buyBitcoin", x_button, y_button-220)
sellBitcoinButton = Button("sellBitcoin", x_button, y_button-275)

buttonList = [collectDataButton, cashInDataButton, hireCollectorButton, hireLaundromatButton, buyBitcoinButton, sellBitcoinButton]
buttonFunctions = {
	"collectData":currentGame.collectData,
	"cashInData":currentGame.cashInData,
	"hireCollector":currentGame.hireCollector,
	"hireLaundromat":currentGame.hireLaundromat,
	"buyBitcoin":currentGame.buyBitcoin,
	"sellBitcoin":currentGame.sellBitcoin
}

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
	timeDisplay.draw()
	collectDataButton.drawButton()
	dataFileCountLabel.draw()
	for button in buttonList[1:]:
		if currentGame.cashInDataVisible:
			cashInDataButton.drawButton()
			cashCountLabel.draw()
		if currentGame.hireCollectorVisible:
			hireCollectorButton.drawButton()
			collectorCountLabel.draw()
		if currentGame.hireLaundromatVisible:
			hireLaundromatButton.drawButton()
		if currentGame.buyBitcoinVisible:
			buyBitcoinButton.drawButton()
			bitcoinCountLabel.draw()
		if currentGame.sellBitcoinVisible:
			sellBitcoinButton.drawButton()
	
pyglet.app.run()