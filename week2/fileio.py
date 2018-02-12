'''
#Problem 1
file_name = input('What is the name of the file? ')
with open(file_name, 'r') as file_handle:
    contents = file_handle.read()
print(contents)

#Problem 2
file_name = input('What is the name of the file? ')
contents = input('What would you like to write into the file? ')
with open(file_name, 'w') as file_handle:
    file_handle.write(contents)


#Problem 3
import dictex
file_name = input('What is the name of the file? ')
with open(file_name, 'r') as file_handle:
    contents = file_handle.read()
dictex.letter_histogram(contents)
dictex.word_histogram(contents)
'''
#Problem 4
import matplotlib.pyplot as mat
import json
'''
data = {
  "data": [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4]
  ]
}
with open('data.json', 'w') as fh:
  json.dump(data, fh)
with open('data.json', 'r') as fh:
  data = json.load(fh)
  print(data)
'''
name = input('What is the json you wish to graph? ')
def jplot(name):
    x = []
    y = []
    with open(name, 'r') as fh:
        data = json.load(fh)
    for i in range(len(data['data'][1])):
        for k in range(len(data['data'])):
            if i == 0:
                x.extend([data['data'][k][i]])
            else:
                y.extend([data['data'][k][i]])
    mat.plot(x,y)
    mat.show()
jplot(name)




    
    



