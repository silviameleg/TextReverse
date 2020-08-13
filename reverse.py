def reversed():
    #Welcome (initial) message for user
    print ('''\nWould you like to see how your name looks like reversed?
    Or perhaps a text or a number :)''')
    
    #find out if user wants to reverse something else (used in the next function)
    def doagain():
        again = input('''Would you like to try something else?
        Type capital Y for yes and capital N for no: ''')
        if again == 'Y':
            repeated()
        elif again == 'N':
            print('See you soon!')
        else:
            doagain()
            
    #get imput from user
    def repeated():
        myStr = input('Just type it in here and we\'ll do the magic: ')
        newStr = myStr[::-1]
        print(newStr)
        doagain()
    repeated()

    
reversed()