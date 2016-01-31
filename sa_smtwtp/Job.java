package sa_smtwtp;
 
public class Job {
	private int weight;
	private int processingTime;
	private int dueTime;
	
	public Job(int weight, int processingTime, int dueTime) {
		this.weight = weight;
		this.processingTime = processingTime;
		this.dueTime = dueTime;
	}

	public int getWeight() {
		return weight;
	}
	
	public int getProcessingTime() {
		return processingTime;
	}
	
	public int getDueTime() {
		return dueTime;
	}
}
