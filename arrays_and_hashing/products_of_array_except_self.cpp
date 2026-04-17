// Memory: 105.9 MB•Time: 2ms•Submitted at: 04/17/2026 12:14
// Beats 98.37% in runtime, 99.90% in memory

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int total_sum = 1;
        int has_zeroes = 0;

        // Get overall product
        for (const auto& num : nums) {
            total_sum *= num;
            
            if (num == 0) { has_zeroes++ ; }

            // Multiple zeroes, quick return
            if (has_zeroes > 1) {
                vector<int> resultant(nums.size(), 0);
                return resultant;
            }
        }

        vector<int> resultant;

        // Calculate each index in resultant
        for (int i = 0; i < nums.size(); i++) {
        
            if (has_zeroes && nums[i] != 0) {
                // Array with a 0, this index not 0
                resultant.push_back(0);
            } else if (has_zeroes == 1 && nums[i] == 0) {
                // Array with a 0, this index is the 0, must recalculate

                int result = 1;
                for (int i = 0; i < nums.size(); i ++) {
                    if (nums[i] != 0) {
                        result *= nums[i];
                    }
                }

                resultant.push_back(result);
            } else {
                // Normal case: At each index, divide out nums[i]
                resultant.push_back(total_sum / nums[i]);
            }
        }

        return resultant;
    }
};
