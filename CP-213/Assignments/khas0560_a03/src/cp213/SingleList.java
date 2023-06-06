package cp213;

/**
 * COMPLETE THE CODE AT // your code here
 *
 * A single linked list structure of <code>Node T</code> objects. These value
 * objects must be Comparable - i.e. they must provide the compareTo method.
 * Only the <code>T</code> value contained in the priority queue is visible
 * through the standard priority queue methods. Extends the
 * <code>SingleLink</code> class.
 *
 * @author // Sahil Khasnobish, 190990560, khas0560@mylaurier.ca
 * @version 2021-06-16
 * @param <T> this SingleList value type.
 */
public class SingleList<T extends Comparable<T>> extends SingleLink<T> {

    /**
     * Searches for the first occurrence of key in this SingleList. Private helper
     * methods - used only by other ADT methods.
     *
     * @param key The value to look for.
     * @return A pointer to the node previous to the node containing key.
     */
    private SingleNode<T> linearSearch(final T key) {
    	int i=0;
    	SingleNode<T> node = this.front;
    	SingleNode<T> result = this.front;
    	
    	while(i<this.length){
    		if(node.getNext().getValue() == key) {
    			result = node;
    		}
    		node = node.getNext();
            i++;
        }

    return result;
    }
    public SingleList() {
    	super();
    }
    /**
     * Appends value to the end of this SingleList.
     *
     * @param value The value to append.
     */
    public void append(final T value) {
    	SingleNode <T> node = new SingleNode <T>(value,null);
    	if(this.length == 0) {
    		this.rear = node;
    		this.front = this.rear;
    	}else {
    		this.rear.setNext(node);
        	this.rear = node;
    	}
    	this.length+=1;
    	

	return;
    }

    /**
     * Removes duplicates from this SingleList. The list contains one and only one
     * of each value formerly present in this SingleList. The first occurrence of
     * each value is preserved.
     */
    public void clean() { 
    int count = 0;
    SingleNode <T> temp = this.front;
    SingleNode <T> node = this.front;
	for(int i=0;i<this.length;i++) {
		count=0;
		for(int j=0;j<this.length;j++) {
			if(this.get(i) == this.get(j)) {
				count++;
			}
		}
		node = temp;
		temp = temp.getNext();
		if(count>1) {
			System.out.println("test");
			node.setNext(temp.getNext());
		}
	}

	return;
    }

    /**
     * Combines contents of two lists into a third. Values are alternated from the
     * origin lists into this SingleList. The origin lists are empty when finished.
     * NOTE: value must not be moved, only nodes.
     *
     * @param left  The first list to combine with this SingleList.
     * @param right The second list to combine with this SingleList.
     */
    public void combine(final SingleList<T> left, final SingleList<T> right) {

	//first list: i+2
    //second list:(i+1)+2
    	int i=0;
    	int length = left.length+right.length;
    	for(i=0;i<length;i++) {
    		i+=1;
    		this.insert(i, left.get(i));
    		this.insert(i+1, right.get(i));
    		
    	}
    	

	return;
    }

    /**
     * Determines if this SingleList contains key.
     *
     * @param key The key value to look for.
     * @return true if key is in this SingleList, false otherwise.
     */
    public boolean contains(final T key) {
    	boolean result = false;
    	SingleNode <T> temp = this.front;
    	for(int j=0;j<this.length;j++) {
			if(temp.getValue() == key) {
				return true;
			}
			temp = temp.getNext();
		}
	return result;
    }

    /**
     * Finds the number of times key appears in list.
     *
     * @param key The value to look for.
     * @return The number of times key appears in this SingleList.
     */
    public int count(final T key) {

    	int count = 0;
    	for(int i=0;i<this.length;i++) {
			if(this.get(i) == key) {
				count+=1;
			}
    	}
	return count;
    }

    /**
     * Finds and returns the value in list that matches key.
     *
     * @param key The value to search for.
     * @return The value that matches key, null otherwise.
     */
    public T find(final T key) {
    	SingleNode <T> temp = this.front;
    	for(int j=0;j<this.length;j++) {
    		if(temp==null) {
    			return null;
    		}else if(temp.getValue() == key) {
				return temp.getValue();
			}
			temp = temp.getNext();
		}
    	return null;
    }

