package weighted_interval_scheduling;

import java.util.Arrays;
import java.util.Comparator;

class Job {
    public int start;
    public int finish;
    public int value;
    
    public Job(int start, int finish, int value) {
        this.start = start;
        this.finish = finish;
        this.value = value;
    }
}

class JobComparator implements Comparator<Job> {
    @Override
    public int compare(Job a, Job b) {
        return a.finish < b.finish ? -1 : a.finish == b.finish ? 0 : 1;
    }
}

public class WeightedIntervalScheduling {
    static public int bsearch(Job jobs[], int start_index) {
        int lo;
        int hi;
        int mid;
        
        lo = 0;
        hi = start_index - 1;
        while (lo <= hi) {
            mid = (lo + hi) / 2;
            if (jobs[mid].finish <= jobs[start_index].start) {
                if (jobs[mid + 1].finish <= jobs[start_index].start) {
                    lo = mid + 1;
                } else {
                    return mid + 1;
                }
            } else {
                hi = mid - 1;
            }
        }
        
        return 0;
    }
    
    static public int schedule(Job jobs[]) {
        int i;
        int n;
        int p[];
        int V[];
        
        Arrays.sort(jobs, new JobComparator());
        
	n = jobs.length;
        p = new int[n + 1];
        p[0] = 0;
        for (i = 0; i < n; i++)
            p[i + 1] = bsearch(jobs, i);

        V = new int[n + 1];
	V[0] = 0;
        for (i = 1; i < n + 1; i++)
            V[i] = Math.max(jobs[i - 1].value + V[p[i]], V[i - 1]);

	return V[n];
    }            
    
    public static void main(String[] args) {
        Job jobs[] = {new Job(1, 2, 50), new Job(3, 5, 20), new Job(6, 19, 100), new Job(2, 100, 200)};
        System.out.println(schedule(jobs));
    }
}
