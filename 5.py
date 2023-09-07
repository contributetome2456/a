def operation(wordlist):
    ans = list()

    for word in wordlist:
        if(word[0] == word[-1] and len(word )>= 2):
            ans.append(word)
    
    return ans

def main():
    wordlist = []
    n = int(input('enter the number of words in the list: '))

    for i in range(0,n):

        word = input('Enter the word: ')
        wordlist.append(word)
    
    print('Resulting words: ')
    print(operation(wordlist))

main()