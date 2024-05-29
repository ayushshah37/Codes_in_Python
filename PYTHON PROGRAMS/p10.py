from BTrees.IIBTree import IIBTree
import time
def print_menu():
    print("enter what do u wanna perform \n1.input\n2.search\n3.print\n4.exit")

    choice=int(input(" enter : "))
    return choice 
b_tree=IIBTree(order=5)
while True :
    choice = print_menu()
    if(choice==1):
        insertion_start_time=time.time()
        value=int(input("enter value : "))
        b_tree.insert(value,value)
        insertion_end_time=time.time()
        print("Element inserted in the B-tree")
        print(f"Insertion Time: {round((insertion_end_time-insertion_start_time)*1000,3)} milliseconds")
    elif(choice==2):
        value=int(input("Enter Value : "))
        search_start_time=time.time()
        if i in b_tree:
            search_end_time=time.time()
            print("element found in the b tree")
            print(f"Element search time :{round((search_end_time-search_end_time)*1000,3)}")
        else:
            print("value not found in the tree")
    elif(choice==3):
        print("B-Tree :")
        print(list(b_tree.items()))

    elif(choice==4):
        print("Exiting the program ")
        break
    else:
        print("enter the correct number again pls ")