class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_dict = {}
        print("Current Dict is:", current_dict)
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    counter += 1
                    current_dict.update({nums[j]: counter})
        keys_list = list(current_dict.keys())
        value_list = list(current_dict.values())
        print(keys_list)
        return keys_list


if __name__ == "__main__":
    s = Solution()
    k = s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])