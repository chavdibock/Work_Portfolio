/*
 * File: Lab02_task04.java

 * Author: NIkola Georgiev

 * Date: 13.11.2023

 */

public class Employee {
    private String name;
    private String department;
    private String position;
    private String emailAddress;
    private String phone;
    private double salary;

    // Constructor with 6 parameters to initialize data members using setters
    public Employee(
            String name,
            String department,
            String position,
            String emailAddress,
            String phone,
            double salary
    ) {
        setName(name);
        setDepartment(department);
        setPosition(position);
        setEmailAddress(emailAddress);
        setPhone(phone);
        setSalary(salary);
    }

    // Accessor method for name
    public String getName() {
        return name;
    }

    // Mutator method for name
    public void setName(String name) {
        this.name = name;
    }

    // Accessor method for department
    public String getDepartment() {
        return department;
    }

    // Mutator method for department
    public void setDepartment(String department) {
        this.department = department;
    }

    // Accessor method for position
    public String getPosition() {
        return position;
    }

    // Mutator method for position
    public void setPosition(String position) {
        this.position = position;
    }

    // Accessor method for emailAddress
    public String getEmailAddress() {
        return emailAddress;
    }

    // Mutator method for emailAddress
    public void setEmailAddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }

    // Accessor method for phone
    public String getPhone() {
        return phone;
    }

    // Mutator method for phone
    public void setPhone(String phone) {
        this.phone = phone;
    }

    // Accessor method for salary
    public double getSalary() {
        return salary;
    }

    // Mutator method for salary
    public void setSalary(double salary) {
        this.salary = salary;
    }

    public static void main(String[] args) {
        // Create an instance of the Employee class with values in the constructor
        Employee myEmployee = new Employee(
                "John Doe",
                "IT",
                "Software Engineer",
                "john.doe@example.com",
                "123-456-7890",
                75000.0
        );

        // Display information about the employee
        System.out.println("Employee Information:");
        System.out.println("Name: " + myEmployee.getName());
        System.out.println("Department: " + myEmployee.getDepartment());
        System.out.println("Position: " + myEmployee.getPosition());
        System.out.println("Email Address: " + myEmployee.getEmailAddress());
        System.out.println("Phone: " + myEmployee.getPhone());
        System.out.println("Salary: $" + myEmployee.getSalary());
    }
}
