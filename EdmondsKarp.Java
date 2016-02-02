package edmonds_karp;

import java.util.LinkedList;

public class EdmondsKarp {
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
                        	if (!seen[v] && residualCapacity(graph, u, v) > 0) {                    
                                        q.add(v);
                                        prev[v] = u;
					seen[v] = true;
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
                flowNetwork = new int[11][11];
                for (int u = 0; u < flowNetwork.length; u++) {
                	for (int v = 0; v < flowNetwork[u].length; v++) {
                    		flowNetwork[u][v] = 0;
                	}	
            	}
                
                source = 0;
                sink = 10;               
                for (int v = 1; v <= 5; v++) flowNetwork[source][v] = 1;
                for (int u = 6; u <= 9; u++) flowNetwork[u][sink] = 1;
                flowNetwork[1][6] = 1;
                flowNetwork[2][6] = 1;
                flowNetwork[2][8] = 1;
                flowNetwork[3][8] = 1;
                flowNetwork[3][9] = 1;
                flowNetwork[4][8] = 1;
                flowNetwork[5][8] = 1;

                // compute the maximum flow of the network
            	fordFulkerson(flowNetwork, source, sink);
                
                // display the flow and its value
                flowValue = 0;
            	for (int u = 0; u < flow.length; u++) {
                	for (int v = 0; v < flow[u].length; v++) {
                    		System.out.println("f(" + u + ", " + v + ") = " + flow[u][v]);
                                if (v == sink) {
                                    flowValue += flow[u][v];
                                }
                	}
            	}
                                
            	System.out.println("Maximum flow value: " + flowValue);
    	}
}
