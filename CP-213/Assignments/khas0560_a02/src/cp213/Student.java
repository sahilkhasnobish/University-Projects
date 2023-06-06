package cp213;

import java.io.PrintStream;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Student class definition.
 *
 * @author Sahil Khasnobish, 190990560, khas0560@mylaurier.ca
 * @version 2021-06-14
 */
public class Student implements Comparable<Student> {

    // Constants
    /**
     * List of string descriptions of student majors.
     */
    public static final String[] MAJORS = { "Computer Science", "Psychology", "Chemistry", "Math", "Business", "Music",
	    "English", "Basket Weaving", "Women's Studies", "History", "Archaeology" };

    /**
     * Returns a string of all majors in the Student.MAJORS list. Use for input
     * menus. Formatted as " 3: Math"
     *
     * @return the majors.
     */
    public static String majorsMenu() {
    	StringBuilder new_str = new StringBuilder();
    	for(int i=0;i<Student.MAJORS.length;i++) {
    		new_str.append(String.format("%3d", i) + ":" + " " + Student.MAJORS[i] + "\n");
    	}
    	
    	String result = new_str.toString();
	    return result;
    }

    /**
     * Converts a string of the form "2,3,6" to an array of Integer objects, [2, 3,
     * 6]. Used when reading Student objects from a file.
     *
     * @param string The string to convert to an array.
     * @return The array version of string.
     */
    public static Integer[] majorsStringToList(final String string) {
    	
    	final ArrayList<Integer> majorsList = new ArrayList<>();
    	int num = 0;
    	String[] list = string.split(",");
    	for(int i=0;i<list.length;i++) {
    		num =  Integer. parseInt((list[i])) ;
    		majorsList.add(num);
    	}

	// Convert arraylist to an array of Integer.
    	return majorsList.toArray(new Integer[majorsList.size()]);
    	
    }

    // Attributes
    private LocalDate birthDate = null;
    private String forename = "";
    private int id = 0;
    private Integer[] majors = null;
    private String surname = "";

    /**
     * Instantiates a Student object.
     *
     * @param id        student ID number
     * @param surname   student surname
     * @param forename  name of forename
     * @param birthDate birthDate in 'YYYY-MM-DD' format
     * @param majors    integers representing student majors list
     */
    public Student(final int id, final String surname, final String forename, final LocalDate birthDate,
	    final Integer[] majors) {

	    this.id = id;
	    this.surname = surname;
	    this.forename = forename;
	    this.birthDate = birthDate;
	    this.majors = majors;
	    

    }

    /**
     * Converts a majors list of the form [2,3,7] to a string "2,3,7" for writing
     * Student data to a file.
     *
     * @return the majors list string
     */
    private String majorsListToString() {
    	String majors_str = "";
    	for(int i=0;i<majors.length;i++) {
    		majors_str+=majors[i];
    		majors_str+=",";
    	}
    	
    	return majors_str;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Comparable#compareTo(java.lang.Object)
     */
    @Override
    public int compareTo(final Student target) { 
    	int result = 0;
    	if(target.forename.compareTo(this.forename)<0) {
    		result = -1;
    	}else if(target.forename.compareTo(forename)>0) {
    		result = 1;
    	}else {
    		if(target.id>this.id) {
    			result = 1;
    		}else if(target.id<this.id) {
    			result = -1;
    		}else {
    			result = 0;
    		}
    	}
    	return result;
    }

    /**
     * birthDate getter.
     *
     * @return the birthDate
     */
    public LocalDate getBirthDate() {
	return this.birthDate;
    }

    /**
     * forename getter.
     *
     * @return the forename
     */
    public String getForename() {
	return this.forename;
    }

    /**
     * id getter
     *
     * @return the id
     */
    public int getId() {
	return id;
    }

    /**
     * majors getter.
     *
     * @return the majors list
     */
    public Integer[] getMajors() {
	return this.majors;
    }

    /**
     * surname getter.
     *
     * @return the surname
     */
    public String getSurname() {
	return this.surname;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#hashCode()
     */
    @Override
    public int hashCode() {
	return this.id;
    }

    /**
     * Creates a formatted string of Student key data in the format "surname,
     * forename, id". Ex: "Brown, David, 123456".
     *
     * @return a Student key as a string
     */
    public String key() {
	return String.format("%s, %s, %d", this.surname, this.forename, this.id);
    }

    /**
     * Converts a list of major integers to a string of major names.
     *
     * @return comma delimited string of major names based upon the current student
     *         object's integer majors list. e.g.: [0, 2] returns "science fiction,
     *         drama"
     */
    public String majorsListToNames() {
	    String names = "";
	    int length = this.majors.length;
	    for(int i=0;i<length;i++) {
	    	if(i<length-1) {
	    		names+=MAJORS[this.majors[i]];
		    	names+=", ";
	    	}else {
	    		names+=MAJORS[this.majors[i]];
	    	}
	    	
	    }
	    return names;
    }

    /**
     * forename setter
     *
     * @param forename the new forename
     */
    public void setForename(String forename) {
	this.forename = forename;
    }

    /**
     * majors setter.
     *
     * @param majors the new list of numeric majors
     */
    public void setMajors(final Integer[] majors) {
	this.majors = majors;
    }

    /**
     * surname setter.
     *
     * @param surname the new surname
     */
    public void setSurname(final String surname) {
	this.surname = surname;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#toString() Creates a formatted string of student data.
     */
    @Override
    public String toString() { 
    	
    	StringBuilder new_str = new StringBuilder();
    	
    	new_str.append("Name" + ":" + "      " + this.surname + ", " + this.forename + "\n");
    	new_str.append("ID" + ":" + "        " + this.id + "\n");
    	new_str.append("Birthdate" + ":" + " " + this.birthDate + "\n");
    	new_str.append("Majors:    " + this.majorsListToNames() + "\n");
    	
    	String result = new_str.toString();
	    return result; 

    }

    /**
     * Writes a single line of student data to an open file in the format
     * id|surname|forename|birthDate|majorCodes
     *
     * @param ps output PrintStream to print to
     */
    public void write(final PrintStream ps) { 
    	
    	ps.printf("%d|%s|%s|",this.id,this.surname,this.forename);
    	ps.println(this.birthDate);
    	ps.println("|");
    	

    }

}
