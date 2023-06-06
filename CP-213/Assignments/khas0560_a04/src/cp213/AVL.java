package cp213;

/**
 * Implements an AVL (Adelson-Velsky Landis) tree. Extends BST.
 *
 * @author Sahil Khasnobish
 * @author David Brown
 * @version 2021-07-05
 */
public class AVL<T extends Comparable<T>> extends BST<T> {

    /**
     * Returns the balance value of node. If greater than 1, then left heavy, if
     * less than -1, then right heavy. If in the range -1 to 1 inclusive, the node
     * is balanced. Used to determine whether to rotate a node upon insertion.
     *
     * @param node The TreeNode to analyze for balance.
     * @return A balance number.
     */
	
	private int balance_left_aux(TreeNode<T> node, int count) {
		if(node == null) {
			return count;
		}
		return balance_left_aux(node.getLeft(),count+=1);
	}
	private int balance_right_aux(TreeNode<T> node, int count) {
		if(node == null) {
			return count;
		}
		return balance_right_aux(node.getRight(),count+=1);
	}
    private int balance(final TreeNode<T> node) {
    	int result = 0;
    	result = balance_left_aux(node, 0) - balance_right_aux(node, 0);
	return result;
    }

    /**
     * Performs a left rotation around node.
     *
     * @param node The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateLeft(final TreeNode<T> node) {

    	TreeNode<T> node_right = node.getRight();
    	TreeNode<T> node_right_left = node_right.getLeft();
    	
    	node_right.setLeft(node);
    	node.setRight(node_right_left);
    	
    	node.updateHeight();
    	node_right.updateHeight();
    	

	return node_right;
    }

    /**
     * Performs a right rotation around {@code node}.
     *
     * @param node The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateRight(final TreeNode<T> node) {

    	TreeNode<T> node_left = node.getLeft();
    	TreeNode<T> node_left_right = node_left.getRight();
    	
    	node_left.setRight(node);
    	node.setLeft(node_left_right);
    	
    	node.updateHeight();
    	node_left.updateHeight();
    	

	return node_left;
    }

    /**
     * Auxiliary method for {@code insert}. Inserts data into this AVL.
     *
     * @param node the current node (TreeNode)
     * @param data Data to be inserted into the node
     * @return The inserted node.
     */
    @Override
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedValue<T> data) {

    	TreeNode<T> new_node = new TreeNode<T>(data);
    	if(node==null) {
    		if(this.root!=null) {
    			this.root.updateHeight();
    		}
    		node = new_node;
    		node.getValue().incrementCount();
    		return node;
    		
    	}
    	if(data.compareTo(node.getValue())>0) {
    		node.setRight(insertAux(node.getRight(),data));
    		
    	}
    	
    	if(data.compareTo(node.getValue())<0) {
    		node.setLeft(insertAux(node.getLeft(),data));
    	}
    	
    	int balance = balance(node);
    	
    	if(node.getLeft()!=null && node.getRight()!=null) {
    		
        	if(balance>1 && node.getValue().compareTo(node.getLeft().getValue())<0) {
        		rotateRight(node);
        	}
        	if(balance<-1 && node.getValue().compareTo(node.getLeft().getValue())>0) {
        		rotateLeft(node);
        	}
        	if(balance>1 && node.getValue().compareTo(node.getLeft().getValue())>0) {
        		rotateRight(node);
        	}
        	if(balance<-1 && node.getValue().compareTo(node.getRight().getValue())<0) {
        		rotateLeft(node);
        	}
    	
    	}
	return node;
    }

    /**
     * Auxiliary method for {@code valid}. Determines if a subtree based on node is
     * a valid subtree. An AVL must meet the BST validation conditions, and
     * additionally be balanced in all its subtrees - i.e. the difference in height
     * between any two children must be no greater than 1.
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
        	}else if(node.getLeft().getHeight()-node.getRight().getHeight()<-1) {
        		return false;
        	}else if(node.getLeft().getHeight()-node.getRight().getHeight()>1) {
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
     * Determines whether two AVLs are identical.
     *
     * @param target The AVL to compare this AVL against.
     * @return true if this AVL and target contain nodes that match in position,
     *         value, count, and height, false otherwise.
     */
    public boolean equals(final AVL<T> target) {
	return super.equals(target);
    }

}
