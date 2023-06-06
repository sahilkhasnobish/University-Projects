package cp213;

import java.util.Scanner;

public class Main {

    /**
     * @param args unused
     */
    public static void main(String[] args) {
	System.out.println("Test scannerTest");
	System.out.println();
	int total = scannerTest();
	System.out.println("Total: " + total);
	System.out.println();

	System.out.print("Test stringPrinter");
	// provide the try/catch block to call:

	// start block
	String output = stringPrinter(5, "*");
	System.out.println(output);
	output = stringPrinter(-5, "*");
	System.out.println(output);
	// end block

    }

    /**
     * Uses exceptions to capture bad input from a keyboard Scanner.
     *
     * @return The total of all the integers entered.
     */
    public static int scannerTest() {
    	Scanner input = new Scanner(System.in);
    	int total = 0;
    	int temp = 0;
    	while(input.next()!="Quit") {
    		try {
    			temp = input.nextInt();
        		total+=temp;
    		}catch (java.util.InputMismatchException e) {
    			System.out.println("That is not an integer!");
    	        input.next(); 
    		}
    		
    	}

	return total;
    }

    /**
     * Repeats a string.
     *
     * @param n   Number of times to repeat a string.
     * @param str The string to print.
     * @return The repeated string.
     * @throws Exception If n is negative.
     */
    public static String stringPrinter(int n, String str) throws Exception {
    	
    	
    	try {
	    	String result = str;
	    	for(int i=0;i<n;i++) {
	    		result.concat(str);
	    	}
    	}catch(

	return null;
    }

}
