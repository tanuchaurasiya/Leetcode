struct node 
{
    node *children[26];
    int countend=0;
    
}; 
class Solution { 
private:
    node* root;
public:
    Solution()
    {
        root = new node();
    } 
    
    void insert(string &word){
        node *temp=root;
        int n= word.size();
        for(int i=0;i<n;i++){
            int idx=int(word[i])-97;
            if (!temp->children[idx])
                temp->children[idx]=new node();
            temp=temp->children[idx] ;
           
        }
        
        temp->countend+=1;
        // cout<<word<<" "<<temp->countend<<endl;
    
    }

    int countWordsEqualTo(string &word){
        node *temp=root;
        int n= word.size();
        for (int i = 0; i < n; i++) {
            int idx = int(word[i]) - 97; 
            if (!temp->children[idx])
                return 0;
            temp = temp->children[idx] ;
        }
        return temp->countend;
        
        
    } 
    
 
    vector<string> topKFrequent(vector<string>& words, int k) { 
        set<string>s;
        for(auto i:words){
            insert(i); 
            s.insert(i); 
        }
        int n=words.size();
        vector<string> v;
        vector<vector<string>> m(n+1); 
        for(auto i:s){
            int x=countWordsEqualTo(i);
            m[x].push_back(i); 
            // cout<<x<<" "<<i<<endl;
        }
    
        int i=n;
        int c=0;
        while(c<k){ 
            // cout<<m[i].size()<<endl;
            int s=m[i].size();
            if(s==0){
                i-=1; 
                continue;
            } 
            if(s==1){
                v.push_back(m[i][0]);
                i-=1;
                c+=1;
            }
            else{
                sort(m[i].begin(),m[i].end()); 
                int x=0;
                while(x<s && c<k){
                    v.push_back(m[i][x]);
                    x+=1;
                    c+=1;
                }
                i-=1;
            }
        }
        return v;
    }
};