

encriptionKey = {"a" : "AA", "b" : "AB", "c" : "AC", "d" : "AD", "e" : "AE",
				 "f" : "BA", "g" : "BB", "h" : "BC", "i" : "BD", "j" : "BD", "k" : "BE",
				 "l" : "CA", "m" : "CB", "n" : "CC", "o" : "CD", "p" : "CE",
				 "q" : "DA", "r" : "DB", "s" : "DC", "t" : "DD", "u" : "DE",
				 "v" : "EA", "w" : "EB", "x" : "EC", "y" : "ED", "z" : "EE", " ": " "}

decriptionKey = {"AA" : "a", "AB" : "b", "AC" : "c", "AD" : "d", "AE" : "e",
				 "BA" : "f", "BB" : "g", "BC" : "h", "BD" : "i", "BD" : "j", "BE" : "k",
				 "CA" : "l", "CB" : "m", "CC" : "n", "CD" : "o", "CE" : "p",
				 "DA" : "q", "DB" : "r", "DC" : "s", "DD" : "t", "DE" : "u",
				 "EA" : "v", "EB" : "w", "EC" : "x", "ED" : "y", "EE" : "z", " ": " "}


def encript(message):
	#codedMessage = str(map(lambda n: encriptionKey[n], message))
	codedMessage = ""
	for i in message:
		codedMessage += encriptionKey[i]
	return codedMessage


def decript(encriptedMessage):
	words = encriptedMessage.split(" ")
	decodedMessage = ""
	for i in words:
		for j in range(0, len(i), 2):
			temp = i[j] + i[j + 1]
			decodedMessage += decriptionKey[temp]
		decodedMessage += " "
	return decodedMessage


test = decript("BCCDCAAA CBDECCADCD")
print(type(test))
print(test)