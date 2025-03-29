
    if count > 0:
        print(f"The number {search_number} is present in the array and appears {count} time(s).")
    else:
        print(f"The number {search_number} is not present in the array.")
search_number_in_array()      #I inserted these numbers : 11 12 3 12 4 8 10 and searched for number 12

#QUESTION NUMBER 2
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
        print(f"Pushed element {element} onto the stack.")
    def pop(self):
        if not self.is_empty():
            popped_element = self.stack.pop()
            print(f"Popped element {popped_element} from the stack.")
            return popped_element
        else:
            print("Stack is empty. Cannot pop element.")
            return None
    def is_empty(self):
        return len(self.stack) == 0
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
#QUESTION NUMBER 3
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            print("Stack overflow")
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
class LinearQueueUsingStacks:
    def __init__(self, capacity):
        self.stack1 = Stack(capacity)
        self.stack2 = Stack(capacity)
    def enqueue(self, element):
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        self.stack1.push(element)
        print(f"Enqueued element {element}")
    def dequeue(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise IndexError("dequeue from empty queue")
        dequeued_element = self.stack2.pop()
        print(f"Dequeued element {dequeued_element}")
        return dequeued_element
    def peek(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise IndexError("peek from empty queue")
        peeked_element = self.stack2.peek()
        print(f"Peeked element {peeked_element}")
        return peeked_element

queue = LinearQueueUsingStacks(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.dequeue()
queue.peek()

#QUESTION 4
def bubble_sort_alphabets(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if ord(arr[j]) > ord(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
alphabets = ['d', 'a', 'c', 'b', 'e']
sorted_alphabets = bubble_sort_alphabets(alphabets)
print("Sorted Alphabets:", sorted_alphabets)
# QUESTION NUMBER 5
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [11, 12, 3, 12, 4, 8, 10]
mergeSort(arr)
print("Sorted array:", arr)
#QUESTION NUMBER 6
def deleteElement(array, index):
    if index < 0 or index >= len(array):
        print("Invalid index.")
        return array

    del array[index]
    return array
array = [3, 7, 1, 9, 4]
index_to_delete = 2
modified_array = deleteElement(array, index_to_delete)
print("Modified Array:", modified_array)
