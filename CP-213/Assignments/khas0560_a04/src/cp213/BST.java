package cp213;

import java.util.ArrayList;

/**
 * Implements a Binary Search Tree.
 *
 * @author Sahil Khasnobish
 * @author David Brown
 * @version 2021-07-05
 */
public class BST<T extends Comparable<T>> {
    protected int comparisons = 0; // Count of comparisons performed by tree.

    // Attributes.
    protected TreeNode<T> root = null; // Root node of the tree.
    protected int size = 0; // Number of elements in the tree.

    /**
     * Auxiliary method for {@code equals}. Determines whether two subtrees are
     * identical in values and height.
     *
     * @param source Node of this BST.
     * @param target Node of that BST.
     * @return true if source and target are identical in values and height.
     */
    protected boolean equalsAux(final TreeNode<T> source, final TreeNode<T> target) {
    	boolean result = true;
    	if(source.getHeight()!=target.getHeight()) {
    		result = false;
    	}else {
    		TreeNode<T> source_node = source;
    		TreeNode<T> target_node = source;
    		while(source_node!=null && target_node!=null) {
    			if(source_node.getValue() != target_node.getValue()) {
    				return false;
    			}
    			source_node = source_node.getLeft();
    			target_node = target_node.getLeft();
    		}
    		
    		while(source_node!=null && target_node!=null) {
    			if(source_node.getValue() != target_node.getValue()) {
    				return false;
    			}
    			source_node = source_node.getRight();
    			target_node = target_node.getRight();
    		}
    		
    		if(source_node==null && target_node!=null) {
    			result = false;
    		}else if(target_node==null && source_node!=null) {
    			result = false;
    		}
    	}
		

	return result;
    }

