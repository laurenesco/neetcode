// Memory: 146 MB•Time: 5ms•Submitted at: 04/09/2026 13:20
// Beats 21.82% in runtime, 68.05% in memory

#include <algorithm>

class Solution {
public:
    bool isAnagram(string s, string t) {
        // Approach: Sort the provided strings, compare the 
        // sorted versions, if matching return true

        // Sort both strings
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        // Return matching bool
        return s == t;
    }
};
