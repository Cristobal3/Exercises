'''
#Problem 1
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
print(phonebook_dict['Elizabeth'])
phonebook_dict['Kareem'] = '938-489-1234'
del phonebook_dict['Alice']
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)

#Problem 2
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
email = ramit['email']
interest1 = ramit['friends'][0]
jas_email = ramit['friends'][0]['email']
interest2 = ramit['friends'][1]

#Problem 3
def letter_histogram(word):
    d = {}
    p = ''
    for x in range(len(word)):
        if word[x] == p:
            d[word[x]] += 1
            p = word[x]
        else:
            d[word[x]] = 1
            p = word[x]
    print(d)
letter_histogram('green')
'''
#Problem 4
def word_histogram(word):
    d = {}
    p = ''
    for x in range(len(word)):
        if word[x] == ' ':
            if d.get(p, 'new') == 'new':
                d[p] = 1
                p = ''
            else:
                d[p] += 1
                p= ''
        else:
            p += word[x]
        if x == len(word) -1:
            if d.get(p, 'new') == 'new':
                d[p] = 1
                p = ''
            else:
                d[p] += 1
                p= ''
    print(d)
word_histogram('to be or not to be')






