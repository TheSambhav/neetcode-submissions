class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>mp;
        for(int i = 0; i < nums.size();i++){
            mp[nums[i]]++;
        }
        vector<int>res;
        for(const auto pair : mp){
            if(pair.second >= k){
                res.push_back(pair.first);
            }
        }
        return res;
    }
};
