class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diff;
        for (int i = 0; i < nums.size(); ++i) {
            int difference = target - nums[i];
            diff[difference] = i;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (diff.find(nums[i]) != diff.end()) {
                if (i == diff[nums[i]]) {
                    continue;
                } else if (i < diff[nums[i]]) {
                    return {i, diff[nums[i]]};
                } else {
                    return {diff[nums[i]], i};
                }
            }
        }
    }
};
