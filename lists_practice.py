#1. Write a Python program to multiply all the items in a list.

nums = [1,2,3,4]

total = 1
if len(nums) > 0:
	for i in nums:
		total = total * i
print(total)

#2. Write a Python program to remove duplicates from a list

nums = [1,1,2,3,2,3]
original = []
for i in nums:
	if i not in original:
		original.append(i)
print(original)

#3. Write a Python program to find the list of words that are longer than n from a given list of words.

words = ["A warrior", "does", "not give up", "what", "he", "loves", "he finds the love", "in", "what", "he does"]
n = 4
new_list = []
for i in words:
	if len(i)>n:
		new_list.append(i)
print(new_list)

#4. Write a Python function that takes two lists and returns True if they have at least one common member.

l1 = [1,2,3,4,5]
l2 = [6,7,8,10,9]

output = False
for i in l1:
	if i in l2:
		output = True
print(output)


#5. Write a Python program to print the numbers of a specified list after removing even numbers from it.

nums = [1,2,3,4,5,6,7,8]
odd_list = []
for i in nums:
	if i%2 != 0:
		odd_list.append(i)

print(odd_list)
