// Memory: 291.3 MB•Time: 4ms•Submitted at: 04/07/2026 10:22
// Beats 100% in speed, 4.26% in memory

#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Create hash map for each anagram group as the key
        // and the index in the result vector as the value

        vector<vector<string>> result;
        map<string, int> indices;
        int i = 1;

        // for each string in strs
        for (string word : strs) {

            // sort the string into temp var
            string sorted = word;
            sort(sorted.begin(), sorted.end());

            // search map for existing entry 
            if (indices.count(sorted) == 0) {

                // if doesnt exist, create entry with temp var and set value to results.size since that is indice of next entry
                indices.insert({sorted, result.size()});

                // add word to result vector at indice
                result.push_back({word});

            } else {
                // otherwise insert at the existing index for the anagram
                int index = indices[sorted];
                result[index].push_back(word);
            }
        
        }

        return result;
    }
};
