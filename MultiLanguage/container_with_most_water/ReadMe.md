## [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

### Instructions 
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

### Example 1
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

### Example 2

Input: height = [1,1]
Output: 1
 
## Solution Explanation

Two Indexes  show up in two-pointer problems, and also sliding windows. On first glance, a sliding window could make sense. After all, an area between two ends constitutes a window. However, a key element of this problem is the distance between two points in the array. Two points of height 3 which are adjacent have an container area of 3, while points of height 1 which are 4 spaces away, have a container area of 4. Therefore, the best solution will attempt to most efficiently evaluate the length between two points. The easiest way to do this is to start from both ends and work inward. Intuitively, this feels efficient since we will start by evaluating the longest window first. 

This makes the solution a Two Pointer, not Sliding Window. When moving inward we need an evaluation criteria on which to pointer to move toward the other. Since we are shortening the length of the pointer, we need to allow the possibility of the largest area. This means moving the index of the shorter height. This allows the max array to be found in any scenario, since the container’s area is always constrained by the shorter height. 
