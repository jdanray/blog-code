package dijkstra;

public class Dijkstra {
    private static int INFINITY = 10000;

    public static int[] dijkstra(int[][] graph, int s)
    {
        int[] dist;
        int   num_vertices;
        int   u, v, w;
        Heap  pq;
        
        num_vertices = graph[0].length;
        dist = new int[num_vertices];
        for (int i = 0; i < num_vertices; i++)
            dist[i] = INFINITY;
        dist[s] = 0;
        
        pq = new Heap(num_vertices, false);
        pq.insert(s, dist[s]);

        while (!pq.isEmpty())
        {
            u = pq.remove();

            for (v = 0; v < num_vertices; v++)
            {
                w = graph[u][v];
                
                if (w == -1) 
                    continue;
                
                if (dist[v] > dist[u] + w)
                {
                    dist[v] = dist[u] + w;
                    pq.insert(v, dist[v]);
                }
            }
        }
                
        return dist;
    }
    
    public static void main(String[] args) {
        int graph[][] = {{0, 5, 10}, {-1, 0, 2}, {-1, -1, 0}};
        int start = 0;
        int end   = 2;
        
        int[] dist = dijkstra(graph, start);
       
        System.out.println(dist[end]);
}
