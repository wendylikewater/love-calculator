print('welcome to love calculator')
name1 = input('what is your name \n')
name2 = input('what is their name \n')
together = name1 + name2.lower()
t= together.count('t')
r= together.count('r')
u= together.count('u')
e= together.count('e')
true = t + r + u + e
l= together.count('l')
o= together.count('o')
v= together.count('v')
e= together.count('e')
love= l + o + v + e
compatability = str(true) + str(love)
int_compatability = int(compatability)
if (int_compatability < 10) or (int_compatability > 90):
 print(f'you are {int_compatability}, you are like coke and mentos')
elif (int_compatability >= 40) or (int_compatability <= 50):
  print(f'you are {int_compatability},you are alright together')
else:
  print(f'your score is {int_compatability}')