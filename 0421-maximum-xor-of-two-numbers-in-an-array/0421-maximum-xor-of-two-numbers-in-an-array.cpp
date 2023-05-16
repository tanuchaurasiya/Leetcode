struct trienode
{
  trienode *arr[2];  
};
class Solution {
public:
    void insert(int num,trienode* root){
        trienode *temp=root;
        for(int i=31;i>=0;i--){
            int bit = (num>>i) & 1;
            if( ! temp->arr[bit])
                temp->arr[bit] = new trienode(); 
            temp=temp->arr[bit]; 
        }
    } 
    
    int findmax(int num, trienode* root){ 
        trienode *temp=root;
        int res=0;
        for(int i=31;i>=0;i--){
            int bit = num>>i & 1; 
            if(bit==0){
                if(temp->arr[1]){
                    res+=pow(2,i);
                    temp=temp->arr[1];
                } 
                else{
                    temp=temp->arr[0];
                }
            }
            if(bit==1){
                if(temp->arr[0]){
                    res+=pow(2,i);
                    temp=temp->arr[0];
                } 
                else{
                    temp=temp->arr[1];
                }
            } 
        }
        return res;
        
    }
    
    int findMaximumXOR(vector<int>& nums) {
        trienode *root=new trienode(); 
        for(auto i:nums) 
            insert(i,root); 
        int maxx=0; 
        for(auto i:nums) 
            maxx=max(maxx,findmax(i,root));
        return maxx;
    }
};