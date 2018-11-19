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