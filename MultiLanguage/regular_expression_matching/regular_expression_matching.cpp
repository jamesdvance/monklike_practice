// This does not compile

class Solution {
    public:
        char* dot_ptn = ".";
        char* star_ptn = "*";
        string str; 
        string ptn;
        int s_size;
        int p_size;
        bool isMatch(string s, string p) {
            str = s; 
            ptn = p;
            s_size = str.size();
            p_size= ptn.size();
            return dfs(0,0);

        }

    private: bool dfs(int i, int j){
        if (i >= s_size && j >= p_size){
            return true;
        };

        if ( j >= p_size ) {
            return false ;
        };

        char subptn = ptn[j];
        char substr = str[i];

        bool match = (i < s_size) && ((substr == subptn) or (subptn == dot_ptn));


        if ((j + 1) < p_size) {
            char* next_ptn = ptn[j+1];
            if (next_ptn == star_ptn){
                return (
                    ( dfs(i, j+2 ) ) || (match && dfs(i+1, j))
                );
            };
        };


        if (match) {
            return dfs(i+1,j+1);
        };

        return false;
    }
}