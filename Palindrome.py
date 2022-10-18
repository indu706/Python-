while True:
    s=input('Enter a line: ') #input
    def palindrome(s): #function
        print('original string:', s)
        r=s[::-1]
        print('Reversed string:', r)
        if s==r:
            print('Yes,string is a palindrome')
        else:
            print('No,string is not a palimdrome')
    palindrome(s)
    continue
