class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int,int> m1;
        map<int,int>m2; 
        for(auto i:nums1){
            if(m1.find(i)==m1.end()) 
                m1[i]=1;
            else
                m1[i]+=1 ;
        } 
        
        for(auto i:nums2){
            if(m2.find(i)==m2.end()) 
                m2[i]=1;
            else
                m2[i]+=1 ;
        } 
        vector<int>res;
        for(auto i:m1)
            if(m2.find(i.first)!=m2.end())
                res.insert(res.end(), min(i.second,m2[i.first]), i.first);
                
        return res;
        
    }
};