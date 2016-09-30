from guess_word import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


hangmen = []
def main():	
	
	print '_'*20
	print '-'*20
	print '`'*20
	print 'start game'
	ans, l = choose_answer()
	sw = ['-']*l
	
	time = 0
	life = 10
	pattern_l = [a_c] * l
	al_guess = []
	wl = word_l

	while life > 0:

		for line in hangmen[100-10*life:110-10*life]:
			print line
		print 'secret word:', ''.join(sw)
		print 'time: ',time
		print 'life: ',life
		print 'input a char: '
		c = raw_input()
		while c not in a_c or not c:

			print 'error input'
			if c == '.':
				print 'give you a suggesstion. why not try' ,next_char(wl, al_guess) ,'?'
			if c == ',':
				c = next_char(wl, al_guess)
				print 'auto try ', c
				break
			print 'input a char: '
			c = raw_input()
		
		wl = re_get_word_list(word_l, pattern_l)
		al_guess.append(c)

		ca = compare_ans(ans, c)

		#print 'pl   :',' '.join(pattern_l)
		if c not in ca:
			life -= 1
			print 'you lost a life'

		for i in range(l):
			if ca[i] == c:
				pattern_l[i] = c
			else:
				pattern_l[i] = ''.join(pattern_l[i].split(c))

		for i in range(l):
			if ca[i] == c:
				sw[i] = c

		if '-' not in sw:
			print 'you win!'
			print 'ans:', ans
			return 1
	else:
		for line in hangmen[100-10*life:110-10*life]:
			print line
		print 'you lost.'
		print 'ans:', ans
		return 0



def hang_man():
	with open('hangmen.txt','r') as inf:
		for line in inf.readlines():
			hangmen.append(line[0:-1])


if __name__ == '__main__':
	init()
	hang_man()
	main()