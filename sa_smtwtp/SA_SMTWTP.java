package sa_smtwtp;

import java.util.ArrayList;
import java.util.Collections;

public class SA_SMTWTP {
	public static int totalWeightedTardiness(ArrayList<Job> schedule) {
    		int tardiness;
    		int total = 0;
    		int currentTime = 0;

	  	for (Job job: schedule) {
      			currentTime += job.getProcessingTime();
      			tardiness = Math.max(currentTime - job.getDueDate(), 0);
      			total += job.getWeight() * tardiness;
    		}
	
	  	return total;
  	}

  	public static double acceptanceProbability(int currentTardiness, int neighborTardiness, double temperature) {
    		return Math.exp((currentTardiness - neighborTardiness) / temperature);
  	}
	
  	public static ArrayList<Job> getNeighbor(ArrayList<Job> currentSchedule) {
    		ArrayList<Job> neighborSchedule;

    		// start with a schedule that is exactly the same as the current schedule
	  	neighborSchedule = new ArrayList<Job>();
	  	for (Job job : currentSchedule) {
      			neighborSchedule.add(job);
	  	}
	
	  	// grab two jobs at random
	  	int jobPos1 = (int) (neighborSchedule.size() * Math.random());
	  	int jobPos2 = (int) (neighborSchedule.size() * Math.random());
	  	Job job1 = neighborSchedule.get(jobPos1);
	  	Job job2 = neighborSchedule.get(jobPos2);
		
	  	// swap them
	  	neighborSchedule.set(jobPos1, job2);
	  	neighborSchedule.set(jobPos2, job1);
	
	  	return neighborSchedule;
  	}

  	public static void main(String[] args) {
    		int currentTardiness;
    		int neighborTardiness;
	  	ArrayList<Job> currentSchedule;
    		ArrayList<Job> neighborSchedule;
                
	  	// generate an initial random schedule
	  	currentSchedule = new ArrayList<Job>();
	  	currentSchedule.add(new Job(100, 10, 15));
	  	currentSchedule.add(new Job(25, 5, 1));
	  	currentSchedule.add(new Job(50, 3, 1));
	  	Collections.shuffle(currentSchedule);
		
	  	// get the initial schedule's tardiness
	  	currentTardiness = totalWeightedTardiness(currentSchedule);
	
    		// parameters
	  	double temperature = 100000;
	  	double coolingRate = 0.9;
	
	  	while (temperature > 1) {
      			neighborSchedule = getNeighbor(currentSchedule);
      			neighborTardiness = totalWeightedTardiness(neighborSchedule);
      			if (neighborTardiness <= currentTardiness) { 
           			currentSchedule = neighborSchedule;
		    		currentTardiness = neighborTardiness;
      			} else if (acceptanceProbability(currentTardiness, neighborTardiness, temperature) > Math.random()) {
        			currentSchedule = neighborSchedule;
		    		currentTardiness = neighborTardiness;
      			}
      			temperature *= coolingRate;
    		}
		
	  	System.out.println(currentSchedule);
	  	System.out.println(currentTardiness);
  	}
}
