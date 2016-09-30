import re
import random
word_l = []
word_num = 333333
a_c = 'abcdefghijklmnopqrstuvwxyz'
def init():
	with open('count_1w.txt', 'r') as input_f:
		line = input_f.readline()
		while line:
			word_l.append(line.split('\t')[0])
			line = input_f.readline()
			if len(word_l)>=word_num:
				return 
	return

def choose_answer():
	ans = random.randint(0, len(word_l)-1)
	
	'''while len(word_l[ans]) != 8:
		ans = random.randint(0, len(word_l)-1) '''
	return word_l[ans], len(word_l[ans])

def next_char(known_list, al_guess=[]):
	char_time = dict()
	total_word = len(known_list)
	l = len(known_list[0])
	for word in known_list:
		for c in a_c:
			if c in word and c not in al_guess:
				char_time[c] = char_time.get(c, 0) + 1

	nc = 'a'
	maxc = 0
	for c in a_c:
		if char_time.get(c, 0) > maxc:
			maxc = char_time.get(c, 0)
			nc = c
	return nc


def re_get_word_list(word_list, pattern):
	known_list = []

	for word in word_list:
		flag = 0
		if len(word) != len(pattern):
			continue
		for i in range(len(word)):

			if word[i] not in pattern[i]:
				flag = 1
				break

		if flag == 0:
			known_list.append(word)
	return known_list

def compare_ans(ans, guess_char):
	t = ['-'] * len(ans)
	for i in range(len(ans)):
		if ans[i] == guess_char:
			t[i] = ans[i]
	return t

def main():	
	
	print '_'*20
	print '-'*20
	print '`'*20
	print 'start game'
	ans, l = choose_answer()
	print 'ans: ',ans
	
	pattern_l = [a_c] * l
	al_guess = []
	wl = word_l

	time = 0
	life = 10

	while life > 0:
		time += 1 
		#print 'time: ', time 
		wl = re_get_word_list(word_l, pattern_l)
		#if len(wl) < 26:
			#print wl

		if len(wl) == 1:
			#print 'only one'
			#print 'ans  :', wl
			#print 'life :', life
			return 1
		#print 'last_:', len(wl)
		nc = next_char(wl, al_guess)
		#print 'guess:', nc
		al_guess.append(nc)
		ca = compare_ans(ans, ''.join(nc))
		#print 'g_sta:', ''.join(ca)

		#print 'pl   :',' '.join(pattern_l)
		if nc not in ca:
			life -= 1
		#print 'life :',life	
		for i in range(l):
			if ca[i] == nc:
				pattern_l[i] = nc
			else:
				pattern_l[i] = ''.join(pattern_l[i].split(nc))
	#print 'false'
	#print wl
	return 0

if __name__ == '__main__':
	init()
	r = 0
	time = 1000
	for i in range(1,time+1):
		r += main()
		print r*1.0/i
