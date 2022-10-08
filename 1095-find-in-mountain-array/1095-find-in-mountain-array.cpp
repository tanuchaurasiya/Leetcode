class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int s=0,e=mountainArr.length()-1;
        int ans=-1;
        while(s<e){
            int mid=s+(e-s)/2;
            if(mountainArr.get(mid)>mountainArr.get(mid+1)) {ans=mid;e=mid;}
            else if(mountainArr.get(mid)<mountainArr.get(mid+1)) {ans=mid+1;s=mid+1;}
        }
        int peak=mountainArr.get(ans);
        cout<<ans<<" "<<peak<<endl;
        if(peak==target) {return ans;}
        if(1) {
            int start=0,end=ans-1;
            while(start<=end){
                int mid=(start+end)/2;
                if(target==mountainArr.get(mid)) return mid;
                else if(target>mountainArr.get(mid)) start=mid+1;
                else if(target<mountainArr.get(mid)) end=mid-1;
            }
        }
        if(1){ 
            
             int start=ans+1,end=mountainArr.length()-1; 
            // cout<<start<<end;
            while(start<=end){
                int mid=(start+end)/2; 
                // cout<<mid<<endl; 
                if (mountainArr.get(end)==target) 
                return end;
                else if(target==mountainArr.get(mid)) return mid;
                else if(target>mountainArr.get(mid)) start=mid+1;
                else if(target<mountainArr.get(mid)) end=mid-1; 
                
            } 
            
        }
        return -1;
    }
};