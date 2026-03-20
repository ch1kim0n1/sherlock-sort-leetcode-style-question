import heapq

def sherlock_sort(arr):
    if len(arr) <= 1:
        return arr

    runs = []
    n = len(arr)
    start = 0
    while start < n:
        end = start
        while end + 1 < n and arr[end] <= arr[end + 1]:
            end += 1
        runs.append((start, end))
        start = end + 1

    if len(runs) == 1:
        return arr

    sorted_segments = []
    for start, end in runs:
        segment = arr[start:end + 1]
        size = len(segment)
        val_range = max(segment) - min(segment) if segment else 0

        if size > 64 and val_range < size:
            count = {}
            for x in segment:
                count[x] = count.get(x, 0) + 1
            sorted_seg = []
            for x in sorted(count.keys()):
                sorted_seg.extend([x] * count[x])
            sorted_segments.append(sorted_seg)
        else:
            segment.sort()
            sorted_segments.append(segment)

    return list(heapq.merge(*sorted_segments))
