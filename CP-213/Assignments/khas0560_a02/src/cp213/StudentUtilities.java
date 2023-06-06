package cp213;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

/**
 * Utilities for working with Student objects.
 *
 * @author Sahil Khasnobish, 190990560, khas0560@mylaurier.ca
 * @version 2021-06-14
 */
public class StudentUtilities {

    /**
     * Creates a list of Students whose birthDates are equal to or later than
     * birthDate.
     *
     * @param students  list of students
     * @param birthDate to compare against
     * @return list of students for birthDate
     */
    public static ArrayList<Student> getByBirthDate(final ArrayList<Student> students, final LocalDate birthDate) {
	final ArrayList<Student> bStudents = new ArrayList<>();

	    for(int i=0;i<students.size();i++) {
	    	
	    	if((students.get(i).getBirthDate().getYear() >= birthDate.getYear()) && (students.get(i).getBirthDate().getMonthValue() >= birthDate.getMonthValue()) && (students.get(i).getBirthDate().getDayOfMonth() >= birthDate.getDayOfMonth())) {
	    		bStudents.add(students.get(i));
	    	}
	    }

	return bStudents;
    }

    /**
     * Creates a list of Students whose list of majors include major.
     *
     * @param students list of students
     * @param major    major to compare against
     * @return list of students for major
     */
    public static ArrayList<Student> getByMajor(final ArrayList<Student> students, final int major) {
	final ArrayList<Student> mStudents = new ArrayList<>();
		
		
		for(int i=0;i<students.size();i++) {
			Integer[] list = students.get(i).getMajors();
			for(int n=0;n<list.length;n++) {
				if(list[n] == major) {
					mStudents.add(students.get(n));
				}
			}
		}

	return mStudents;
    }

    /**
     * Creates a list of Students whose list of majors include all the major codes
     * in majors.
     *
     * @param students list of students
     * @param majors   majors list to compare against
     * @return list of students for majors
     */
    public static ArrayList<Student> getByMajors(final ArrayList<Student> students, final Integer[] majors) {
	final ArrayList<Student> gStudents = new ArrayList<>();
	
	int temp = 0;
	for(int i=0;i<students.size();i++) {
		
		if(majors.length==students.size()) {
			Integer[] list = students.get(i).getMajors();
			for(int n=0;n<majors.length;n++) {
				if(majors[n] != list[n]) {
					temp=-1;
				}
			}if(temp != -1) {
				gStudents.add(students.get(i));
			}
		}
	}

	return gStudents;
    }

    /**
     * Creates a list of Students from a particular birth year.
     *
     * @param students list of students
     * @param year birth date year of students
     * @return list of students for birthDate
     */
    public static ArrayList<Student> getByYear(final ArrayList<Student> students, final int year) {
	final ArrayList<Student> yStudents = new ArrayList<>();

	for(int i=0;i<students.size();i++) {
    	
    	if((students.get(i).getBirthDate().getYear() == year)) {
    		yStudents.add(students.get(i));
    	}
    }

	return yStudents;
    }

    /**
     * Creates a Student object by requesting data from a user.
     *
     * @param keyboard a keyboard Scanner
     * @return a Student object
     */
    public static Student getStudent(final Scanner keyboard) {

    	final ArrayList<Integer> majorsList = new ArrayList<>();
    	
    	System.out.println("Enter student ID: ");
    	int id = keyboard.nextInt();
    	
    	System.out.println("Surname: ");
    	String surname = keyboard.next();
    	
    	System.out.println("Forename: ");
    	String forename = keyboard.next();
    	
    	System.out.println("BirthDate: ");
    	int year = keyboard.nextInt();
    	int month = keyboard.nextInt();
    	int day = keyboard.nextInt();
    	LocalDate of  = LocalDate.of(year, month, day);
    	
    	System.out.println("Majors: ");
    	
    	Integer[] array = readMajors(keyboard);
    	
    	Student student = new Student(id,surname,forename,of,array);
    	return student;
    }

    /**
     * Counts the number of students in each major given in Student.GENRES.
     *
     * @param students list of students
     * @return Number of majors across all Students.
     */
    public static int[] majorCounts(final ArrayList<Student> students) { 
    	int length = Student.MAJORS.length;
    	int[] array = new int[length];
    	
	    for(int i=0;i<length;i++) {
	    	array[i] = 0;
	    }
	    
	    for(int n=0;n<length;n++) {
	    	for(int j=0;j<students.get(n).getMajors().length;j++) {
	    		if(students.get(n).getMajors()[j] == n) {
	    			array[n]+=1;
	    		}
	    	}
	    }
	   
	    
	    return array;
    }

    /**
     * Asks a user to select majors from a list of majors and returns an integer
     * list of the majors chosen.
     *
     * @param keyboard Keyboard input.
     * @return An integer list of major codes.
     */
    public static Integer[] readMajors(final Scanner keyboard) {
	
    	final ArrayList<Integer> majors = new ArrayList<>();

		int student_major = 0;
		while(!keyboard.next().equals("q")) {
			System.out.println("Enter a major number ('q' to quit): ");
			if(!keyboard.hasNextInt()) {
				System.out.println("Not a number");
			}else {
				
				student_major = keyboard.nextInt();
				
	    		if(student_major>11) {
	    			System.out.println("Major code must be less than 11");
	    		}else if(student_major<0) {
	    			System.out.println("Major code must be 0 or greater");
	    		}else {
	    			majors.add(student_major);
	    		}
			}
	}

	return majors.toArray(new Integer[majors.size()]);
    }

    /**
     * Creates and returns a Student object from a line of formatted string data.
     *
     * @param line a vertical bar-delimited line of student data in the format
     *             id|surname|forename|birthDate|majorCodes
     * @return the data from line as a Student object
     */
    public static Student readStudent(final String line) {
    	
    	String[] student_values = line.split("[|]");
    
    	int id = Integer.parseInt(student_values[0]);
    	String surname = student_values[1];
    	String forename = student_values[2];
    	
    	String[] birth_date_str = student_values[3].split("-");
    	int year = Integer.parseInt(birth_date_str[0]);
    	int month = Integer.parseInt(birth_date_str[1]);
    	int day = Integer.parseInt(birth_date_str[2]);
    	LocalDate of  = LocalDate.of(year, month, day);
    	
    	String[] major_codes_str = student_values[4].split(",");
    	int length = major_codes_str.length;
    	final ArrayList<Integer> majors = new ArrayList<>();
    	for(int i=0;i<length;i++) {
    		majors.add(Integer.parseInt(major_codes_str[i]));
    	}
    	Integer[] majors_list = majors.toArray(new Integer[majors.size()]);
    	Student student = new Student(id,surname,forename,of,majors_list);
    	
    	return student;

    }

    /**
     * Reads a list of Students from a file.
     *
     * @param fileScanner The file to read.
     * @return A list of Student objects.
     * @throws FileNotFoundException file not found
     */
    public static ArrayList<Student> readStudents(final Scanner fileScanner) throws FileNotFoundException {
	final ArrayList<Student> students = new ArrayList<>();

	    while(fileScanner.hasNextLine()) {
	    	students.add(readStudent(fileScanner.nextLine()));
	    }

	return students;
    }

    /**
     * Writes the contents of students to a file. Overwrites or creates a new file of
     * Student objects converted to strings.
     *
     * @param students List of Students.
     * @param ps       PrintStream to write Student data to.
     */
    public static void writeStudents(final ArrayList<Student> students, PrintStream ps) {
    	
    	int length = students.size();
	    for(int i=0;i<length;i++) {
	    	ps.println(students.get(i).toString());
	    }
	    	

    }

}
