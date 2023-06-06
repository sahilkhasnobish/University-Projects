package cp213;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author Sahil Khasnobish, 190990560, khas0560@mylaurier.ca
 * @version 2021-06-14
 */
public class A02_Main {
    // Constants
    public static final String SEP = "-".repeat(40);

    public static void main(String[] args) {

    	//TESTING CLOSEST
    	//System.out.printf("Closest: %f",A02.majorsStringToList("2,3,6"));
    	//System.out.println(StudentUtrilities.majorsStringToList("2,3,6"));
    	
    	//LocalDate now = LocalDate.now();  
    	//Integer[] majors = {0,1};
    	//Student test = new Student(123456,"k","sahil",now, majors);
    	//String test1 = Student.majorsStringToList(SEP);
    	
    	//TESTING MAJORS_STRING_TO_LIST
    	/*
    	Integer[] test2 = Student.majorsStringToList("2,4,5");
    	int length = test2.length;
    	for(int i=0;i<length;i++) {
    		System.out.println(test2[i]);
    	}
    	*/
    	//TESTING COMPARE TO  
    	/*
    	LocalDate now2 = LocalDate.now();  
    	Integer[] majors2 = {2,3};
    	Student test = new Student(123456,"k","sahil",now, majors);
    	Student test2 = new Student(923451,"Brown","Tasmin",now, majors);
    	int result = test.compareTo(test2);
    	
    	System.out.println(result);
    	*/
    	/*
    	//TESTING majorsListToNames 
    	
    	Student test = new Student(123456,"k","sahil",now, majors);
    	String result = test.majorsListToNames();
    	System.out.println(result);
    	*/
    	//TESTING toString 
    	/*
    	Student test = new Student(123456,"k","sahil",now, majors);
    	String result = test.toString();
    	System.out.println(result);
    	*/
    	
    	
    	//TESTING write
    	/*
    	Student test = new Student(123456,"k","sahil",now, majors);
    	//File text = new File(A02_Main.class.getResource("test.txt").getFile());
    	
    	PrintStream ps;
		try {
			ps = new PrintStream("test.txt");
			test.write(ps);
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			System.out.println("File not found");
		}
    	*/
    	
    	
    	//TESTING getStudent
    	/*
    	final ArrayList<Student> student_list = new ArrayList<>();
    	//Student student = StudentUtilities.getStudent(new Scanner(System.in));
    	for(int i=0;i<10;i++) {
    		Student student = StudentUtilities.getStudent(new Scanner(System.in));
    		student_list.add(student);
    	}
    	
    	for(int i=0;i<10;i++) {
    		System.out.println(student_list.get(i));
    	}
    	*/
    	
    	//TESTING readStudent 
    	//Student student = StudentUtilities.readStudent("923451|Brown|Tasmin|1995-03-01|4,5");
    	//System.out.println(student);
    	
    	//TESTING majorsMenu
    	/*
    	Student test = new Student(123456,"k","sahil",now, majors);
    	String result = test.majorsMenu();
    	System.out.println(result);
    	*/
    	
    	//TESTING readStudents
    	/*
    	ArrayList <Student> test = new ArrayList();
    	try {
			test = StudentUtilities.readStudents(new Scanner(new File("students.txt")));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	
    	//for(int i=0;i<test.size();i++) {
    	//	System.out.println(test.get(i));
    	}
    	
    	//TESTING writeStudents
    	PrintStream ps;
		try {
			ps = new PrintStream("test.txt");
			StudentUtilities.writeStudents(test, ps);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	//StudentUtilities.writeStudents(test, ps);
		*/
    	
    	//TESTING majorCounts
    	/*
    	int[] count = StudentUtilities.majorCounts(null);
		for(int i=0;i<count.length;i++) {
	    	System.out.println(count[i]);
	    }
	    */
    	
    	//TESTING getByBirthDate 
    	/*
    	ArrayList <Student> test = new ArrayList();
    	ArrayList <Student> result = new ArrayList();
    	try {
			test = StudentUtilities.readStudents(new Scanner(new File("students.txt")));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	result = StudentUtilities.getByYear(test, 1999);
    	
    	for(int i=0;i<result.size();i++) {
    		System.out.println(result.get(i));
    	}
    	*/
   }	
}