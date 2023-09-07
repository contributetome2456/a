def main():

    sentence = input('Enter the sentnce: ')

    mylist = sentence.split()
    my_set = set(mylist)

    print(sorted(my_set))

main()