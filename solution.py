from typing import List
import heapq

class Solution:
    def sherlockSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        runs = []
        n = len(nums)
        i = 0

        while i < n:
            j = i
            while j + 1 < n and nums[j] <= nums[j + 1]:
                j += 1
            runs.append(nums[i:j + 1])
            i = j + 1

        if len(runs) == 1:
            return nums

        for k in range(len(runs)):
            segment = runs[k]
            size = len(segment)
            val_range = max(segment) - min(segment) if segment else 0

            if size > 64 and val_range < size:
                mn = min(segment)
                mx = max(segment)
                count = [0] * (mx - mn + 1)
                for x in segment:
                    count[x - mn] += 1
                sorted_seg = []
                for idx, c in enumerate(count):
                    if c:
                        sorted_seg.extend([idx + mn] * c)
                runs[k] = sorted_seg
            else:
                segment.sort()

        heap = []
        for i in range(len(runs)):
            if runs[i]:
                heap.append((runs[i][0], i, 0))
        heapq.heapify(heap)

        result = []
        while heap:
            val, i, j = heapq.heappop(heap)
            result.append(val)
            if j + 1 < len(runs[i]):
                heapq.heappush(heap, (runs[i][j + 1], i, j + 1))

        return result
