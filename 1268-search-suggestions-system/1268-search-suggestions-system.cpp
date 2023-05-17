struct node 
{
    node *children[26];
    string Word="";
    int countend=0;
    
};

class Solution {
private:
    node* root;
public:
     Solution(){
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
        temp->Word=word;
    
    } 
     
    void findAllString(node* temp, vector<string>& res){
        if (temp==NULL)
            return ;
        if (res.size()==3)
            return ; 
        if(temp->Word!="")
            res.push_back(temp->Word);
        for(int i=0;i<26;i++){
            string s1="";
            if (temp->children[i]) 
            {
                findAllString(temp->children[i],res);
             }  
                
        }
        
        
    }
    vector<string> findword(string &word){
        node *temp=root;
        int n= word.size();
        vector<string> res;
        for (int i = 0; i < n; i++) {
            int idx = int(word[i]) - 97; 
            if (!temp->children[idx])
                return res;
            temp = temp->children[idx] ;
        } 
        
        findAllString(temp,res);
        return res;
    }
    
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(),products.end()); 
        int n=searchWord.size();  
        vector<vector<string>> ans;
        for(auto i:products)
            insert(i); 
        string s="";
        for(int i=0;i<n;i++){
            s+=searchWord[i];
            vector<string> res; 
            ans.push_back(findword(s));
            
        }
        return ans;
        
        
    }
};