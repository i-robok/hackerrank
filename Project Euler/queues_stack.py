import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.fifo_queue = []
        self.lifo_stack = []
    
    def pushCharacter(self, ch):
        self.fifo_queue.append(ch)
        
    def enqueueCharacter(self, ch):
        self.lifo_stack.append(ch)
        
    def popCharacter(self):
        return self.lifo_stack.pop(0) 
        
    def dequeueCharacter(self):
        return self.fifo_queue.pop(-1)

if __name__ == '__main__':
    # read the string s
    s=input()
    #Create the Solution class object
    obj=Solution()   
    
    l=len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])
    
    print(f'fifo_queue: {obj.fifo_queue}')
    print(f'lifo_stack: {obj.lifo_stack}')

    isPalindrome=True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    ''' 
    for i in range(l // 2):
        a = obj.popCharacter()
        b = obj.dequeueCharacter()
        print(f'a: {a}, b: {b}')
        if  a != b:
            isPalindrome=False
            break
    #finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, "+s+", is a palindrome.")
    else:
        print("The word, "+s+", is not a palindrome.")    
    
    #print(f'fifo_queue: {obj.fifo_queue}')'