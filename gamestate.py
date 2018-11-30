import pyglet

class GameState:
	def __init__(self, saveFile = None):
		self.saveFile = savefile if saveFile is not None else 'init'
		self.dataFileCount = int()
		self.cumulativeDataFileCount = int()
		self.cashCount = int()
		self.bitcoinCount = int()
		self.collectorCount = int()
		self.databaseCount = int()
		self.laundromatCount = int()
		self.attributeList = [self.dataFileCount, self.cumulativeDataFileCount, self.cashCount, self.bitcoinCount,
self.collectorCount, self.databaseCount, self.laundromatCount]
	
	def loadSaveData(self):
		save = open(self.saveFile + '.txt', 'r')
		saveData = save.readlines()
		saveData = [x.strip() for x in saveData]
		for i in range(len(saveData)):
			self.attributeList[i] = saveData[i]
		
	def collectData(self):
		self.dataFileCount += 1
		
	def cashInData(self):
		if self.dataFileCount < 10:
			return False
		self.dataFileCount -= 10
		n = 0
		success_chance = round(random.uniform(0.45, 0.55)) + database_modifier
		for _ in range(10):
			c = round(random.random())
			if c <= success_chance:
				n += 2500
		self.cashCount += n
		return True
	
	def hireCollector(self):
		if self.cashCount < 100:
			return False
		self.collectorCount += 1
		self.cashCount -= 100
		return True
	
	def hireLaudromat(self):
		if self.cashCount < 50:
			return False
		self.cashCount -= 50
		self.laundromatCount += 1
		return True
	
	def buyBitcoin(self):
		if self.cashCount < 5000:
			return False
		self.cashCount -= 5000
		self.bitcoinCount += 1
		return True
	
	def sellBitcoin(self):
		if bitcoinCount < 1:
			return False
		self.bitcoinCount -= 1
		self.cashCount += 5000
		return True
