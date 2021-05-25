x =  input("enter the string")
w = ' '
for i in x:
	w = i + w
print(ord(w))
print(ord(x))
if x == w:
	print(f'{x} is a  palindrome')
else:
	print(f'{x} is not a palindrome')

