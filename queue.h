template <typename T>
class Queue {
private:
	struct Node {
		Node() { next = NULL; }
		Node* next;
		T data;
	} *front, *rear;
public:
	//Initializes the queue
	Queue() {
		front = NULL;
		rear = NULL;
	}
	
	//Deletes all the nodes that have been created
	~Queue() {
		while (!empty()) {
			dequeue();
		}
	}
	
	//Given data, adds an element with that data to the front of the queue
	void enqueue(T d){
		Node* elem = new Node;
		elem->data = d;
	
		if (empty()) {	
			front = elem;
		} else {	
			rear->next = elem;
		}
		
		rear = elem;
	}
	
	//Removes the front element
	void dequeue() {
		if (!empty()) {
			Node* temp = front;
			front = front->next;
			delete temp;
		}
	}
	
	//Returns the data of the front element
	T peek() {
		if (empty()) {
			throw;
		} else {
			return front->data;
		}
	}
	
	//Returns true if the queue is empty
	bool empty() {
		return front == NULL;
	}	
};
