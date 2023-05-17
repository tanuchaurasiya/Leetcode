class Solution {
public:
    bool wordPattern(string pattern, string s) { 
        vector<string> m(26,"");
        vector<string >v;
        stringstream ss(s);
        string str;
        while (getline(ss, str, ' ')) 
            v.push_back(str);
        int n=pattern.size(); 
        set<string> se;
        if(pattern.length()!=v.size()) return false;
        for(int i=0;i<n;i++) 
        {
            if (m[int(pattern[i])-97]!="") 
            {
                // cout<<m[int(pattern[i])-97]<< " "<<v[i]<<endl;
                if (m[int(pattern[i])-97]!=v[i])  
                    return false;
            }
            else 
            {
                if(se.find(v[i])!=se.end())
                    return false;
                se.insert(v[i]);
                m[pattern[i]-97]=v[i];
            }
            
        }
        return true;
    }
};