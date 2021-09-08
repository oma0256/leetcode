class Solution:
    def twoSum(self, numbers, target):
        sum_index_list = []
        numbers_dict = {}
        for index, num in enumerate(numbers):
            reminder = target - num
            if reminder in numbers_dict:
                sum_index_list.append(numbers_dict[reminder] + 1)
                sum_index_list.append(index + 1)
                break
            numbers_dict[num] = index
        return sum_index_list


numbers = [-1, 0]
target = -1
print(Solution().twoSum(numbers, target))
