import os

with open('mydata.txt', mode ='a', encoding = 'utf-8') as myFile:
    myFile.write('some random text')

with open('mydata.txt', encoding = 'utf-8') as myFile:
    #read() readLine() readLines()
    print(myFile.read())

print(myFile.closed) #True, with block closes the myFile

#some os mathods
#os.rename("mydata.txt", "mydata2.txt")

#os.remove('mydata2.txt')

#os.mkdir('mydir')

#os.chdir('mydir')
print('Current Directory: ', os.getcwd())
#os.rmdir('mydir')

def fib(num = 10):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num-1)+fib(num-2)
        #print(result)
        return result

with open('mydata.txt', mode ='w', encoding = 'utf-8') as myFile:
    for k in range(10):
        myFile.write('{} \n'.format(fib(k)))
    myFile.write('good job sir!')
