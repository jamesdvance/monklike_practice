// This gets a wrong answer

class Solution {
    String str; 
    String ptn;
    String star_ptn = "*";
    String pt_ptn = ".";
    public boolean isMatch(String s, String p) {
        str = s; 
        ptn = p; 

        return dfs(0,0);
    }

    private boolean dfs(int i, int j) {
        if( (i >= str.length()) && (j >= ptn.length()) ){
            return true; 
        };

        if (j >= ptn.length()) {
            return true ;
        };

        boolean match = (
            (i < str.length()) 
            && ((str.substring(i)==ptn.substring(j)) || (ptn.substring(j)==pt_ptn)));

        if ( ( j + 1) < ptn.length() && ptn.substring(j+1) == star_ptn ) {
            return dfs(i,j+2) || (match && dfs(i+1,j));
        };

        if( match ){
            return dfs(i + 1, j + 1);
        };

        return false;
    }
}
