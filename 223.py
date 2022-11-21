# 223. Rectangle Area
"""
Medium

Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).



Example 1:

Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45
Example 2:

Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16


Constraints:

-104 <= ax1 <= ax2 <= 104
-104 <= ay1 <= ay2 <= 104
-104 <= bx1 <= bx2 <= 104
-104 <= by1 <= by2 <= 104
"""


# Solution
# Overview
# In this problem, we are given the coordinates of four points on a 2D plane. Two of them belong to the bottom left, and top right corners of rectangle AAA, and the other two belong to the bottom left and top right corners of rectangle BBB. The sides of the rectangles are parallel to the xxx and yyy axes. Using these points, we need to find the total area covered by two rectangles.
#
# Without an indicative diagram, we might think it'll simply be the addition of the individual areas of both rectangles. And that's the most common mistake people make with this question. The two rectangles could potentially overlap with each other. Considering this, let's see how to go about the problem's solution.
#
# Approach: Math and Geometry
# Intuition
# As explained in the overview section above, calculating the individual areas of both rectangles is easy enough. We have the coordinates of top right and bottom left corners - (x1,y1)(x1, y1)(x1,y1) and (x2,y2)(x2, y2)(x2,y2). In this case, the area of the rectangle would be height∗widthheight * widthheight∗width or in other words, (y2−y1)∗(x2−x1)(y2 - y1) * (x2 - x1)(y2−y1)∗(x2−x1). We can calculate the area of both rectangles and sum it together.
#
# But, the rectangles could potentially have an overlap between them. This means we might be counting the overlapping area twice, which should have been added only once. So, to get the final answer, we need to subtract the overlapping area from the total area.
#
# two rectangles overlapping with each other
#
#
# Finding the overlap
# To find the overlap, we need to find the width and height of the overlapping area (if there is any). We can get the width by finding the overlap in the horizontal or xxx direction. heightheightheight can be calculated by finding the overlap in the yyy direction.
#
# To find the xxx overlap, let's think about the projection made by the corners of the rectangles on the x-axis. In other words, draw a line perpendicular to the x-axis from both rectangles' bottom left and top right corners. We mark the points at which these lines meet the x-axis. We can see that these points create two line segments - one formed by (ax1,0),(ax2,0)(ax1, 0), (ax2, 0)(ax1,0),(ax2,0), and the other one formed by (bx1,0),(bx2,0)(bx1, 0), (bx2, 0)(bx1,0),(bx2,0).
#
# projection of the rectangles
#
# Now, finding x overlap is equivalent to finding the intersection of these two line segments.
#
# cases where lines don't overlap
#
# cases where lines overlap
#
# From the image above, we can see that if there is an overlap, min(ax2,bx2)−max(ax1,bx1)min(ax2, bx2) - max(ax1, bx1)min(ax2,bx2)−max(ax1,bx1) will be a positive quantity equal to the x overlap of the two rectangles. If the amount is negative or 000, there is no overlap between the two lines (and rectangles).
#
# xOverlap=min(ax2,bx2)−max(ax1,bx1)xOverlap = min(ax2, bx2) - max(ax1, bx1)xOverlap=min(ax2,bx2)−max(ax1,bx1)
#
# In a similar way, we can find the y overlap of the two rectangles.
#
# yOverlap=min(ay2,by2)−max(ay1,by1)yOverlap = min(ay2, by2) - max(ay1, by1)yOverlap=min(ay2,by2)−max(ay1,by1)
#
# The area of the overlap overlap=xOverlap∗yOverlapoverlap = xOverlap * yOverlapoverlap=xOverlap∗yOverlap.
#
# The total area considering the overlap between the two rectangles:
#
# area=areaA+areaB−overlaparea = areaA + areaB - overlaparea=areaA+areaB−overlap
#
# Algorithm
# We are given four points - ax1,ay1,ax2,ay2{ax1, ay1}, {ax2, ay2}ax1,ay1,ax2,ay2 and bx1,by1,bx2,by2{bx1, by1}, {bx2, by2}bx1,by1,bx2,by2.
#
# Calculate areaAareaAareaA and areaBareaBareaB by multiplying width and height of the respective rectangles.
#
# Calculate the xxx overlap:
#
# xOverlap=min(ax2,bx2)−max(ax1,bx1)xOverlap = min(ax2, bx2) - max(ax1, bx1)xOverlap=min(ax2,bx2)−max(ax1,bx1)
#
# Calculate the yyy overlap:
#
# yOverlap=min(ay2,by2)−max(ay1,by1)yOverlap = min(ay2, by2) - max(ay1, by1)yOverlap=min(ay2,by2)−max(ay1,by1)
#
# If xOverlapxOverlapxOverlap and yOverlapyOverlapyOverlap, both are positive, multiply xxx and yyy overlaps to get the area of the overlap. Otherwise, it is 000.
#
# Calculate the total area as - areaA+areaB−overlapareaA + areaB - overlapareaA+areaB−overlap.
#
# Return the total area.

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        "min end > max start"
        overlap_x = overlap_y = 0
        if min(ax2, bx2) > max(ax1, bx1):
            overlap_x = min(ax2, bx2) - max(ax1, bx1)
        if min(ay2, by2) > max(ay1, by1):
            overlap_y = min(ay2, by2) - max(ay1, by1)

        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - overlap_x * overlap_y
