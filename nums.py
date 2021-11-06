def find_missing_nums(nums):
    nums1 = list(range(1,len(nums)))
    return list(set(nums1) - set(nums))

while True:
    print("Вход (введите значения списка через пробел): ")
    nums = [int(i) for i in input('nums = ').split()]
    print("Вывод: ", find_missing_nums(nums))
