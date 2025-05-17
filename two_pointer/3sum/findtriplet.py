from typing import List

def three_sum(lst: List):
    lst.sort()
    result = []

    for pivot in range(len(lst)-2): 
        if lst[pivot] > 0:
            break            
        if pivot > 0 and lst[pivot] == lst[pivot-1]:
            continue                                     
        low, high = pivot + 1, len(lst)-1
        while low < high:
            total = lst[pivot] + lst[low] + lst[high]
            if total < 0:
                low += 1
            elif total > 0:
                high -= 1
            else:
                triplet = [lst[pivot], lst[low], lst[high]]
                result.append(triplet)
                low += 1
                high -= 1
                while low < high and lst[low] == lst[low-1]:
                    low += 1
                while low < high and lst[high] == lst[high+1]:
                    high -= 1
    return result

def main():
    nums = [2, 4, 5]
    print(three_sum(nums))
if __name__ == "__main__":
    main()
