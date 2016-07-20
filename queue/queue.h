template <typename T>
class Queue {
private:
	struct Node {
		Node() { next = NULL; }
		Node* next;
		T data;
	} *first, *last;
public:
	//Initializes the queue
	Queue() {
		first = NULL;
		last = NULL;
	}
	
	//Deletes all the nodes that have been created
	~Queue() {
		while (!empty()) {
			dequeue();
		}
	}
	
	//Given data, adds an element with that data to the first of the queue
	void enqueue(T d){
		Node* elem = new Node;
		elem->data = d;
	
		if (empty()) {	
			first = elem;
		} else {	
			last->next = elem;
		}
		
		last = elem;
	}
	
	//Removes the first element and returns its data
	T dequeue() {
		if (empty()) {
			throw;
		} else {
			T d = first->data;
			Node* temp = first;
			first = first->next;
			delete temp;
			return d;
		}
	}
	
	//Returns the data of the first element
	T peek() {
		if (empty()) {
			throw;
		} else {
			return first->data;
		}
	}
	
	//Returns true if the queue is empty
	bool empty() {
		return first == NULL;
	}	
};
