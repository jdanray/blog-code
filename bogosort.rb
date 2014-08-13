def shuffle(arr)
    if arr.length > 1
        i = arr.length - 1
        while i > 0
            r = rand(i)
            arr[i], arr[r] = arr[r], arr[i]
            i -= 1
        end
    end
    arr
end

def bogosort(arr)
    arr = shuffle(arr) until arr == arr.sort
    arr
end
