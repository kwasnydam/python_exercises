class myFileHandler():

    def __init__(self, filename=''):
        self.filename = filename
        self.opened = False
    def open(self):
        try:
            file = open(self.filename, mode = 'r')

        except FileNotFoundError:
            print('ERROR: There is no file {}'.format(self.filename))

        else:
            self.file = file
            self.opened = True
            print('File {} opened'.format(self.filename))

        finally:
            print('I dont care if it worked tbh xD')
    def read(self):
        if self.opened:
            print(self.file.read())
        else:
            print('File not opened')
    def close(self):
        if self.opened:
            self.file.close()
        else:
            print('No file to close')


def main():
    fileHandler = myFileHandler('mydata2.txt')
    fileHandler.open()
    fileHandler.read()
    fileHandler.close()

    fileHandler = myFileHandler('mydata3.txt')
    fileHandler.open()
    fileHandler.read()
    fileHandler.close()

main()
