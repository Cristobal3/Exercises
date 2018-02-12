
book = {'Melissa': '584-394-5857', 'Igor': '857-485-2935'}
while True:
    print('Electronic Phone Book')
    print('=====================')
    print('1. Look up an entry')
    print('2. Set an entry')
    print('3. Delete an entry')
    print('4. List all entries')
    print('5. Quit')
    choice = int(input('What do you want to do? (1-5) '))
    if choice == 1:
        person = input('Name: ')
        if book.get(person, 'new') == 'new':
            print('That person is not in your contacts. Please try again.')
        else:
            print('Found entry for Melissa: ', book[person])

    elif choice == 2:
        person = input('Name: ')
        number = input('Phone Number: ')
        book[person] = number
        print('Entry stored for', person,'.')

    elif choice == 3:
        person = input('Name: ')
        if book.get(person, 'new') == 'new':
            print('That person is not in your contacts. Please try again.')
        else:
            del book[person]
            print('Deleted entry for', person)

    elif choice == 4:
        for x in book:
            print('Found entry for {person}: {number}'.format(person=x, number=book[x]))

    
    elif choice == 5:
        print('Byë')
        break