package primefactorization;

import java.util.ArrayList;

public class PrimeFactorization {
    public static ArrayList<Integer> primeFactors(int n) {
        ArrayList<Integer> factors = new ArrayList<>();
        
        while (n % 2 == 0) {
            factors.add(2);
            n /= 2;
        }
        
        for (int i = 3; i < n * n; i += 2) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        
        if (n > 2) {
            factors.add(n);
        }
        
        return factors;   
    }
    
    public static void main(String[] args) {
        int n = 28;
        
        System.out.println(primeFactors(n));
    }
}
