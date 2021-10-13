import numpy as np

class Employee:
    def __init__(self,id,name,email,age,gender):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.gender = gender

    def printInfo(self):
        printInfo = np.array([self.id,self.name,self.email,self.age,self.gender])
        print(printInfo)
        return " "

s1 = Employee(1, 'AA', 'AA@GMAIL', 17, 'F')
s2 = Employee(2, 'BB', 'bb@GMAIL', 19, 'M')
s3 = Employee(3, 'CC', 'cc@GMAIL', 57, 'F')
s4 = Employee(4, 'DD', 'dd@GMAIL', 47, 'M')
s5 = Employee(5, 'EE', 'ee@GMAIL', 97, 'F')
s6 = Employee(6, 'FF', 'ff@GMAIL', 37, 'M')
s7 = Employee(7, 'GG', 'gg@GMAIL', 97, 'F')
s8 = Employee(8, 'HH', 'hh@GMAIL', 67, 'M')
s9 = Employee(9, 'II', 'ii@GMAIL', 37, 'F')
s10=Employee(10, 'JJ', 'jj@GMAIL', 87, 'M')

theList = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]

class Node:
    def __init__(self,key=None,left=None,right=None,parent=None):
        self.key = key
        self.left= left
        self.right= right
        self.parent = parent

#creating class for all methods
class Binary_SearchTree():
    def __init__(self):
        self.root = None

#progam for insertion starts from here....................
    def insertNode(self, value, root):
        if self.root == None:
            self.root = Node(key=value)
            print(self.root.key.printInfo())
        else:
            if root.key.id > value.id:

                if root.left is None:
                    root.left = Node(key=value, parent=root)
                    print(root.left.key.printInfo())

                else:
                    self.insertNode(value, root.left)

            elif root.key.id < value.id:
                if root.right is None:
                    root.right = Node(key=value, parent = root)
                    print(root.right.key.printInfo())

                else:
                    self.insertNode(value, root.right)
            else:
                print("Value already exist.:-)")

#program for search starts from here................
    def searchNode(self, root, k):
        if root is None or root.key.id == k.id:
            if root is None:
                print("Value Not Found.")

            else:
                print("Value found :-")
                print(k.printInfo())
            return root
        else:
            if k.id < root.key.id:
                return self.searchNode(root.left, k)
            elif k.id > root.key.id:
                return self.searchNode(root.right, k)
            else:
                pass

#program for delete starts from here.........
    def deleteNode(self,root,k):
        if root is None:
            print("Value Not Found.")

        elif root.key.id == k.id:
            print("Value Deleted:- \n",root.key.printInfo())
            if root.left == None and root.right == None:
                print("Recently Deleted Value")
                print(root.key.printInfo())
                temp = root.parent
                if temp == None:
                    pass
                elif temp is not None:
                    if temp.right == root:
                        temp.right = None
                    elif temp.left == root:
                        temp.left = None                #IN DELETION >> remember we are deleting only those id's which are at leaf nodes.
                else:
                    pass
                root.key = None

            else:
                print("We can delete the value only at LEAF node here.") #konsa e
                return ""

        else:
            if k.id < root.key.id:
                return  self.deleteNode(root.left, k)
            elif k.id > root.key.id:
                return  self.deleteNode(root.right,k)
            else:
                pass


#printing evrything in the form of tree
    def printInOrder(self, root):
        if root is None:
            return
        lst = []
        lst.append(root)
        while lst:
            length = len(lst)
            while length > 0:
                temp = lst.pop(0)
                if temp.key == None:
                    print(None, end=' ')
                else:
                    print(temp.key.printInfo(), end=' ')
                if temp.left:
                    lst.append(temp.left)
                if temp.right:
                    lst.append(temp.right)

                length -= 1
            print('')


b = Binary_SearchTree()

i = 0
while True:
    print('''Instructions :-
        1-For Insertion In Tree
        2-To Search Value
        3-To Delete Element from the TREE
        4-Iterating Elements of tree
        5-Exit Program''')

    ans=int(input(' My Answer is >> '))
    if ans==1:
        x=int(input('Enter id uh want to insert value for::'))
        b.insertNode(theList[x-1],b.root)
        print('')

    elif ans==2:
        x=int(input('Enter id uh want to search value for::'))
        b.searchNode(b.root,theList[x-1])
        print('')

    elif ans == 3:
        x = int(input('Enter id uh want to delete::'))

        b.deleteNode(b.root,theList[x-1])
        print('')

    elif ans==4:
        print('\n','--------------------------------------------------------------------------------------------')
        print('Binary Search Tree:::')
        b.printInOrder(b.root)
        print('')

    elif ans==5:
        print('\nThank You ^_^')
        break

    else:
        print('invalid input')



