class Solution(object):
    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, left, right):
        if left >= right:
            return

        mid = (left + right) // 2

        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)

        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= right:
            temp.append(nums[j])
            j += 1

        for k in range(len(temp)):
            nums[left + k] = temp[k]