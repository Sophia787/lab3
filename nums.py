def find_missing_nums(nums):
    list1 = nums   
    n = 0
    for i in list1:
        n += 1
        
    list2 = [list2 for list2 in range(1, n+1)]

    k = 0
    list3 = []
    while k < n:
        if list2[k] not in list1:
            list3.append(list2[k])
            k+=1
        else:
            k+=1
            
    return list3
