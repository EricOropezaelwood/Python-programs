'''
katakanaTest,py
Eric Oropezaelwood
25 September 2015
A quiz app that tests the users knowledge of katakana and Japanese vocabulary
'''

class Student:
	def __init__(self, name):
		self.name = name
		print("Konichiwa {0}".format(self.name), "san")

print("What is your name?")
response = input()
student1 = Student(response)

#start of alpha class
class alpha():

	def basics(self):
		katakanaBasic = {
			'ア': "a",
			'イ': "i",
			'ウ': "u",
			'エ': "e",
			'オ': "o",
			'ン': "n"
			}

		correct = 0
		incorrect = 0
		for k, v in katakanaBasic.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)

		return katakanaBasic

	def k(self):
		katakanaK = {
			'カ': "ka",
			'キ': "ki",
			'ク': "ku",
			'ケ': "ke",
			'コ': "ko"
			}

		correct = 0
		incorrect = 0
		for k, v in katakanaK.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)

		return katakanaK

	def s(self):
		katakanaS = {
			'サ': "sa",
			'シ': "shi",
			'ス': "su",
			'セ': "se",
			'ソ': "so"
			}

		correct = 0
		incorrect = 0
		for k, v in katakanaS.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)

		return katakanaS
	def t(self):
		katakanaT = {
			'タ': "ta",
			'チ': "chi",
			'ツ': "tsu",
			'テ': "te",
			'ト': "to"
			}

		correct = 0
		incorrect = 0
		for k, v in katakanaT.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)

		return katakanaT

	def n(self):
		katakanaN = {
			'ナ': "na",
			'ニ': "ni",
			'ヌ': "nu",
			'ネ': "ne",
			'ノ': "no"
			}

		correct = 0
		incorrect = 0
		for k, v in katakanaN.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)

		return katakanaN

	def h(self):
		katakanaH = {
			'ハ': "ha",
			'ヒ': "hi",
			'フ': "fu",
			'ヘ': "he",
			'ホ': "ho"
			}

		correct = 0
		incorrect = 0
		for k, v in katakanaH.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)

		return katakanaH

	def m(self):
		katakanaM = {
			'マ': "ma",
			'ミ': "mi",
			'ム': "mu",
			'メ': "me",
			'モ': "mo"
			}

		correct = 0
		incorrect = 0
		for k, v in katakanaM.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)

		return katakanaM

	def y(self):
		katakanaY = {
			'ヤ': "ya",
			'ユ': "yu",
			'ヨ': "yo"
			}

		correct = 0
		incorrect = 0
		for k, v in katakanaY.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)

		return katakanaY
	def r(self):
		katakanaR = {
			'ラ': "ra",
			'リ': "ri",
			'ル': "ru",
			'レ': "re",
			'ロ': "ro"
			}

		correct = 0
		incorrect = 0
		for k, v in katakanaR.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)

		return katakanaR
	def w(self):
		katakanaW = {
			'ワ': "wa",
			'ヲ': "wo"
			}

		correct = 0
		incorrect = 0
		for k, v in katakanaW.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)

		return katakanaW

#end of aplha class

#start of nouns!!!!!!!!

class noun():
	def locations(self):
		places = {
		"としょかん":"library",
		"といれ":"toilet",
		"おてら":"temple",
		"こうえん":"park",
		"スーパー":"supermarket",
		"デパート":"department store",
		"バスてい":"bus stop",
		"びょういん":"hospital",
		"ホテル":"hotel",
		"ほんや":"bookstore",
		"まち":"town",
		"レストラン":"restaurant"
		}
		correct = 0
		incorrect = 0
		for k, v in places.items():

			print("translate: ", k)
			answer = input()
			if answer == v:
				print("correct")
				correct = correct + 1
			else:
				print("incorrect, answer: ", v)
				incorrect = incorrect + 1
		print("correct: ",correct, "incorrect: ", incorrect)
		

		# activates Japanese bot, a highly intelligent robot whose calculations determine one's lifespan in Japan based on their results
		if correct < 1:
			print("Beep boop \"My calculations suggest you would survive 1/2 a day in Japan\" beep boop")
		elif correct < 5:
			print("Beep boop \"My calculations suggest you would survive 1 week in Japan\" beep boop")
		else:
			print("Beep boop \"My calculation suggest you would be able to order ramen in Japan, CONGRATULATIONS! おめでとうございます!\" beep boop")
		return places

def main():
	
	again = "yes"
	#Create objects in order to use classes
	aChoice=alpha()
	bChoice=noun()
	while again != "no":
		#prompts the user on what to study
		print("What do you want to study: locations or katakana?")
		choice1 = input()
		
		#prompt for katakana review
		if choice1 == "katakana":
			print("choose a category: a-o/n, k, s, t, n, h, m, y, r, or w?")
			choice = input()
			if choice == "a-o/n":
				aChoice.basics()
			elif choice == "k":
				aChoice.k()
			elif choice == "s":
				aChoice.s()
			elif choice == "t":
				aChoice.t()
			elif choice =="n":
				aChoice.n()
			elif choice =="h":
				aChoice.h()
			elif choice =="m":
				aChoice.m()
			elif choice =="y":
				aChoice.y()
			elif choice =="r":
				aChoice.r()
			elif choice =="w":
				aChoice.w()

		#execute locations() and begin quizzing
		elif choice1 =="locations":
			bChoice.locations()
	
		print("Do you want to go again? yes or no")
		again = input()
main()






