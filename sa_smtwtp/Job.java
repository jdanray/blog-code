package sa_smtwtp;
 
public class Job {
	private int weight;
	private int processingTime;
	private int dueDate;
	
	public Job(int weight, int processingTime, int dueDate) {
		this.weight = weight;
		this.processingTime = processingTime;
		this.dueDate = dueDate;
	}

	public int getWeight() {
		return weight;
	}
	
	public int getProcessingTime() {
		return processingTime;
	}
	
	public int getDueDate() {
		return dueDate;
	}
}
