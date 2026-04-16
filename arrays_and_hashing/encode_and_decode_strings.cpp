// Memory: 133.5 MB•Time: 43ms•Submitted at: 04/16/2026 14:36
// Beats 99.4% in runtime, 100% in memory

class Solution {
public:

    string encode(vector<string>& strs) {

        // Resultant string initialization
        string result;

        // For each entry in strs
        for (const auto& word : strs) {
            // Add a delimiter
            result += word;
            result += '`';
        }

        return result;

    }

    vector<string> decode(string s) {

        // Resultant vector
        vector<string> result;
        string word;

        // For each letter in encoded string
        for (const auto& c : s) {

            // Split on delimiter
            if (c != '`') {
                word += c;
            } else {
                result.push_back(word);
                word.clear();
            }
        } 

        return result;
    }
};
