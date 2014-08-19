#include <stack>
#include <queue>

//Returns true if a string is a palindrome
bool palindrome(string word) {
	queue<char> q;
	stack<char> s;

	for (unsigned int i = 0; i < word.length(); i++) {
		q.push(word[i]);
		s.push(word[i]);
	}
	
	for (unsigned int i = 0; i < word.length(); i++) {
		if (s.top() == q.front()) {
			s.pop();
			q.pop();
		} else {
			return false;
		}
	}
	
	return true;
}
