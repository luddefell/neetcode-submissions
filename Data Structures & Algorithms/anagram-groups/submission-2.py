class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i, word in enumerate(strs):
            anagram = [0] *26
            for char in word:
                anagram[ord(char) - ord('a')] += 1
            anagram=tuple(anagram)
            hashmap[anagram].append(word)
        return list(hashmap.values())
                
