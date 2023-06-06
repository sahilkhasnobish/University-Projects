package cp213;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Arrays Lab task methods.
 *
 * @author Sahil Khasnobish
 * @version 2021-06-07
 */
public class ArrayTest {

    /**
     * Tests arrays.
     *
     * @param args unused default parameter
     */
    public static void main(final String[] args) {
	System.out.println("Task 1");
	System.out.println(ArrayTest.task1());
	System.out.println("Task 2");
	System.out.println(ArrayTest.task2());
	System.out.println("Task 3");
	System.out.println(ArrayTest.task3());
	System.out.println("Task 4");
	System.out.println(ArrayTest.task4());
	System.out.println("Task 5");
	System.out.println(Arrays.toString(ArrayTest.task5()));
	
    }

    /**
     * Print the contents of the arrays first and second using a standard for loop.
     *
     * @return true if second contains the same values as first, false otherwise
     */
    public static boolean task1() {
	final int[] first = { 1, 3, 5, 7, 9 };
	final int[] second = first;
	
	System.out.println("Values in first:");

	  for (int i = 0; i < first.length; i++) {
	      System.out.println(first[i]);
	  }
	  System.out.println("Values in second:");

	  for (int i = 0; i < second.length; i++) {
	      System.out.println(second[i]);
	  }

	return true;
    }

    /**
     * Double the contents of the array first with a standard for loop.
     *
     * @return true if second contains the same values as first, false otherwise
     */
    public static boolean task2() {
	final int[] first = { 1, 3, 5, 7, 9 };
	final int[] second = first;
	for (int n=0;n<first.length;n++) {
	      first[n] *=2 ;

	  }
	
	System.out.println("Values in first:");

	  for (int i = 0; i < first.length; i++) {
	      System.out.println(first[i]);
	  }
	  System.out.println("Values in second:");

	  for (int i = 0; i < second.length; i++) {
	      System.out.println(second[i]);
	  }

	return true;
    }

    /**
     * Double the contents of the array first with an enhanced for loop.
     *
     * @return true if the values in first are permanently changed, false otherwise
     */
    public static boolean task3() {
	final int[] first = { 1, 3, 5, 7, 9 };
	int count = 0;
	for (int n : first) {
	      n *=2 ;
	      first[count] = n;
	      count+=1;

	  }
	
	System.out.println("Values in first:");

	  for (int i = 0; i < first.length; i++) {
	      System.out.println(first[i]);
	  }
	  

	return true;
    }

    /**
     * Attempt to assign the array first to a row of the 2D array third.
     *
     * @return true if this is allowed, false otherwise
     */
    public static boolean task4() {
	final int[] first = { 1, 3, 5, 7, 9 };
	final int[][] third = new int[2][first.length];

	third[0] = first;
	/*
	for (int i = 0; i < first.length; i++) {
		for (int n = 0; n < first.length; n++) {
		      System.out.println(third[i][n]);
		  }
	  }
	 */
	return true;
    }

    /**
     * Assign the values 1 through 10 to an Integer ArrayList.
     *
     * @return the contents of the ArrayList as an Integer[] array.
     */
    public static Integer[] task5() {
	final ArrayList<Integer> values = new ArrayList<>();
	
	for(int i = 0 ; i < 10 ; i++) {
	    values.add(i);
	}
	
	
	Integer[] valuesArray = values.toArray(new Integer[values.size()]);
	
	
	return valuesArray;
    }
}
