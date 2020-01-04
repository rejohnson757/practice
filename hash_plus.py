spam = '####'
bacon = "+#+="

def hash_plus(lst):
	hashes = lst.count('#')
	plus = lst.count('+')
	print([hashes, plus])
hash_plus(spam)
hash_plus(bacon)
