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
        cur = self.head.next #self.head is an emty element
        if (index >= self.length()):
            print('ERROR: index out of scope!!!')
            return
        for i in range(index):
            cur = cur.next

        return  cur


print('============ Test Node=================')
n1 = Node("111")
print(n1)

print('============ Test List: create and append =================')
lst1 = LinkedList('lst1')
lst1.append('10')
lst1.append('20')
lst1.append('30')

print('============ Test List: count, get =================')
print('lst1 length : ' + str(lst1.length()))

print(lst1.name + '[2] : ' + str(lst1.get(2)))
print(lst1.name + '[5] : ' + str(lst1.get(5)))