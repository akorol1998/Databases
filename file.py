#! /Users/akorol/Desktop/Python/DB/env/bin/python
import numpy as np
import timeit

class Entity:
	def __init__(self, name, age, passport):
		self.name = name
		self.age = age
		self.passport = passport


class General:
	size = 5381
	lst = np.empty((size,1), dtype=Entity)

	def element(self, key):
		hash = self.HASH(key)
		index = hash % self.size
		if self.lst[index][0] and self.lst[index][0].passport != key:
			index = self.collision_getter(index, key)
		elif self.lst[index][0] == None:
			return "No such element found..."
		return self.lst[index]			

	def insert(self, el):
		hash = self.HASH(el.passport)
		index = hash % self.size
		if self.lst[index]:
			index = self.collision_resolver(index)
		self.lst[index][0] = el

	def HASH(self, key):
		hash = 5381
		c = 0;
		for i in key:
			hash = ((hash<<5)  + hash) + ord(i)
		return hash

	def collision_resolver(self, index):
		for i in range(self.size):
			i = i**2;
			if i + index > self.size:
				arbit = np.empty((i,1), dtype=self.lst.dtype)
				self.lst = np.vstack((self.lst, arbit))
			if not self.lst[index + i]:
				return index + i
		return 0

	def collision_getter(self, index, key):
		for i in range(self.size):
			i = i**2;
			if self.lst[index + i][0].passport == key:
				return index + i
		return 0

def access():
	with open("read.txt", 'r') as file:
		lst = file.read()
		li = lst.split()
	temp = []
	for i in li:
		temp.append(Entity("RandomName", 21, i))
	gen = General()
	for i in temp:
		gen.insert(i)
	lst1 = "KVWl0Pi \
			58fyHST\
			XxBROj5\
			19u43Qy\
			nr8IuKJ\
			YsRll7Z\
			vzs2LLh\
			eUsyrOn\
			VJNLcsK\
			Q9h2f8D\
			y414EQG\
			s4R3S2s\
			VbonNTB\
			2uDhzOL\
			O8ptKx4"
	spl = lst1.split()
	for i in spl:
		print(gen.element(i))


def main():
	print(timeit.timeit("access()","from __main__ import access", number=1))
	

if "__main__" == __name__:
	main()
