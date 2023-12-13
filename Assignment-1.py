def stack(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        if our_list:
            our_list.pop()
    return our_list


def queue(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        if our_list:
            our_list.pop(0)
    return our_list

print("Testing Stack Function : \n")
new_list = [1,2,3,4]
print(f"Original list : {new_list}")
stack(new_list,"add",0)
print(f"After Adding Element 0 : {new_list}")
stack(new_list,"remove")
print(f"After remove fucntion : {new_list}\n")

print("Testing Queue Function: \n")
new_list = [1,2,3,4]
print(f"Original Queue : {new_list}")
queue(new_list,"add",0)
print(f"After adding element 0 : {new_list}")
queue(new_list,"remove")
print(f"After remove fucntion : {new_list}")