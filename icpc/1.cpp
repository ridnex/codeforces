#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<vector<string> >arr(3);
        map<string, int> mp;
        for(int i=0; i<3; i++){
            for(int j=0; j<n; j++){
                string k;
                cin >> k;
                if(mp[k]){
                    mp[k]+=1;
                }
                else{
                    mp[k]=1;
                }
                arr[i].push_back(k);
            }
        }
        for(int i=0; i<3; i++){
            int cnt = 0;
            for(int j=0; j<n; j++){
                if(mp[arr[i][j]]==2){
                    cnt++;
                }
                else if(mp[arr[i][j]]==1){
                    cnt+=3;
                }
            }
            cout << cnt << " ";
        }
        cout<<endl;


        
    }
   
}