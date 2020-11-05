class Cryptogram:

	def __init__(self, line):
		self.letters = []

		for byteStr in str(line).split(' '):
			self.letters.append(chr(int(byteStr, 2)))

	def letterByIdx(self, index):
		if index < len(self.letters):
			return self.letters[index]
		else:
			return '*'
