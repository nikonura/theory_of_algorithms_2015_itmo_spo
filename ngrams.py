'''
алгоритмы на строках

основная задача - разбивка строки на энграммы
N - грамма - "слово"
N варьирумая

N=2
[сл,ло,ов,во]
N=3
['сло','лов','ово']

'''
def ngram_generetor(word,n):
	ngrams=[]
	for i in range(len(word)-n+1):
		ngrams.append(word[i:i+n])
	return ngrams
	
def unique(L):
	r=[]
	for i in L:
		if i not in r:
			r+=[i]
	return r

def union(a,b):
	return unique(a+b)

def intersection(a,b):
	r=[]
	for i in a:
		for j in b:
			if i==j:
				r.append(i)
	return r
		
def jaccard_similarity(a,b):
	r1=len(intersection(a,b))
	r2=len(union(a,b))
	J = r1/r2
	return J

print(jaccard_similarity(["How", "many", "roads", "must", "a", "man", "walked", "down"],["How", "many", "roads", "in", "your", "city"])