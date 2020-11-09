from random import randint

def make_fair_dice(sides):
	''' Создание игральной кости с количеством сторон sides 
	(кидание костяшки)
	'''
	assert type(sides) == int and sides >= 1, 'Illegal value for sides'
	def dice():
		return randint(1, sides)
	return dice
	
four_sided_dice = make_fair_dice(4)
six_sided_dice = make_fair_dice(6)

#four = make_fair_dice(4)
#print(four())

def roll_dice(num_rolls, dice=six_sided_dice, who='Grand Jedi Master Yoda'):
	'''кидание костяшки несколько раз'''
	assert type(num_rolls) == int, 'num_rolls must be an integer.'
	assert num_rolls > 0, 'Must roll at least once.'
	score = 0
	while num_rolls!=0:
		score += dice()
		if dice()==1:
			return 1
		num_rolls -= 1
	return score
	
#print(roll_dice(5))

commentary = True

def take_turn(num_rolls, opponent_score, dice=six_sided_dice, who='Grand Jedi Master Yoda'):
	assert type(num_rolls) == int, 'num_rolls must be an integer.'
	assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
	if commentary:
		print(who, 'is going to roll', num_rolls, 'dice')
	if num_rolls==0:
		score=opponent_score
		return score
	else:
		return roll_dice(num_rolls)
	
#print(take_turn(1,24))

'''
def ending(score, n):
	while score>=10:
		score-=10
	if score == n:
		return True
	return False
	
#print(multiplicity(17,5))'''

def is_prime(n):
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True
	
def next_prime(n):
	n=n+1
	while is_prime(n)!=True:
		n+=1
	return n
		
#print(next_prime(7))

def HogtimusPrime(score):
	if is_prime(score)==True:
		return next_prime(score)
	return False
	
print(HogtimusPrime(10))

def Touchdown(score, n):
	if score%n==0:
		return int(score+(score/n))
	return False
		
#print(Touchdown(12,6))

def FreeBacon(num_rolls, opponent_score):
	if num_rolls==0:
		return int(opponent_score/10)+1
	return False

#print(FreeBacon(0,32))