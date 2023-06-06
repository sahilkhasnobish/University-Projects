package cp213;

/**
 * Implements a Popularity Tree. Extends BST.
 *
 * @author Sahil Khasnobish
 * @author David Brown
 * @version 2021-07-05
 */
public class PopularityTree<T extends Comparable<T>> extends BST<T> {

    /**
     * Auxiliary method for {@code valid}. May force node rotation if the retrieval
     * count of the located node value is incremented.
     *
     * @param node The node to examine for key.
     * @param key  The value to search for. Count is updated to count in matching
     *             node value if key is found.
     * @return the updated node.
     */
    private TreeNode<T> retrieveAux(TreeNode<T> node, final CountedValue<T> key) {
    	if(node.getValue() == key) {
    		node.getValue().incrementCount();
    		
    		if(node.getValue().getCount()<node.getLeft().getValue().getCount()) {
        		rotateRight(node);
        	}
        	
        	if(node.getValue().getCount()>node.getRight().getValue().getCount()) {
        		rotateLeft(node);
        	
    	}else {
    		if(key.compareTo(node.getValue())<0) {
    			retrieveAux(node.getLeft(),key);
    		}
    		
    		if(key.compareTo(node.getValue())>0) {
    			retrieveAux(node.getRight(),key);
    		}
    	}
    	}
    return node;
    }

    /**
     * Performs a left rotation around node.
     *
     * @param parent The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateLeft(final TreeNode<T> parent) {
    	
    	TreeNode<T> node_right = parent.getRight();
    	TreeNode<T> node_right_left = node_right.getLeft();
    	
    	node_right.setLeft(parent);
    	parent.setRight(node_right_left);
    	
    	parent.updateHeight();
    	node_right.updateHeight();
    	

	return node_right;
    }

    /**
     * Performs a right rotation around {@code node}.
     *
     * @param parent The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateRight(final TreeNode<T> parent) {

    	TreeNode<T> node_left = parent.getLeft();
    	TreeNode<T> node_left_right = node_left.getRight();
    	
    	node_left.setRight(parent);
    	parent.setLeft(node_left_right);
    	
    	parent.updateHeight();
    	node_left.updateHeight();
    	

	return node_left;
    }

    /**
     * Replaces BST {@code insertAux} - does not increment count on repeated
     * insertion. Counts are incremented only on retrieve.
     */
    @Override
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedValue<T> data) {

    	TreeNode<T> new_node = new TreeNode<T>(data);
    	if(node==null) {
    		if(this.root!=null) {
    			this.root.updateHeight();
    		}
    		node = new_node;
    		node.updateHeight();
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
     * a valid subtree. An Popularity Tree must meet the BST validation conditions,
     * and additionally the counts of any node data must be greater than or equal to
     * the counts of its children.
     *
     * @param node The root of the subtree to test for validity.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    @Override
    protected boolean isValidAux(final TreeNode<T> node) {

    	boolean result = true;
    	if(node!=null) {
    		if(node.getLeft().getValue().compareTo(node.getValue()) > 0 || (node.getRight().getValue().compareTo(node.getValue()) < 0)) {
        		return false;
        	}else if(node.getValue().getCount()<node.getLeft().getValue().getCount() || node.getValue().getCount()<node.getRight().getValue().getCount()) {
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
     * Very similar to the BST retrieve, but increments the character count here
     * instead of in the insertion.
     *
     * @param key The key to search for.
     */
    @Override
    public CountedValue<T> retrieve(CountedValue<T> key) {
    
    	
    	TreeNode<T> node = retrieveAux(this.root,key);
    	
	return node.getValue();
    }

    /**
     * Determines whether two PopularityTrees are identical.
     *
     * @param target The PopularityTree to compare this PopularityTree against.
     * @return true if this PopularityTree and target contain nodes that match in
     *         position, value, count, and height, false otherwise.
     */
    public boolean equals(final PopularityTree<T> target) {
	return super.equals(target);
    }

}
