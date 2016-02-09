package graham_scan;

import java.util.Comparator;

public class Point implements Comparable<Point> {
    private double x;
    private double y;
    
    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }
    
    @Override
    public int compareTo(Point pt) {
        if (this.getY() < pt.getY())
            return -1;
        else if (this.getY() > pt.getY())
            return 1;
        else if (this.getX() < pt.getX())
            return -1;
        else if (this.getX() > pt.getX())
            return 1;
        else
            return 0;
    }
    
    public static int ccw(Point a, Point b, Point c) {
        double d;
        
        d =  (b.getX() - a.getX()) * (c.getY() - a.getY()) - (b.getY() - a.getY()) * (c.getX() - a.getX()); 
        
        if (d > 0.0)
            return -1;
        else if (d < 0.0)
            return 1;
        else
            return 0;
    }
    
    public static double sqDist(Point a, Point b)  {
        double dx; 
        double dy;

        dx = a.getX() - b.getX();
        dy = a.getY() - b.getY();
        
        return (dx * dx) + (dy * dy);
    }    
    
    public Comparator<Point> polarOrder() {
        return new PolarOrder();
    }
    
    private class PolarOrder implements Comparator<Point> {
        @Override
        public int compare(Point a, Point b) {
            int order;
            
            order = Point.ccw(Point.this, a, b);
            
            if (order == 0) {
                if (Point.sqDist(Point.this, a) < Point.sqDist(Point.this, b)) {
                    return -1;
                } else {
                    return 1;
                }
            } else {
                return order;
            }
        }
    }
}
