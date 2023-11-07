nums = [88,46,25,11,18,12,22]


def Quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        left_list = []
        middle_list = []
        right_list = []

        pivot = nums[-1]
        x = 0
        for x in nums:
            if pivot > x:
                left_list.append(x)
            elif pivot < x:
                right_list.append(x)
            else:
                middle_list.append(x)
        return Quicksort(left_list)+middle_list+Quicksort(right_list)
print(Quicksort(nums))
        
        
    
    