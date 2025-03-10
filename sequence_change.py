def find_sequence_change(arr):

    # 判斷陣列的長度是否小於3
    if len(arr) < 3:
        return -1
    
    # 判斷陣列的
    for i in range(len(arr)-2):

        # 檢查從遞增轉為遞減
        if arr[i] < arr[i + 1] and arr[i + 1] > arr[i + 2]:
            return i + 1
        
        # 檢查從遞減轉為遞增
        if arr[i] > arr[i + 1] and arr[i + 1] < arr[i + 2]:
            return i + 1
    
    return -1
