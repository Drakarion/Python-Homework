def merge_lists(list1, list2):
    return list1 + list2

input1 = input("Enter the first list: ")
input2 = input("Enter the second list: ")

list1 = [int(x) for x in input1.strip().split()]
list2 = [int(x) for x in input2.strip().split()]

result = merge_lists(list1, list2)
print("Merged list:", result)
