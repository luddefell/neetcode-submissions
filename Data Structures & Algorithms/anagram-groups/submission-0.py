class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hist_list = []
        final_return = []
        for i,word in enumerate(strs):
            current_anagram = {}
            for char in word:
                if char not in current_anagram:
                    current_anagram[char] = 1
                else:
                    current_anagram[char] = current_anagram[char] + 1
            if current_anagram not in anagram_hist_list:
                anagram_hist_list.append(current_anagram)
                final_return.append([word])
            else:
                for j,anagram_j in enumerate(anagram_hist_list):
                    if (current_anagram == anagram_j):
                        final_return[j].append(strs[i])
        return final_return



