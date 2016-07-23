from random import shuffle

def test_quicksort(ntests, N):
    for _ in range(ntests):
        lst = list(range(N))
        shuffle(lst)
        print('%s -> %s' % (lst, quicksort(lst)))

def quicksort(lst):
    if not lst:
        return []

    pivot = lst[0]
    lt = [elem for elem in lst if elem < pivot]
    eq = [elem for elem in lst if elem == pivot]
    gt = [elem for elem in lst if elem > pivot]
    return quicksort(lt) + eq + quicksort(gt)

ntests = 5
N = 10
test_quicksort(ntests, N)
