package dijkstra;

public class Heap 
{
    private int[]   heap;
    private int[]   values;
    private int[]   indices;
    private boolean maxheap;
    private int     N;
    private int     max_elems;
	
    Heap(int max_elems, boolean maxheap)
    {
        this.N         = 0;
        this.max_elems = max_elems;
        this.heap      = new int[max_elems + 1];
        this.values    = new int[max_elems + 1];
        this.indices   = new int[max_elems + 1];
        this.maxheap   = maxheap;
		
        for (int i = 0; i < max_elems; i++)
	{
            this.heap[i]    = -1;
            this.values[i]  = -1;
            this.indices[i] = -1;
	}
    }

    public boolean contains(int item)
    {
	return this.indices[item] != -1;
    }

    public boolean isEmpty() 
    {
        return this.N == 0;
    }
	
    private void swap(int i, int j)
    {
        int tmp;
		
	tmp = this.heap[i];
	this.heap[i] = this.heap[j];
	this.heap[j] = tmp;
	
	this.indices[this.heap[i]] = i;
	this.indices[this.heap[j]] = j;
    }

    private boolean isPrior(int i, int j)
    {
        if (this.maxheap)
            return this.values[this.heap[i]] > this.values[this.heap[j]];
	else
            return this.values[this.heap[i]] < this.values[this.heap[j]];
    }

    public void bubbleUp(int pos)
    {
        int parent;
		
	parent = pos / 2;
        while (parent >= 1 && isPrior(pos, parent))
	{
            swap(pos, parent);

            pos = parent;
            parent = pos / 2;
        }
    }
            
    public void bubbleDown(int pos)
    {
        int left;
	int right;
        int m;
        
        left = pos * 2;
        while (left < this.N)
	{
            right = left + 1;
            if (right < this.N && isPrior(right, left))
                m = right;
            else
                m = left;

            if (!isPrior(m, pos))
                break;
            
            swap(pos, m);
            
            pos = m;
            left = pos * 2;
	}
    }	
	
    public void insert(int item, int val)
    {
        if (this.N + 1 <= max_elems)
	{
            this.N++;
            this.heap[this.N] = item;
            this.indices[item] = this.N;
            this.values[item] = val;
            bubbleUp(this.N);
        }
    }
	
    public int remove()
    {
        int m;
		
        if (isEmpty())
            return -1;
        
        m = this.heap[1];
		
        swap(1, this.N);
        this.N--;
		
        bubbleDown(1);
	
        this.indices[m]  = -1;
        this.heap[N + 1] = -1;

        return m;
    }

    public void update(int item, int val)
    {
        int pos;
		
        this.values[item] = val;
		
        pos = this.indices[item];
        bubbleUp(pos);
    }
}
