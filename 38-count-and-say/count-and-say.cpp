class Solution {
public:
    string countAndSay(int n) {
        if(n == 1) return "1";

        string s = "1";
        string res;

        for(int i = 1; i < n; i++){
            res = "";
            int cnt = 1;

            for(int j = 1; j < s.size(); j++){
                if(s[j] != s[j - 1]){
                    res += (to_string(cnt) + s[j - 1]);
                    cnt = 1;
                }
                else {
                    cnt++;
                }
            }

            // Add the last group
            res += (to_string(cnt) + s[s.size() - 1]);

            s = res;
        }

        return s;
    }
};