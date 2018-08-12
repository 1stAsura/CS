def binary_search(li, target):
    """
    인자의 리스트는 정렬된 리스트
    """
    start=0
    end=len(li)-1

    while start <= end:
        middle=(start+end)//2
        if li[middle]==target:
            return middle
        elif li[middle] > target:
            end=middle-1
        else:
            start=middle+1

    return None

if __name__=="__main__":
    data=[i**2 for i in range(1, 10)]

    target=9
    idx=binary_search(data, target)

    if idx:
        print('index : {}, data : {}'.format(idx, data[idx]))
    else:
        print('Failed to find the data of {}'.format(target))