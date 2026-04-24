// Memory: 104.7 MB•Time: 2ms•Submitted at: 04/24/2026 14:49
// Beats 92.08 in runtime, 95.22% in memory

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        char* start = &s[0];
        char* end = &s[s.size()-1];

        // Single element/empty array case
        if (s.size() <= 1) {
            return true;
        }

        // Ignore special character at start 
        while (!isalnum(*start) && start < end) {
            start ++;
        }

        // Array is all special character case
        if (start == end) {
            return true;
        }

        // Ignore special characters at end
        while (!isalnum(*end)) {
            end --;
        }

        while (start < end) {

            // Run the comparison
            if (tolower(*start) != tolower(*end))  {
                return false;
            }

            // Move the pointers
            start ++;
            end --;

            // Ignore special characters
            while (!isalnum(*start)) {
                start ++;
            }

            while (!isalnum(*end)) {
                end --;
            }

        }

        return true;


    }
};
