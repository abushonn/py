class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
            return self.data


class LinkedList:
    def __init__(self, name='???'):
        self.head = Node()
        self.name = name

        print('List ' + self.name + ' created.' )

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while (cur.next != None):
            cur = cur.next
        cur.next = new_node

        print('added : ' + str(new_node))

    def display(self):
        elems=[]
        curr_node = self.head.next
        while(curr_node != None):
            # print('curr: ' + str(curr_node.data))
            elems.append(curr_node.data)
            curr_node = curr_node.next

        print(elems)

    def length(self):
        cur = self.head
        count = 0
        while (cur.next != None):
            cur = cur.next
            count = count + 1

        return  count


    def get(self, index):
        if (index >= self.length()):
            print('ERROR: index out of scope!!! Length={}, index={}'.format(self.length(), index))
            return
        cur = self.head.next  # self.head is an emty element
        for i in range(index):
            cur = cur.next

        return  cur

    def erase(self, index):
        if (index >= self.length()):
            print('ERROR: index out of scope!!! Length={}, index={}'.format(self.length(), index))
            return
        cur = self.head.next  # self.head is an emty element
        for i in range(index-1):
            cur = cur.next

        del_node = cur.next
        cur.next = del_node.next

        #return deleted node
        return  del_node


print('============ Test Node=================')
n1 = Node("111")
print(n1)

print('============ Test List: create and append =================')
lst1 = LinkedList('lst1')
lst1.append('10')
lst1.append('20')
lst1.append('30')
lst1.append('40')
print('The list after adding:')
lst1.display()

print('============ Test List: count, get =================')
print('lst1 length : ' + str(lst1.length()))

print(lst1.name + '[2] : ' + str(lst1.get(2)))
print(lst1.name + '[5] : ' + str(lst1.get(5)))

print('============ Test List: erase =================')
print('Before:')
lst1.display()
print('Erasing element index=2:')
lst1.erase(2)
print('After:')
lst1.display()