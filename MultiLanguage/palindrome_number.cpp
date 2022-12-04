// 
class Solution {
public:
    bool isPalindrome(int x) {
        string x_str = to_string(x);
        string y = "";

        int n = x_str.length();
        for (int i =0; i < n; i++)
            y+= x_str[n-i-1];

        return x_str == y;

    }
};


//

class Solution {
public:
    bool isPalindrome(int x) {
        string x_str = to_string(x);

        int n = x_str.length();
        for (int i =0; i < n/2; i++)
            if(x_str[i] != x_str[n-i-1]){
                return false;
            };


        return true;

    }
};
