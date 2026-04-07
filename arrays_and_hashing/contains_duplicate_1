#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Approach 1
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
