/*
 * File: Lease.java

 * Author: NIkola Georgiev

 * Date: 13.11.2023

 */
public class Lease {
    private String tenantName;
    private int apartmentNumber;
    private double monthlyRent;
    private int leaseTermInMonths;

    // Constructor with parameters to initialize data members using setters
    public Lease(String tenantName, int apartmentNumber, double monthlyRent, int leaseTermInMonths) {
        setTenantName(tenantName);
        setApartmentNumber(apartmentNumber);
        setMonthlyRent(monthlyRent);
        setLeaseTermInMonths(leaseTermInMonths);
    }

    // Accessor method for tenantName
    public String getTenantName() {
        return tenantName;
    }

    // Mutator method for tenantName
    public void setTenantName(String tenantName) {
        this.tenantName = tenantName;
    }

    // Accessor method for apartmentNumber
    public int getApartmentNumber() {
        return apartmentNumber;
    }

    // Mutator method for apartmentNumber
    public void setApartmentNumber(int apartmentNumber) {
        this.apartmentNumber = apartmentNumber;
    }

    // Accessor method for monthlyRent
    public double getMonthlyRent() {
        return monthlyRent;
    }

    // Mutator method for monthlyRent
    public void setMonthlyRent(double monthlyRent) {
        this.monthlyRent = monthlyRent;
    }

    // Accessor method for leaseTermInMonths
    public int getLeaseTermInMonths() {
        return leaseTermInMonths;
    }

    // Mutator method for leaseTermInMonths
    public void setLeaseTermInMonths(int leaseTermInMonths) {
        this.leaseTermInMonths = leaseTermInMonths;
    }

    public static void main(String[] args) {
        // Create an instance of the Lease class with values in the constructor
        Lease myLease = new Lease("Your Name", 101, 1200, 6);

        // Display information about the lease
        System.out.println("Lease Information:");
        System.out.println("Tenant Name: " + myLease.getTenantName());
        System.out.println("Apartment Number: " + myLease.getApartmentNumber());
        System.out.println("Monthly Rent: $" + myLease.getMonthlyRent());
        System.out.println("Lease Term (months): " + myLease.getLeaseTermInMonths());
    }
}
