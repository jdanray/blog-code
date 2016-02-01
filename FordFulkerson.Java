package ford_fulkerson;

import java.util.LinkedList;

public class FordFulkerson {
	private static int[][] flow;

	public static void initFlow(int flowSize) {
        	flow = new int[flowSize][flowSize];

            	for (int u = 0; u < flowSize; u++) {
                	for (int v = 0; v < flowSize; v++) {
                    		flow[u][v] = 0;
                	}
            	}
        }

	public static int[] augmentingPath(int[][] network, int source, int sink) {
		return breadthFirstSearch(network, source, sink);		
	} 
        
 	public static int[] breadthFirstSearch(int[][] graph, int source, int sink) {
		LinkedList<Integer> q = new LinkedList<>();
                int                 u;
		int[]               prev = new int[graph.length];
		boolean[]           seen = new boolean[graph.length];
		
		q.add(source);
		while (!q.isEmpty()) {                    
			u = q.remove();

			if (u == sink) {
                        	return prev;
			}

			for (int v = 0; v < graph[u].length; v++) {
                        	if (!seen[v]) {
                                	if (residualCapacity(graph, u, v) > 0) {                    
						q.add(v);
						prev[v] = u;
						seen[v] = true;
					}
                            	}
			}
		}
		
		return null;
	}
	
	public static int residualCapacity(int[][] flowNetwork, int u, int v) {
		if (flowNetwork[u][v] > 0) {
			return flowNetwork[u][v] - flow[u][v];
		} else if (flowNetwork[v][u] > 0) {
			return flow[v][u];
		} else {
			return 0;
		}
        }
        
        // the residual capacity of a path is the minimum residual capacity over its edges
        public static int residualCapacity(int[] path, int[][] flowNetwork, int source, int sink) {
        	int u;
        	int v;
        	int rc;
        	int minimum;
        
        	minimum = Integer.MAX_VALUE;
		for (v = sink; v != source; v = path[v]) {
            		u = path[v];
            		rc = residualCapacity(flowNetwork, u, v);
            		if (rc < minimum) {
                		minimum = rc;
            		}
        	}
        
        	return minimum;
	}
        
    	public static void augmentFlow(int[] path, int[][] flowNetwork, int source, int sink) {
        	int u;
        	int v;
        	int augment;
        
        	augment = residualCapacity(path, flowNetwork, source, sink);
		for (v = sink; v != source; v = path[v]) {
            		u = path[v];
            		if (flowNetwork[u][v] > 0) {
                		flow[u][v] += augment;
            		} else {
                		flow[u][v] -= augment;
            		}
		}
    	}
        
    	public static void fordFulkerson(int[][] flowNetwork, int source, int sink) {
        	int[] path;
			
            	initFlow(flowNetwork.length);
           
            	while ((path = augmentingPath(flowNetwork, source, sink)) != null) {	
                	augmentFlow(path, flowNetwork, source, sink);	
            	}
    	}
	
	public static void main(String[] args) {
                int     source;
                int     sink;
		int     flowValue;
            	int[][] flowNetwork;
            
                // generate a flow network and designate its source and sink
            	flowNetwork = new int[6][6];
            	for (int u = 0; u < flowNetwork.length; u++) {
                	for (int v = 0; v < flowNetwork[u].length; v++) {
                    		flowNetwork[u][v] = 0;
                	}	
            	}
            	
            	flowNetwork[0][1] = 3;
            	flowNetwork[0][2] = 3;
            	flowNetwork[1][2] = 2;
            	flowNetwork[1][3] = 3;
            	flowNetwork[2][4] = 2;
            	flowNetwork[3][4] = 4;
            	flowNetwork[3][5] = 2;
            	flowNetwork[4][5] = 3;
            	
                source = 0;
                sink = 5;
                
                // compute the max flow of the network
            	fordFulkerson(flowNetwork, source, sink);
 
                // display the flow and its value 
		flowValue = 0;
            	for (int u = 0; u < flow.length; u++) {
                	for (int v = 0; v < flow[u].length; v++) {
                    		System.out.println(u + ", " + v + ": " + flow[u][v]);       
 				if (v == sink) {
 					flowValue += flow[u][v];
 				}
                	}
            	}
            	
            	System.out.println("Maximum flow value: " + flowValue);
    	}
}
