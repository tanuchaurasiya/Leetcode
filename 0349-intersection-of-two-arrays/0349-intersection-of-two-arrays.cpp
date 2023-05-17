class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int>s;
        for(auto i:nums1)
            s.insert(i);
        vector<int> res;
        for(auto i:s)
            if(find(nums2.begin(),nums2.end(),i)!=nums2.end())
                res.push_back(i);
        return res;
    }
};