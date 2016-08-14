package prime_factorization;

import java.util.ArrayList;

public class PrimeFactorization {
    public static ArrayList<Integer> primeFactors(int n) {
        ArrayList<Integer> factors = new ArrayList<>();
        
        // divide by 2 until n is no longer even
        while (n % 2 == 0) {
            factors.add(2);
            n /= 2;
        }
 
        // divide by all the odd primes that divide n
        for (int i = 3; i < n * n; i += 2) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        
        // if n doesn't reduce to 1, include it
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
