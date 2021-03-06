def inorder(arr)
    arr == arr.sort
end

def shuffle(arr)
    i = arr.length - 1
    while i > 0
        r = rand(i)
        arr[i], arr[r] = arr[r], arr[i]
        i -= 1
    end
    arr
end

def bogosort(arr)
    arr = shuffle(arr) until inorder(arr)
    arr
end
