// Memory: 106.5 MB•Time: 2ms•Submitted at: 04/20/2026 11:35
// Beats 99.7% in runtime, 94.89% in memory

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int result = 0;
        int tmp_result = 0;

        // Empty vector case
        if (nums.size() == 0) {
            return 0;
        }

        // Sort the array
        sort(nums.begin(), nums.end());

        // Remove duplicates
        nums.erase(unique(nums.begin(), nums.end()), nums.end());

        // Count consecutive terms
        for(int i = 0; i < nums.size(); i++) {
            if (nums[i+1] == nums[i] + 1) {
                tmp_result ++;
                if (tmp_result > result) {
                    result = tmp_result;
                }
            } else {
                tmp_result = 0;
            }
        }

        return result + 1;
    }
};
