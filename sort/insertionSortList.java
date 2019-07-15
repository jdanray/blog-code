public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class insertionSortList {
    public ListNode sort(ListNode head) {
        if (head == null)
            return null;
            
        ListNode node1;
        ListNode node2;
        int tmp;
        int oldval;
            
        node1 = head;
        while (node1 != null) {
            node2 = head;
            while (node2.val < node1.val)
                node2 = node2.next;
            
            oldval = node1.val;
            while (node2 != node1) {
                tmp = oldval;
                oldval = node2.val;
                node2.val = tmp;
                
                node2 = node2.next;
            }
            node1.val = oldval;
            
            node1 = node1.next;
        }
        
        return head;
    }
}
