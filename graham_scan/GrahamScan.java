package graham_scan;

import java.util.Arrays;
import java.util.Stack;

public class GrahamScan {
	public static Stack<Point> grahamScan(Point[] points) {
		Point        top;
        	Stack<Point> hull; 

        	// a hull requires at least three points
        	if (points.length < 3) {
            		return null;
        	}
        
        	// put the leftmost lowest point at the front of the array
        	Arrays.sort(points);
        
		// sort points about the leftmost lowest point by polar angle
        	Arrays.sort(points, 1, points.length, points[0].polarOrder());

        	// put the first three points on the hull
        	hull = new Stack<>();
        	for (int i = 0; i < 3; i++) {
        		hull.push(points[i]);
		}

        	// scan each remaining point
        	// if it lies to the left, then add it
        	// if it doesn't, then remove the last hull point until it does
		for (int i = 3; i < points.length; i++) {
            		top = hull.pop();
            		while (Point.ccw(hull.peek(), top, points[i]) != -1) {
                		top = hull.pop();
            		}
            		hull.push(top);
            		hull.push(points[i]);
		}

		return hull;
    	}
    
    	public static void main(String[] args) {
        	Point        pt;
        	Point[]      points;
        	Stack<Point> convexHull;
        
        	points    = new Point[4];
        	points[0] = new Point(0.0, 0.0);
        	points[1] = new Point(1.0, 1.0);
        	points[2] = new Point(2.0, 2.0);
        	points[3] = new Point(3.0, -1.0);
 
		convexHull = grahamScan(points);
        	while (!convexHull.empty()) {
            		pt = convexHull.pop();
            		System.out.println("(" + pt.getX() + ", " + pt.getY() + ")");
        	}
    	}
}
