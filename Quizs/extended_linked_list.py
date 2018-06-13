# Written by **** for COMP9021

from Quizs.linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        if len(self) < 3:
            return
        min_elements = self.head.value
        p = self.head
        while p != None:
            if min_elements > p.value:
                min_elements = p.value
            p = p.next_node
        p = self.head
        if p.value == min_elements:
            q = self.head.next_node
            while q != None:
                q = q.next_node
            LL = LinkedList()
            LL.append(p.value)
            LL.append(q.value)
            while LL.__len__() < len(self):
                if p.next_node == None:
                    p = self.head.next_node
                    q = self.head
                elif p.next_node.next_node != None and p.next_node != None:
                    q = p.next_node
                    p = p.next_node.next_node
                else:
                    q = p.next_node
                    p = self.head
                LL.append(p.value)
                LL.append(q.value)
            p = self.head
            q = LL.head
            while p != None:
                p.value = q.value
                p = p.next_node
                q = q.next_node
        else:
            p = self.head.next_node
            q = self.head
            while p.value != min_elements:
                p = p.next_node
                q = q.next_node
            LL = LinkedList()
            LL.append(p.value)
            LL.append(q.value)
            while LL.__len__()<len(self):
                if p.next_node == None:
                    p = self.head.next_node
                    q = self.head

                elif p.next_node.next_node!=None and p.next_node!=None:
                    q = p.next_node
                    p=p.next_node.next_node
                else:
                    q=p.next_node
                    p=self.head

                LL.append(p.value)
                LL.append(q.value)
            p=self.head
            q=LL.head
            while p!=None:
                p.value=q.value
                p=p.next_node
                q=q.next_node