    /**
     * Get the nth item in this SingleList.
     *
     * @param n The index of the item to return.
     * @return The nth item in this SingleList.
     * @throws ArrayIndexOutOfBoundsException if n is not a valid index.
     */
    public T get(final int n) throws ArrayIndexOutOfBoundsException {
    	int i=0;
    	SingleNode <T>node = this.front;
    	while(i<n){
    		node = node.getNext();
            i++;
        }
	return node.getValue();
    }

    /**
     * Determines whether two lists are identical.
     *
     * @param source The list to compare against this SingleList.
     * @return true if this SingleList contains the same values in the same order as
     *         source, false otherwise.
     */
    public boolean identical(final SingleList<T> source) {

    	int i=0;
    	boolean result = true;
    	SingleNode <T>node1 = this.front;
    	SingleNode <T>node2 = source.front;
    	
    	if(this.length!=source.length) {
    		result = false;
    	}
    	
    	while(i<this.length){
    		if(node1.getValue()!=node2.getValue()) {
    			result = false;
    		}
    		node1 = node1.getNext();
    		node2 = node2.getNext();
            i++;
        }

	return result;
    }

    /**
     * Finds the first location of a value by key in this SingleList.
     *
     * @param key The value to search for.
     * @return The index of key in this SingleList, -1 otherwise.
     */
    public int index(final T key) {

    	SingleNode <T> temp = this.front;
    	for(int j=0;j<this.length;j++) {
    		if(temp==null) {
    			return -1;
    		}else if(temp.getValue() == key) {
				return j;
			}
			temp = temp.getNext();
		};

	return -1;
    }

    /**
     * Inserts value into this SingleList at index i. If i greater than the length
     * of this SingleList, append value to the end of this SingleList.
     *
     * @param i     The index to insert the new value at.
     * @param value The new value to insert into this SingleList.
     */
    public void insert(int i, final T value) {
    	int n=0;
    	if(i>this.length) {
    		SingleNode <T>node = new SingleNode<T>(value,null);
    		this.rear.setNext(node);
    		this.rear = node;
    		
    	}else {
    		SingleNode<T> node = new SingleNode<T>(value,null);
    		SingleNode <T>temp = this.front;
    		if(i==0) {
    			node.setNext(front);
    			this.front = node;
    		}else {
    			for(n=0;n<i-1;n++) {
            		temp = temp.getNext();
            	}
        		if(temp!=null) {
        			
        		}
        		node.setNext(temp.getNext());
        		temp.setNext(node);
        	
    		}
    		this.length+=1;
    		
    		
    	}
    	

	return;
    }

    /**
     * Creates an intersection of two other SingleLists into this SingleList. Copies
     * value to this SingleList. left and right SingleLists are unchanged. Values
     * from left are copied in order first, then values from right are copied in
     * order.
     *
     * @param left  The first SingleList to create an intersection from.
     * @param right The second SingleList to create an intersection from.
     */
    public void intersection(final SingleList<T> left, final SingleList<T> right) {

	// your code here

	return;
    }

    /**
     * Finds the maximum value in this SingleList.
     *
     * @return The maximum value.
     */
    public T max() {
    	T max = this.front.getValue();
    	//SingleNode <T> max = this.front;
    	SingleNode <T> node = this.front;
    	for(int j=0;j<this.length;j++) {
    		if(node.getValue().compareTo(max) > 0) {
    			max = node.getValue();
			}
			node = node.getNext();
		}

	return max;
    }

    /**
     * Finds the minimum value in this SingleList.
     *
     * @return The minimum value.
     */
    public T min() {

    	T min = this.front.getValue();
    	//SingleNode <T> max = this.front;
    	SingleNode <T> node = this.front;
    	for(int j=0;j<this.length;j++) {
    		if(node.getValue().compareTo(min) < 0) {
    			min = node.getValue();
			}
			node = node.getNext();
		}

	return min;
    }

