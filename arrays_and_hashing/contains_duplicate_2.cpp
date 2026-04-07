#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Approach 2
        // Sort the vector, iterate through and if i-1 = 1, return false
        // No data storage required

        bool result = false;

        sort(nums.begin(), nums.end());

        for (int i = 1; i < nums.size(); i++) {
            
            if (nums[i-1] == nums[i]) {
                result = true;
                break;
            }
        }

        return result;
    }
};
