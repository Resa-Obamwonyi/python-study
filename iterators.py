box = []
def iterate():
    for i in 'python':
        box.append(i)
    return box


print(iterate())



class iterateSomething:
    def __init__(self,box):
        self.box = box
        self.firstnum = -1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.firstnum += 1
        return self.box[self.firstnum]


a=[1,2,3,4,5,6]
myList = iterateSomething(a)
it = iter(myList)



my_iter = iter([1,2,3,4,5,6])
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
