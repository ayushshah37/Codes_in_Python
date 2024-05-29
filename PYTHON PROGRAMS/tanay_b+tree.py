from bplustree import BPlusTree

def print_menu():
    print("\n**** B+ Tree ****")
    print("1. Insert")
    print("2. Search")
    print("3. Show Tree")
    print("4. Exit")
    return input("Enter your choice: ")

class SimpleSerializer:
    def serialize(self, obj, size):
        return str(obj).encode('utf-8').ljust(size, b'\0')

    def deserialize(self, data):
        try:
            return int(data.rstrip(b'\0').decode('utf-8'))
        except ValueError:
            # Return a default value (0) if deserialization fails
            return 0

bplus_tree = BPlusTree("D:/b1.db", order=3, serializer=SimpleSerializer())

while True:
    choice = print_menu()

    if choice == '1':
        value = int(input("Enter Element to Insert : "))
        # Encode the key as bytes and insert the value
        bplus_tree[str(value).encode('utf-8')] = str(value).encode('utf-8')
        print("Element inserted into the B+ tree.")
    elif choice == '2':
        value = int(input("Enter Element to Search : "))
        # Encode the search key as bytes
        search_key = str(value).encode('utf-8')
        if search_key in bplus_tree:
            # Decode the value when printing
            print("Value found in the tree:", bplus_tree[search_key].decode('utf-8'))
        else:
            print("Value not found in the tree")
    elif choice == '3':
        print("B+ Tree:")
        try:
            for key, _ in bplus_tree.items():
                print(key.decode('utf-8'))
        except Exception as e:
            pass
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")