class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        The idea is to use two hashmaps. One hashmap will be used to maintain the frequency of the elements from the nums
        array and the other hashmap will be the reverse of the 1st hashmap and this 2nd hashmap will have values as a list
        because frequencies of different elements could be same and while reversing the 1st hashmap, multiple items with
        same values would come under one key in the reversed hashmap. Also, mathematically k would never be too large and
        after creating the reversed hashmap our job is keep on decrementing the max_count until ans array length is equal to k.
        """
        max_count = 0  # frequency of the element that appeared max in the nums array
        freq_dict = {}  # 1st hashmap to store the frequencies of the elements from nums array
        rev_dict = {}  # 2nd hashmap i.e. reverse of the 1st hashmap but values as a list
        ans = []

        for num in nums:
            if freq_dict.get(num) is None:
                freq_dict[num] = 1
                temp_count = 1
            else:
                freq_dict[num] += 1
                temp_count = freq_dict[num]
            if temp_count > max_count:  # maintain max_count
                max_count = temp_count

        if len(freq_dict) == k:  # if len(freq_dict) == k just simply return 1st hashmap keys
            return freq_dict.keys()

        # Now, we need to reverse the 1st hashmap because we will find the most frequent k elements by decrementing the
        # max_count and that should be O(1) operation. While reversing, key will become value and value will become key
        # but value this time has to be a list because multiple elements could have same frequency in the 1st hashmap.
        for key, val in freq_dict.items():
            if rev_dict.get(val) is None:
                rev_dict[val] = [key]  # maintain values as a key
            else:
                rev_dict[val].append(key)  # append elements under the same key if their frequencies are same

        # Now, we need to just iterate until len of ans array is equal to k
        while True:
            # We will start from max_count and keep on decrementing it by 1 because this way we will be getting our most
            # frequent top k elements. Also, order does not matter here.
            data = rev_dict.get(max_count)
            if data:  # if data is not None then just extend the data list to ans array
                ans.extend(data)
            if len(ans) == k:  # if len(ans) == k, we have our top k elements, therefore, just break
                break
            max_count -= 1  # keep on decrementing k by 1

        return ans
