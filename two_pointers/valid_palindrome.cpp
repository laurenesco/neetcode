// Memory: 104.3 MB•Time: 1ms•Submitted at: 04/24/2026 15:07
// Beats 100 in runtime, 100% in memory

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

        while (start < end) {

            // Ignore special characters
            while (!isalnum(*start) && start < end) {
                start ++;
            }

            if (start == end) {
                return true;
            }

            // Ignore special characters
            while (!isalnum(*end) && end > start) {
                end --;
            }

            // Run the comparison
            if (tolower(*start) != tolower(*end))  {
                return false;
            }

            // Move the pointers
            start ++;
            end --;

        }

        return true;


    }
};