    /**
     * Inserts value into the front of this SingleList.
     *
     * @param value The value to insert into the front of this SingleList.
     */
    public void prepend(final T value) {
    	insert(0,value);

	return;
    }

    /**
     * Finds, removes, and returns the value in this SingleList that matches key.
     *
     * @param key The value to search for.
     * @return The value matching key, null otherwise.
     */
    public T remove(final T key) {
    
    	SingleNode<T> node = this.front;
		SingleNode <T>temp = this.front;
		int n=0;
		while(temp.getNext()!=null && node.getValue()!=key) {
			node = temp;
			temp = temp.getNext();
			n++;
		}
		T result = temp.getValue();
		node.setNext(temp.getNext());

	return result;
    }

    /**
     * Removes the value at the front of this SingleList.
     *
     * @return The value at the front of this SingleList.
     */
    public T removeFront() {
    	SingleNode<T> result = this.front;
    	this.front = this.front.getNext();

	return result.getValue();
    }

    /**
     * Finds and removes all values in this SingleList that match key.
     *
     * @param key The value to search for.
     */
    public void removeMany(final T key) {
    	SingleNode<T> node = this.front;
    	SingleList<T> list = new SingleList<>();
    	for(int i=0;i<this.length;i++) {
    		list.insert(i, node.getValue());
    	}
    	SingleNode<T>temp = list.front;
    	for(int j=0;j<list.length;j++) {
    		temp = temp.getNext();
    	}
    	SingleNode<T> node2 = this.front;
    	if(this.contains(key)==false) {
    		return;
    	}else {
    		int i=0;
    		while(i<list.length && node2!=null) {
    			if(node2.getValue()==key) {
    				this.remove(key);
    				this.length-=1;
    			}
    			i++;
    			node2 = node2.getNext();
    			
    		}
    	}
    	

	return;
    }

    /**
     * Reverses the order of the values in this SingleList.
     */
    public void reverse() {

    	SingleNode<T> node = this.front;
    	SingleList<T> list = new SingleList<>();
    	for(int i=0;i<this.length;i++) {
    		list.insert(i, node.getValue());
    	}
    	int count = this.length;
    	for(count = this.length;count==0;count--) {
    		this.insert(count, node.getValue());
    	}

	return;
    }

    /**
     * Splits the contents of this SingleList into the left and right SingleLists.
     * Moves nodes only - does not move value or call the high-level methods insert
     * or remove. this SingleList is empty when done. The first half of this
     * SingleList is moved to left, and the last half of this SingleList is moved to
     * right. If the resulting lengths are not the same, left should have one more
     * item than right. Order is preserved.
     *
     * @param left  The first SingleList to move nodes to.
     * @param right The second SingleList to move nodes to.
     */
    public void split(final SingleList<T> left, final SingleList<T> right) {

	// your code here

	return;
    }

    /**
     * Splits the contents of this SingleList into the left and right SingleLists.
     * Moves nodes only - does not move value or call the high-level methods insert
     * or remove. this SingleList is empty when done. Nodes are moved alternately
     * from this SingleList to left and right. Order is preserved.
     *
     * @param left  The first SingleList to move nodes to.
     * @param right The second SingleList to move nodes to.
     */
    public void splitAlternate(final SingleList<T> left, final SingleList<T> right) {

	// your code here

	return;
    }

    /**
     * Creates a union of two other SingleLists into this SingleList. Copies value
     * to this list. left and right SingleLists are unchanged. Values from left are
     * copied in order first, then values from right are copied in order.
     *
     * @param left  The first SingleList to create a union from.
     * @param right The second SingleList to create a union from.
     */
    public void union(final SingleList<T> left, final SingleList<T> right) {
    	
    	SingleNode<T> node2 = right.front;
    	for(int j=0;j<right.length;j++) {
    		this.insert(j, node2.getValue());
    		node2 = node2.getNext();
    	}
    	
    	SingleNode<T> node = left.front;
    	for(int i=0;i<left.length;i++) {
    		this.insert(i, node.getValue());
    		node = node.getNext();
    	}

	return;
    }
}
