def ispalindrome(s):
	return s== s[::-1]
s= input('enter the word:')
res = ispalindrome(s)
if res :
	print('yes')
else:
	print('no')
