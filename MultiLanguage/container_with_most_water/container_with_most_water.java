
class Solution {
    public int maxArea( int[] height) {
        int water =0; 
        int l = 0;
        int r = height.length - 1;
        while ( r > l ){
            water = Math.max(water, (r-l)*Math.min(height[l],height[r]));
            if (height[r] < height[l]){
                r-- ;
            } else {
                l++ ;
            }
        };
        return water;
    }
}