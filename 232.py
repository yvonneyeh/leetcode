# 232. Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_front = []
        self.stack_back = []

        # stack_front[0] is the queue front
        # stack_back[0] is the queue back

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        while self.stack_back:
            self.stack_front.append(self.stack_back.pop())

        self.stack_front.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        while self.stack_front:
            self.stack_back.append(self.stack_front.pop())

        return self.stack_back.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """

        while self.stack_front:
            self.stack_back.append(self.stack_front.pop())

        return self.stack_back[-1]



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        return not self.stack_front and not self.stack_back


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack1.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack2)!=0:
            self.stack2.pop()
        else:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            self.stack2.pop()

    # @return an integer
    def peek(self):
        if len(self.stack2)!=0:
            return self.stack2[-1]
        else:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    # @return an boolean
    def empty(self):
        if len(self.stack1)==0 and len(self.stack2)==0:
            return True
        else:
            return False
