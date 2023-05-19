class RangeFreqQuery {
    
private:
    vector<map<int,int>>seg;
    int n;
public:  
    
    void insert(vector<int> & nums,int idx, int low, int high){
        if(low==high){
            seg[idx][nums[low]]+=1;
            return;
        } 
        int mid=(low+high)/2; 
        insert(nums,2*idx+1,low,mid);
        insert(nums,2*idx+2, mid+1,high);
        for(auto it = seg[2*idx+1].begin() ; it!=seg[2*idx+1].end() ; it++)
        {
            int ele = it->first;
            int freq = it->second;
            seg[idx][ele]+=freq;
        }
        
        for(auto it = seg[2*idx+2].begin() ; it!=seg[2*idx+2].end() ; it++)
        {
            int ele = it->first;
            int freq = it->second;
            seg[idx][ele]+=freq;
        }
    }
    
    int Freqrange(int idx,int low, int high, int l, int r,int val)
    {
        if(l>high || r<low)
            return 0; 
        if(low>=l && high<=r) 
        {   
            return seg[idx][val];  
        }
        int mid=(low+high)/2;
        int left=Freqrange(2*idx+1,low,mid,l,r,val);
        int right=Freqrange(2*idx+2,mid+1,high,l,r,val); 
        return left+right;
    } 

    RangeFreqQuery(vector<int>& nums) {
        n=nums.size();
        seg.resize(4*n);
        insert(nums,0,0,n-1);
    }
    
    int query(int left, int right, int value) {
        return Freqrange(0,0,n-1,left,right,value);
    }
};

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery* obj = new RangeFreqQuery(arr);
 * int param_1 = obj->query(left,right,value);
 */