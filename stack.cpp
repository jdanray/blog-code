template <typename T>
class Stack {
private:
struct Node {
		Node() { next = NULL; }
		T data;
		Node* next;
	} *head;
	int count;
public:
        //Initializes the stack
	Stack() {
		head = NULL;
		count = 0;
	}
	
        //Deletes all the nodes that have been created
	~Stack() {
		while (!empty()) {
			pop();
		}
	}
	
        //Adds an element to the stack
	void push(T x) {
		Node* newNode = new Node;

		newNode->data = x;
		if (head == NULL)
			newNode->next = NULL;
		else
			newNode->next = head;
		head = newNode;
		count++;
	}
	
        //Removes an element from the stack
	void pop() {
		if (!empty()) {
			Node* temp = head;
			head = head->next;
			delete temp;
			temp = NULL;
			count--;
		}
	}
	
        //Returns true if the stack has no elements
	bool empty() const {
		return head == NULL;
	}
	
        //Returns the first element on the stack
	T top() const {
		return head->data;
	}

        //Returns the number of elements on the stack
	int size() const {
		return count;
	}
};
