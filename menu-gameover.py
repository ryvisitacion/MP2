import pyglet
from pyglet.window import mouse



def gameOverScreen():
	window = pyglet.window.Window(width = 1200, height = 900)
	gameover_label = pyglet.text.Label('GAME OVER',
		font_name ='Times New Roman',
		font_size = 80,
		x = window.width//2, y = 3 * window.height//4,
		anchor_x ='center', anchor_y = 'top')

	global mainMenu
	mainMenu = pyglet.image.load('mainMenu.png')
	mainMenuSprite = pyglet.sprite.Sprite(mainMenu)
	mainMenuP = pyglet.image.load('mainMenuP.png') 
	mainMenuPSprite = pyglet.sprite.Sprite(mainMenuP)

	gameOverButtons = [mainMenuSprite, mainMenuPSprite]
	
	for buttons in gameOverButtons:
		buttons.position = (window.width//2.5, window.height//3)
		global a, b
		a, b = buttons.position

	def cursorCheck(x, y):
		if (a < x < a + mainMenu.width) and (b < y < b + mainMenu.height):
			return True
		return False
	
	@window.event()
	def on_draw():
		gameover_label.draw()

	@window.event()
	def on_mouse_motion(x, y, button, modifiers):
		if not cursorCheck(x, y):
			mainMenuSprite.draw()

	@window.event()
	def on_mouse_press(x, y, button, modifiers):
		if cursorCheck(x, y):
			mainMenuPSprite.draw()

	@window.event()
	def on_mouse_release(x, y, button, modifiers):
		if cursorCheck(x, y):
			mainMenuSprite.draw()
			mainMenuScreen()
			window.close()


def mainMenuScreen():
	window = pyglet.window.Window(width = 1200, height = 900)
	title_label = pyglet.text.Label('DROP',
		font_name ='Times New Roman',
		font_size = 80,
		x = window.width//2, y = 9 * window.height//10,
		anchor_x ='center', anchor_y = 'top')

	mainMenuStr = ['loadGame', 'loadGameP', 'newGame', 'newGameP', 'exitGame', 'exitGameP']
	mainMenuButtons = []

	for strings in mainMenuStr:
		loadImageButton = pyglet.image.load(strings + '.png')
		imageButton = pyglet.sprite.Sprite(loadImageButton)
		mainMenuButtons.append(imageButton)

	buttonPositions = []	
	for i in range(len(mainMenuButtons)):
		if i % 2 == 0:
			if i > 0:
				mainMenuButtons[i].position = (window.width//3, mainMenuButtons[i-1].position[1] - mainMenuButtons[i].height)
			else:
				mainMenuButtons[i].position = (window.width//3, window.height//2)
		else:
			mainMenuButtons[i].position = mainMenuButtons[i-1].position
		buttonPositions.append(mainMenuButtons[i].position)

	def cursorCheckMenu(x, y, i):
		if ((buttonPositions[i][0]) < x < buttonPositions[i][0] + mainMenuButtons[i].width) and (buttonPositions[i][1] < y < buttonPositions[i][1] + mainMenuButtons[i].height):
			return True
		return False		

	@window.event()
	def on_draw():
		title_label.draw()

	@window.event()
	def on_mouse_motion(x, y, button, modifiers):
		for i in range(0, len(mainMenuButtons), 2):
			if not cursorCheckMenu(x, y, i):
				mainMenuButtons[i].draw()

	@window.event()
	def on_mouse_press(x, y, button, modifiers):
		for i in range(1, len(mainMenuButtons), 2):
			if cursorCheckMenu(x, y, i):
				mainMenuButtons[i].draw()

	@window.event()
	def on_mouse_release(x, y, button, modifiers):
		for i in range(0, len(mainMenuButtons), 2):
			if cursorCheckMenu(x, y, i):
				mainMenuButtons[i].draw()
				#if i == 0:
					#load previous game
				#if i == 2:
					#start new game
				if i == 4:
					exit()



gameOverScreen()


pyglet.app.run()