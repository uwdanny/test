#! /usr/bin/python

# this is the first comment
SPAM = 1                 # and this is the second comment
                         # ... and now a third!
STRING = "# This is not a comment."

hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the beginning of the line is\
 significant."

print hello

a, b = 0, 1
while b < 10:
	print b,
	a, b = b, a+b
print

#x = int(raw_input("please enter an integer: "))
x = 1

if x < 0:
	x = 0
	print "negative value ==> 0"
elif x == 0:
	print 'zero'
elif x == 1:
	print 'single'
else:
	print 'more'

print
a = ['cat', 'window', 'defenestrate']
for x in a:
	print x, len(x)

print
a = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print i, a[i]

print
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print n, 'equals', x, '*', n/x
			break
	else: 
		print n, 'is a prime number'

print
def fib(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

print fib(2000)

print

def ask_ok(prompt, retries=4, complaint='yes or no, please!'):
	while True:
		ok = raw_input(prompt)
		if ok in ('y', 'yes', 'ye'):
			return True
		if ok in ('n'):
			return False
		retries = retries - 1
		if retries < 0:
			raise IOError('refusal')
		print complaint

#ask_ok('do you want to quit')

i = 5

def f(arg=i):
	print arg
	
i = 6
f()

print
def f(a, L=None):
	if L is None:
		L = []
	L.append(a)
	return L

print f(1)
print f(2)
print f(3)
print f(4)

print
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

parrot(1, state='hello kitty')

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

write_multiple_items(open('a.out', 'w'), ' ', '1', '2')

print
print range(3, 6)
args = [3, 6]
print range(*args)
