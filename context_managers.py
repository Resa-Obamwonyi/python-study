#implementing a context manager as a class

#file opening context managers
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()


#using the with statement with the class
with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
