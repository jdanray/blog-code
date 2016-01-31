package sa_smtwtp;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class SA_SMTWTP {
	public static int totalWeightedTardiness(ArrayList<Job> schedule) {
    		int tardiness;
    		int total = 0;
    		int currentTime = 0;

	  	for (Job job: schedule) {
      			currentTime += job.getProcessingTime();
      			tardiness = Math.max(currentTime - job.getDueTime(), 0);
      			total += job.getWeight() * tardiness;
    		}
	
	  	return total;
  	}

  	public static boolean acceptNeighbor(int currentTardiness, int neighborTardiness, double temperature) {
  		Random rand;
  		
        	if (neighborTardiness <= currentTardiness) { 
           		return true;
		} else {
			rand = new Random();
        		return acceptanceProbability(currentTardiness, neighborTardiness, temperature) > rand.nextDouble();
		}
  	}
	
        public static double acceptanceProbability(int currentTardiness, int neighborTardiness, double temperature) {
                return Math.exp((currentTardiness - neighborTardiness) / temperature);
  	}
        
  	public static ArrayList<Job> getNeighbor(ArrayList<Job> currentSchedule) {
  		int            jobPos1;
  		int            jobPos2;
  		Job            job1;
  		Job            job2;
    		ArrayList<Job> neighborSchedule;
                Random         rand;

    		// start with a schedule that is exactly the same as the current schedule
	  	neighborSchedule = new ArrayList<Job>();
	  	for (Job job : currentSchedule) {
      			neighborSchedule.add(job);
	  	}
	
	  	// grab two jobs at random
	  	rand    = new Random();
	  	jobPos1 = rand.nextInt(neighborSchedule.size());
	  	jobPos2 = rand.nextInt(neighborSchedule.size());
	  	job1    = neighborSchedule.get(jobPos1);
	  	job2    = neighborSchedule.get(jobPos2);
		
	  	// swap them
	  	neighborSchedule.set(jobPos1, job2);
	  	neighborSchedule.set(jobPos2, job1);
	
	  	return neighborSchedule;
  	}
        
        public static ArrayList<Job> anneal() {
    		int            currentTardiness;
    		int            neighborTardiness;
    		double         temperature;
    		double         coolingRate;
    		ArrayList<Job> currentSchedule;
                ArrayList<Job> neighborSchedule;
	
    		// parameters
	  	temperature = 100000;
	  	coolingRate = 0.9;

	  	// generate an initial random schedule
	  	currentSchedule = new ArrayList<Job>();
	  	currentSchedule.add(new Job(100, 10, 15));
	  	currentSchedule.add(new Job(25, 5, 1));
	  	currentSchedule.add(new Job(50, 3, 1));
	  	Collections.shuffle(currentSchedule);
                
                // compute the initial schedule's tardiness
	  	currentTardiness = totalWeightedTardiness(currentSchedule);
	
                // anneal
	  	while (temperature > 1) {
                        neighborSchedule  = getNeighbor(currentSchedule);
      			neighborTardiness = totalWeightedTardiness(neighborSchedule);
			if (acceptNeighbor(currentTardiness, neighborTardiness, temperature)) {
                                currentSchedule  = neighborSchedule;
                                currentTardiness = neighborTardiness;
			}
      			temperature *= coolingRate;
    		}        
                
                return currentSchedule;
        }
        
  	public static void main(String[] args) {
	  	System.out.println(anneal());
  	}
}
