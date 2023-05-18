class NumArray {
private:
    vector<int> seg;
    int n;
public:  
    
    void insert(vector<int> & nums,int idx, int low, int high){
        if(low==high){
            seg[idx]=nums[low];
            return;
        } 
        int mid=(low+high)/2; 
        insert(nums,2*idx+1,low,mid);
        insert(nums,2*idx+2, mid+1,high);
        seg[idx]=seg[2*idx+1] + seg[2*idx+2]; 
    }
    
    int sumrange(int idx,int low, int high, int l, int r)
    {
        if(l>high || r<low)
            return 0; 
        if(low>=l && high<=r) 
            return seg[idx];  
        int mid=(low+high)/2;
        int left=sumrange(2*idx+1,low,mid,l,r);
        int right=sumrange(2*idx+2,mid+1,high,l,r); 
        return left+right;
    } 
    
    void update(int idx,int i,int val,int low, int high)
    { 
        
        if(low==high) 
        {
            seg[idx]=val;
            return ;
        }
        int mid=(low+high)/2; 
        if (i<=mid)
            update(2*idx+1,i,val,low,mid);
        else
            update(2*idx+2,i,val,mid+1,high);
        
        seg[idx]=seg[2*idx+1]+seg[2*idx+2];
        
    } 
    
    NumArray(vector<int>& nums) { 
        n=nums.size();
        seg.resize(4*n);
        insert(nums,0,0,n-1);
        
    }
    
    void update(int index, int val){
        update(0,index,val, 0,n-1);
        
    }
    
    int sumRange(int left, int right) {
        return sumrange(0,0,n-1,left,right);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */