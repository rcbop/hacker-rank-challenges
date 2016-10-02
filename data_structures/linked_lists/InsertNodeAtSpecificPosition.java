/*
  Insert Node at a given position in a linked list
  head can be NULL
  First element in the linked list is at position 0
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/

Node InsertNth(Node head, int data, int position) {
   // This is a "method-only" submission.
    // You only need to complete this method.
    //System.out.println("calling: " + head.data + " d: "+ data+ " pos " + position);
    Node newNode = new Node();
    newNode.data = data;

    if ( position == 0 ) {
        newNode.next = head;
        return newNode;
    }

    int i = 1;
    Node start = head;
    while(i++ < position){
        //System.out.println(" i: "+i+" d: "+start.data+ " pos: "+position);
        start = start.next;
    }

    Node tmp = start.next;
    start.next = newNode;
    newNode.next = tmp;

    return head;
}
