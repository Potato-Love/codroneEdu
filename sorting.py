with open("unsorted integer.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x > pivot]      # pivot보다 큰 값 (내림차순)
    right = [x for x in arr[1:] if x <= pivot]    # pivot보다 작거나 같은 값
    return quick_sort(left) + [pivot] + quick_sort(right)

sorted = quick_sort(lines)
with open("SB-a04-1-sorted_out.txt", "w", encoding="utf-8") as f:
    for num in sorted:
        f.write(f"{num}")