// Memory: 105.9 MB•Time: 2ms•Submitted at: 04/15/2026 13:25
// Beats 99.27% in run time, 97.36% in memory

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> results;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j <= nums.size(); j ++) {
                if (nums[i] + nums[j] == target) {
                    results.push_back(i);
                    results.push_back(j);
                    return results; 
                }
            }
        }

        return results;

    }
};
