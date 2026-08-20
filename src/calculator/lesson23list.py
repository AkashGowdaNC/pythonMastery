num=[]
numbers=[10,20,30,40]
nums=list()
nums1=list(range(5))
print(nums1)
print(nums1[0])
nums1[1]=99
print(nums1)
numbers.insert(1, 99)
numbers.extend([3, 4])
numbers.append([3, 4])
print(len(numbers))
x = numbers.pop(1)
numbers.remove(30)
numbers.clear()
names = ["Zara", "Akash", "Rahul"]

names.sort()

print(names)
new_numbers = sorted(numbers)
num=(10,20,30)
n1=(10)
n2=(10,)
print(type(n1))
print(type(n2))
student=('Akash',22,'AIML')
name,age,branch=student
print(name)
print(age)
print(branch)