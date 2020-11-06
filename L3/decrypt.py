from cryptogram import Cryptogram


class Decrypt:
	def __init__(self, data):
		self.data = data
		self.cryptograms = []

		self.letterFreq = {'a': 89, 'i': 82, 'o': 78, 'e': 77, 'z': 56, 'n': 55, 'r': 47, 'w': 47, 's': 43, 't': 40,
		                   'c': 40, 'y': 38, 'k': 35, 'd': 33, 'p': 31, 'm': 28, 'u': 25, 'j': 23, 'l': 21, 'b': 15,
		                   'g': 14, 'h': 11, 'f': 3, 'q': 1, 'v': 1, 'x': 1, ' ': 100, ',': 16, '.': 10, '-': 10,
		                   '"': 10, '!': 10, '?': 10, ':': 10, ';': 10, '(': 10, ')': 10}

		self.addLetters()
		self.createCryptograms()

	# Adding numbers and big letters to letters alphabet
	def addLetters(self):
		for i in range(48, 91):
			if i in range(58, 65):
				pass
			else:
				self.letterFreq[chr(i)] = 10

	def createCryptograms(self):
		for line in self.data.splitlines():
			self.cryptograms.append(Cryptogram(line))

	def findKey(self):
		key = []
		longestString = max(len(cryptogram.letters) for cryptogram in self.cryptograms)

		for i in range(longestString):
			possibleKeys = {}
			for cryptogram in self.cryptograms:
				if i >= len(cryptogram.letters):
					continue

				for letter in self.letterFreq.keys():
					possibleKey = ord(cryptogram.letterByIdx(i)) ^ ord(letter)
					possibleKeys[possibleKey] = possibleKeys.get(possibleKey, 0) + self.letterFreq[letter]

			sortedKeys = sorted(possibleKeys.keys(), key=lambda k: possibleKeys[k], reverse=True)

			possibleLetter = ord(' ')
			count = 0

			for letter in sortedKeys:
				counter = 0

				for cryptogram in self.cryptograms:
					if i >= len(cryptogram.letters):
						continue
					if (chr(ord(cryptogram.letterByIdx(i)) ^ letter)) in self.letterFreq.keys():
						counter += 1

				if counter > count:
					count = counter
					possibleLetter = letter

			key.append(possibleLetter)
		return key

	def decrypt(self):
		key = self.findKey()
		result = ""

		for cryptogram in self.cryptograms:
			for i in range(0, len(cryptogram.letters)):
				result += chr(ord(cryptogram.letterByIdx(i)) ^ key[i])
			result += "\n"

		return result


def main():
	with open('data.txt', 'r') as file:
		decrypt = Decrypt(file.read())

	txt = decrypt.decrypt()
	print(txt)


if __name__ == '__main__':
	main()