    /**
     * Auxiliary method for {@code insert}. Inserts data into this BST.
     *
     * @param node the current node (TreeNode)
     * @param data data to be inserted into the node
     * @return the inserted node.
     */
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedValue<T> data) {
    	TreeNode<T> new_node = new TreeNode<T>(data);
    	if(node==null) {
    		if(this.root!=null) {
    			this.root.updateHeight();
    		}
    		node = new_node;
    		node.updateHeight();
    		node.getValue().incrementCount();
    		return node;
    		
    	}
    	if(data.compareTo(node.getValue())>0) {
    		node.setRight(insertAux(node.getRight(),data));
    		node.updateHeight();
    		
    	}
    	
    	if(data.compareTo(node.getValue())<0) {
    		node.setLeft(insertAux(node.getLeft(),data));
    		node.updateHeight();
    	}
    	
	return node;
    }

    /**
     * Auxiliary method for {@code valid}. Determines if a subtree based on node is
     * a valid subtree.
     *
     * @param node The root of the subtree to test for validity.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    protected boolean isValidAux(final TreeNode<T> node) {
    	boolean result = true;
    	if(node!=null) {
    		if(node.getLeft().getValue().compareTo(node.getValue()) > 0 || (node.getRight().getValue().compareTo(node.getValue()) < 0)) {
        		return false;
        	}
    	}else {
    		result = true;
    	}
    	
    	isValidAux(node.getLeft());
    	isValidAux(node.getRight());
    	
    	

	return result;
    }

    /**
     * Returns the height of a given TreeNode.
     *
     * @param node The TreeNode to determine the height of.
     * @return The value of the height attribute of node, 0 if node is null.
     */
    protected int nodeHeight(final TreeNode<T> node) {
	int height = 0;

	if (node != null) {
	    height = node.getHeight();
	}
	return height;
    }

    /**
     * Determines if this BST contains key.
     *
     * @param key The key to search for.
     * @return true if this BST contains key, false otherwise.
     */
    public boolean contains(final CountedValue<T> key) {

    	int i = 0;
    	TreeNode<T> node = this.root;
    	while(i<this.size && node.getValue()!=key) {
    		if(key.compareTo(node.getValue())>0) {
    			node = node.getRight();
    		}else if(key.compareTo(node.getValue())>0) {
    			node = node.getLeft();
    		}
    	}
    	
    	if(i==size) {
    		return false;
    	}
    	return true;
    }

    /**
     * Determines whether two BSTs are identical.
     *
     * @param target The BST to compare this BST against.
     * @return true if this BST and that BST contain nodes that match in position,
     *         value, count, and height, false otherwise.
     */
    public boolean equals(final BST<T> target) {
	boolean isEqual = false;

	if (this.size == target.size) {
	    isEqual = this.equalsAux(this.root, target.root);
	}
	return isEqual;
    }

    /**
     * Get number of comparisons executed by the {@code retrieve} method.
     *
     * @return comparisons
     */
    public int getComparisons() {
	return this.comparisons;
    }

    /**
     * Returns the height of the root node of this BST.
     *
     * @return height of root node, 0 if the root node is null.
     */
    public int getHeight() {
	int height = 0;

	if (this.root != null) {
	    height = this.root.getHeight();
	}
	return height;
    }

    /**
     * Returns the number of nodes in the BST.
     *
     * @return number of node in this BST.
     */
    public int getSize() {
	return this.size;
    }

    /**
     * Returns an array of copies of CountedValue objects in a linked data
     * structure. The array contents are in data order from smallest to largest.
     *
     * Not thread safe as it assumes contents of data structure are not changed by
     * an external thread during the copy loop. If data elements are added or
     * removed by an external thread while the data is being copied to the array,
     * then the declared array size may no longer be valid.
     *
     * @return this tree data as an array of data.
     */
    public ArrayList<CountedValue<T>> inOrder() {
	return this.root.inOrder();
    }

    /**
     * Inserts data into this BST.
     *
     * @param data Data to store.
     */
    public void insert(final CountedValue<T> data) {
    	
    	this.root = insertAux(this.root,data);
    	

	return;
    }

    /**
     * Determines if this BST is empty.
     *
     * @return true if this BST is empty, false otherwise.
     */
    public boolean isEmpty() {
	return this.root == null;
    }

    /**
     * Determines if this BST is a valid BST; i.e. a node's left child data is
     * smaller than its data, and its right child data is greater than its data, and
     * a node's height is equal to the maximum of the heights of its two children
     * (empty child nodes have a height of 0), plus 1.
     *
     * @return true if this BST is a valid BST, false otherwise.
     */
    public boolean isValid() {
	return this.isValidAux(this.root);
    }

    /**
     * Returns an array of copies of CountedValue objects int a linked data
     * structure. The array contents are in level order starting from the root
     * (this) node. Helps determine the structure of the tree.
     *
     * Not thread safe as it assumes contents of data structure are not changed by
     * an external thread during the copy loop. If data elements are added or
     * removed by an external thread while the data is being copied to the array,
     * then the declared array size may no longer be valid.
     *
     * @return this tree values as an array of values.
     */
    public ArrayList<CountedValue<T>> levelOrder() {
	return this.root.levelOrder();
    }

    /**
     * Resets the comparison count to 0.
     */
    public void resetComparisons() {
	this.comparisons = 0;
	return;
    }

    /**
     * Retrieves a copy of value matching key (key should have value count of 0).
     * Returning a complete CountedValue gives access to the value and count.
     *
     * @param key The key to look for.
     * @return data The complete CountedValue that matches key, null otherwise.
     */
    public CountedValue<T> retrieve(final CountedValue<T> key) {
    	int i = 0;
    	TreeNode<T> node = this.root;
    	while(i<this.size && node.getValue()!=key) {
    		if(key.compareTo(node.getValue())>0) {
    			node = node.getRight();
    		}else if(key.compareTo(node.getValue())>0) {
    			node = node.getLeft();
    		}
    	}
    	
    	if(i==size) {
    		return null;
    	}
    	return node.getValue();
    }
}
