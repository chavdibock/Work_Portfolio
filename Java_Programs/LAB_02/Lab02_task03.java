/*
 * File: Lab02_task03.java

 * Author: NIkola Georgiev

 * Date: 13.11.2023

 */

public class Student {
    private String name;
    private int idNumber;
    private double semesterFee;
    private int semestersLeft;

    // Constructor with values initialized using setters
    public Student() {
        setName("John Doe");
        setIdNumber(201165003);
        setSemesterFee(10000);
        setSemestersLeft(3);
    }

    // Accessor method for name
    public String getName() {
        return name;
    }

    // Mutator method for name
    public void setName(String name) {
        this.name = name;
    }

    // Accessor method for idNumber
    public int getIdNumber() {
        return idNumber;
    }

    // Mutator method for idNumber
    public void setIdNumber(int idNumber) {
        this.idNumber = idNumber;
    }

    // Accessor method for semesterFee
    public double getSemesterFee() {
        return semesterFee;
    }

    // Mutator method for semesterFee
    public void setSemesterFee(double semesterFee) {
        this.semesterFee = semesterFee;
    }

    // Accessor method for semestersLeft
    public int getSemestersLeft() {
        return semestersLeft;
    }

    // Mutator method for semestersLeft
    public void setSemestersLeft(int semestersLeft) {
        this.semestersLeft = semestersLeft;
    }

    public static void main(String[] args) {
        // Create an instance of the Student class
        Student myStudent = new Student();

        // Display information about the student
        System.out.println("Student Information:");
        System.out.println("Name: " + myStudent.getName());
        System.out.println("ID Number: " + myStudent.getIdNumber());
        System.out.println("Semester Fee: $" + myStudent.getSemesterFee());
        System.out.println("Semesters Left: " + myStudent.getSemestersLeft());
    }
}
