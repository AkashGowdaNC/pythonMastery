from collections import deque
stack=[]
stack.append(1) #push
stack[-1] #peek
stack.pop() #pop
not stack #empty check
queue=deque()
queue.append(10) #enqueue
queue.append(20)
queue.popleft() #dequeue
print(queue.popleft())
queue.appendleft(5)
def is_valid(s):
    stack=[]
    pairs={
        ')':'(',
        '}':'{',
        ']':'['

    }
    for char in s:
        if char in pairs:
            if not stack or stack[-1]!=pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack)==0


def reverse_string(s):
    stack = []

    for char in s:
        stack.append(char)

    result = ""

    while stack:
        result += stack.pop()

    return result
#linear serach 
def linear_search(numbers,target):
    for i in range(len(numbers)):
        if numbers[i]==target:
            return i
    return -1
numbers=[10,20,30,40,50]
print(linear_search(numbers,30))

#binary search 
def binary_search(numbers,target):
    left=0
    right=len(numbers)-1
    while(left<=right):
        mid=(left+right)//2
        if numbers[mid]==target:
            return mid
        elif numbers[mid]<mid:
            left=mid+1
        else:
            right=mid-1
    return -1
numbers=[10,20,30.40,50,60,70]
print(linear_search(numbers,60))
#bubble sort
"""n = len(numbers)

Find how many elements are in the list.

Example: If numbers = [5, 3, 8, 4], then n = 4.

for i in range(n):

Outer loop runs n times.

Each pass ensures the largest remaining element "bubbles up" to its correct position.

for j in range(0, n - i - 1):

Inner loop compares adjacent elements.

Notice n - i - 1:

After each outer loop, the last i elements are already sorted, so we don’t need to check them again.

if numbers[j] > numbers[j + 1]:

Compare the current element with the next one.

If the current element is bigger, they’re in the wrong order.

numbers[j], numbers[j + 1] = (numbers[j + 1], numbers[j])

Swap the two elements.

Python allows swapping in one line using tuple unpacking.

return numbers

After all passes, the list is sorted and returned."""
def bubble_sort(numbers):
    n=len(numbers)
    for i in range(n):
        for j in range(0,n-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=(numbers[j+1],numbers[j])
    return numbers
#selectionsort
"""for i in range(1, len(numbers)):

Start from the second element (i = 1) because the first element is trivially “sorted.”

Each iteration picks one element (key) and inserts it into the correct position among the already sorted part of the list.

key = numbers[i]

Store the current element we want to insert into the sorted portion.

j = i - 1

Start comparing key with elements before it (the sorted portion).

while j >= 0 and numbers[j] > key:

As long as we haven’t reached the beginning (j >= 0) and the current element is greater than key, keep shifting elements to the right.

numbers[j + 1] = numbers[j]

Move the larger element one position to the right to make space for key.

j -= 1

Step backward to continue checking earlier elements.

numbers[j + 1] = key

Once we find the correct spot, place key there.

return numbers

After all passes, the list is sorted."""
def insertion_sort(numbers):

    for i in range(1, len(numbers)):

        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers
"""
SEARCHING
│
├── Linear Search
│   └── O(n)
│
└── Binary Search
    ├── sorted data
    ├── divide in half
    └── O(log n)


SORTING
│
├── Bubble
│   └── swap neighbors
│
├── Selection
│   └── select minimum
│
├── Insertion
│   └── insert into sorted portion
│
├── Merge
│   └── divide + merge
│
└── Quick
    └── pivot + partition 
   
Linear Search → O(n)

Binary Search → O(log n)
                 ↓
              sorted data

Bubble/Selection/Insertion
→ generally O(n²)

Merge Sort
→ O(n log n)

Quick Sort
→ average O(n log n)
→ worst O(n²)

Python sort()
→ highly optimized Timsort """
#twopointersalgorithm
def two_array_pointersum(numbers,target):
    left=0
    right=len(numbers)-1
    while(left<right):
        total=numbers[left]+numbers[right]
        if total==target:
            return left,right
        elif total<target:
            left+=1
        else:
            right-=1
    return -1 -1
def palindorome_twopointer(s):
    left=0
    right=len(s)-1
    while(left<right):
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
#sliding window
def max_sum(numbers, k):

    window_sum = sum(numbers[:k])
    best = window_sum

    for right in range(k, len(numbers)):

        window_sum += numbers[right]
        window_sum -= numbers[right - k]

        best = max(best, window_sum)

    return best