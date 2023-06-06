package cp213;

import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.File;
import java.lang.String;
/**
 * @author Sahil Khasnobish
 * @version 2021-05-25
 *
 */

public class ScannerTest {
	
	/** Counts all the numbers from user input and outputs the total. 
	 * @param args unused default parameter
	 */
	public static void main(String args[]) {
		
        System.out.println("Enter a series of integers. Press 'q' to quit.");
       
        
        Scanner s = new Scanner(System.in);
      
        int result = 0;
     
        String test = s.next();
        while (test!="q") {
        	if (s.hasNextInt()) {
        		result += s.nextInt();
        	}
        	test = s.next();     
        }
        
        s.close();
        System.out.println("The total is " + result);
        
    }
	
	
	/** Reads and displays each line from a file.
	 * 
	 */
	public void readTokens() {

		Scanner source = null;
		try {
			source = new Scanner(new FileInputStream("src/cp213/test.txt"));
		
		} catch (FileNotFoundException e) {
			System.out.printf("File not found.");
		}
		
		while(source.hasNextLine()) {
			String token = source.nextLine();
			System.out.println(token);
		}
		
	}
	
	/** Reads and displays each line from a file. Count's the lines in the file. 
	 * 
	 */
	public void countLines() {
		Scanner source = null;
		int counter = 0;
		try {
			source = new Scanner(new FileInputStream("src/cp213/test.txt"));
			
		} catch (FileNotFoundException e) {
			System.out.printf("File not found.");
		}
		
		while(source.hasNextLine()) {
			String token = source.nextLine();
			counter+=1;
			System.out.println(token);
		}
		System.out.printf("\nNumber of lines: %d",counter);
		
	}
	

}


