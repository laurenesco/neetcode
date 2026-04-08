# Memory: 8.7 MB•Time: 57ms•Submitted at: 04/08/2026 14:18
# Beats 100% in runtime, 20.87% in memory

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create hash map where
        # key: anagram with letters sorted
        # value: the index in the result vector

        anagram_indices = {}
        anagrams = []
        i = 0;

        # for each string in strs
        for j in range(len(strs)):

            # sort the string into temp var
            og_word = strs[j]
            sorted_word = "".join(sorted(str(og_word)))

            # search map for existing entry 
            if sorted_word not in anagram_indices:

                # if doesnt exist, create entry with temp var and set value to i
                anagram_indices[sorted_word] = i

                # create new entry in dict for the word
                anagrams.append([og_word])

                # increment i
                i += 1
            else:
                # otherwise append to appropriate list in dict
                anagrams[anagram_indices[sorted_word]].append(og_word)

        return anagrams
