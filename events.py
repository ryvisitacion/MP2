import pyglet
import random

def dropPartyEvent(database_count, data_files_count)
	n = 10
	for _ in range(database_count):
		n += (5 + random.randint(4, 8))
	
	new_count = data_files_count + n
	
	return new_count

def dataLeakEvent(database_count, data_files_count, bitcoin_count):
	n = 100
	t = .05
	for _ in range(database_count):
		r = round(random.uniform(0.45, 0.55), 2)
		n += round(100 * r)
		t += round((.025 * r), 2)
	return {'new_data_files':(data_files_count + n),
	'new_bitcoin_count':(bitcoin_count - t)}

def arrestEvent(laundromat_count):
	arrest_chance = random.random(0, 1)
	laundromat_modifier = 0
	for i in range(laundromat_count):
		laundromat_modifier += 0.5 * (1/1.25**(i-1))

	cash_modifier = 0
	excess = cash - 6000
	if excess > 0:
		x = excess//500
		for i in range(x):
			cash_modifier += 0.04

	day_modifier = (day - 2) * 0.05

	if arrest_chance <= (0.1 + laundromat_modifier + cash_modifier + day_modifier):
		gameOverScreen()

def irsVulnerability(collector_count):
	irsVulnerabilityChance = random.random(0, 1)
	if irsVulnerabilityChance <= 0.05:
		x = 30 #number of days it takes to convert data files to cash
		for _ in range(collector_count):
			x -= round(5 * random.uniform(0.45, 0.55))
		return x
