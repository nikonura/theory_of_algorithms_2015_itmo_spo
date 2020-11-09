'''
деревья
T=<N,E>
 N=nodes(узлы)
 E=edges(ребра)

у дерева всегда есть корень, причём только один.
ели у дерева(корня) есть только 2 потомка, то оно называется бинарным.
дерево называется пустым, если нет ни листов, ни ребер, или состоять из 
корня и нуля из более поддеревьев.
'''
def binary_tree(value):
	return [value,[],[]]

def get_left_child(node):
	return node[1]
	
def get_right_child(node):
	return node[2]
	
def get_root_value(node):
	return node[0]
	
#вставка потомка влево 
def insert_left(root,value):
	child=root.pop(1) #выталкиваем первый элемент
	if len(child)>1: 
		root.insert(1,[value,child,[]]) #меняем старый список на новый, попросту вставляем значение 1, значение и старый ребёнок как потомок
	else:
		root.insert(1,[value,[],[]]) #если список пустой, заменяем его на пустой
		
[2,
 [9,[4,[],[]],[],[]]
]

#вставка потомка вправо
def insert_right(root,value):
	child=root.pop(2)
	if len(child)>1:
		root.insert(2,[value,[],child])
	else:
		root.insert(2,[value,[],[]])
		
'''
[1,[2,[],[]].[3,[],[]]]
хотим вставить левого потомка в левый потомок
insert_left(get_left_child(tree),4)
получим
[1,[2,[4,[],[]],[]],[3,[],[]]]
хотим вставить правого потомка в потомки потомка 4
insert_right(get_left_child(get_left_child(tree)),5)
'''

#поиск элемента			
def find(tree,e):
	if not tree:
		return False
	if e==get_root_value(tree):
		return True
	return find(get_left_child(tree),e) or find(get_right_child(tree),e)
	

'''ДЗ создать функцию binary_search_tree [1,[2,[3,[4,[],[]],[]],[]],[]]'''


#есть корень, все левые элементы которого меньше правых
def find1(tree,e):
	if not tree:
		return False
	if e==get_root_value(tree):
		return True
	if get_left_child<e:
		return find(get_left_child(tree),e) 
	else:
		return find(get_right_child(tree),e)
		
tree=binary_tree(21)
insert_left(tree,13)
insert_right(tree,33)
insert_left(insert_left(tree,4))
insert_right(insert_left(tree,15))
insert_left(insert_right(tree,26))
insert_right(insert_right(tree,37))

print(find1(tree,15))


def foo(n,tabs=o):
	if n!=0:
		print(tabs*'\t',n)
		return foo(n-1,tabs+1)
		
def preorder(tree,tabs=0):
	if tree:
		print(tabs*'\t',get_root_value(tree))
		preorder(get_left_child(tree).tabs+1)
		preorder(get_right_child(tree).tabs+1)

import operator
"+"-add()
"-"-sup()
"*"-mul()
"/"-truediv()}
operator.add(3,5)

'''
ops={'+': operator.add, \
'-': operator.sub, \
'*': operator.mul, \
'\': operator.truediv}

ops['+'](3,5)

словарь - это объекты типа слова-значения

phones={'Mike':1111, 'john':2222, 'Pit':3333}
phones['Mike']

ключами могут быть только строки и целые числа

chars={'a':1, 'b':2, 'c':3, 'd':4}
chars
chars.keys()
sorted(chars.keys())
sorted_chars=sorted(chars.keys())
'''

def evaluate(exp):
	left_op=get_left_child(exp)
	right_op=get_right_child(exp)
	if left_op and right_op:
		op=ops[get_root_value(exp)]
		return op(evaluate(left_op),evaluate(right_op))
	else:
		return get_root_value(exp)
		
def postorder_evaluate(exp):
	ops={'+': operator.add, '-': operator.sub, '*': operator.mul, '\': operator.truediv}
	left_op=get_left_child(exp)
	right_op=get_right_child(exp)
	if left_op and right_op:
		op=ops[get_root_value(exp)]
		left_op = postorder_evaluate(get_left_child(exp))
		right_op = postorder_evaluate(get_right_child(exp))
		return op((left_op),(right_op))
	else:
		return get_root_value(exp)