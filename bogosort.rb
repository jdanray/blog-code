def shuffle(arr)
    if arr.length > 1
        i = arr.length - 1
        while i > 0
            r = rand(i)
            arr[i], arr[r] = arr[r], arr[i]
            i -= 1
        end
    end
    return arr
end

def bogosort(arr, order)
    while arr != order
        arr = shuffle(arr)
    end
    return arr
end
