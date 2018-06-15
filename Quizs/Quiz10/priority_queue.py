# Written by *** for COMP9021


from Quizs.Quiz9.binary_tree_adt import *


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()
        self.pq = [None]
        self.size = 0
    def insert(self, value):
        self.size += 1
        self.pq.append(value)
        self._bubble_up(self.size)
        list = []
        node_list = self.pq[1:]
        for i in node_list:
            list.append(BinaryTree(i))
        for i in range(self.size):
            if (2*i+1)<self.size:
                list[i].left_node=list[2*i+1]
            if (2*i+2)<self.size:
                list[i].right_node=list[2*i+2]
        self.value=list[0].value
        self.left_node=list[0].left_node
        self.right_node=list[0].right_node
    def _bubble_up(self,position):
        if position==1:
            return
        parent_position=position // 2
        if self.pq[position]<self.pq[parent_position]:
            self.pq[parent_position],self.pq[position] = self.pq[position],self.pq[parent_position]
            self._bubble_up(parent_position)