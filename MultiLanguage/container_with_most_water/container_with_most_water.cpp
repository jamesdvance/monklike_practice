#include <vector>

class Solution {
    public: 
        int maxArea(vector<int>& height) {
            int l = 0; 
            int r = height.size()-1; 
            int max_ar = 0; 
            while (l < r) {
                int min_height = min(height[r], height[l]);
                max_ar = max(max_ar, (r-l) * max(0,min_height));
                if( height[l] < height[r] ) {
                    l++;
                } else {
                    r--;
                }
            }
            return max_ar;
        }
};