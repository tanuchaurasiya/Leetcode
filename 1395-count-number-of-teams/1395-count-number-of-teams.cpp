class Solution {
public:
    int dp1[1001][3][1002];
    int f(int i,int j,vector<int>&rating,int prev)
    {
        if(j==3) return 1;
        if(i==rating.size()) return 0;
        if(dp1[i][j][prev+1]!=-1) return dp1[i][j][prev+1];
        int ans=0;
        if(prev ==-1 || rating[i]>rating[prev])
        {
           ans+=f(i+1,j+1,rating,i);
        }
        ans+=f(i+1,j,rating,prev); 
        return dp1[i][j][prev+1]=ans;
    }
    int numTeams(vector<int>& rating) {
        memset(dp1,-1,sizeof(dp1));      
       int ans1= f(0,0,rating,-1);
       reverse(rating.begin(),rating.end());
         memset(dp1,-1,sizeof(dp1));
       int ans2= f(0,0,rating,-1);       
        return ans2+ans1;      
    }
};