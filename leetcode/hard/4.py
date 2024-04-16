def merge(merge_arr, n1, n2):
    if len(n1) == 0 or len(n2) == 0:
        merge_arr += n2
        merge_arr += n1
        return
    if n1[0] > n2[0]:
        merge_arr.append(n2[0])
        merge(merge_arr, n1, n2[1:])
    else:
        merge_arr.append(n1[0])
        merge(merge_arr, n1[1:], n2)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) ->float:
        merge_arr = []
        total = len(nums1) + len(nums2)
        index = total // 2
        merge(merge_arr, nums1, nums2)
        if total % 2 == 0:
            return (merge_arr[index] + merge_arr[index-1]) / 2
        else:
            return merge_arr[index]