// Memory: 150.8 MB•Time: 2ms•Submitted at: 04/08/2026 13:46
// Beats 93.17% in runtime, 5.77% in memory

#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Use map to track occurences of values in array
        // Return true if any value of map increments to 2

        map<int, int> numbers;
        bool result = false;

        for (int num : nums) {
            if (numbers.contains(num)) {
                result = true;
                break;
            } else {
                numbers[num] = 1;
            }
        }

        return result;
    }
};
