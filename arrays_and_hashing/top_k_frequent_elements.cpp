// Memory: 113.1 MB•Time: 2ms•Submitted at: 04/13/2026 14:53
// Beats 98.73% in runtime and 95.54% in memory

// #include <iostream>
// #include <algorithm>
// #include <map>
// #include <vector>

// using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        // Transfer vector to map with occurrence count
        map<int, int> occ_map;

        for (int i = 0; i < nums.size(); i ++) {
            occ_map[nums[i]] = (occ_map.contains(nums[i])) ? occ_map[nums[i]] + 1 : 1;
        }

        // Transfer the map to a vector of pairs
        vector<pair<int, int>> pair_vector(occ_map.begin(), occ_map.end());

        // Sort the vector of pairs by value
        sort(pair_vector.begin(), pair_vector.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second > b.second;
        });

        // Put together result vector
        vector<int> results;
        for (int i = 0; i < k; i++) {
            results.push_back(pair_vector[i].first);
        }

        return results;

    }
};
