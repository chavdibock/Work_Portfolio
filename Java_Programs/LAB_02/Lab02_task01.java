/*
 * File: Lab02_task01.java

 * Author: NIkola Georgiev

 * Date: 13.11.2023

 */

public class Stock {
    private char symbol;
    private String name;
    private double previousPrice;
    private double currentPrice;

    // Constructor with setters
    public Stock(char symbol, String name, double previousPrice, double currentPrice) {
        setSymbol(symbol);
        setName(name);
        setPreviousPrice(previousPrice);
        setCurrentPrice(currentPrice);
    }

    // Default constructor
    public Stock() {
        // You can add default values or leave it empty
    }

    // Getter and Setter for symbol
    public char getSymbol() {
        return symbol;
    }

    public void setSymbol(char symbol) {
        this.symbol = symbol;
    }

    // Getter and Setter for name
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    // Getter and Setter for previousPrice
    public double getPreviousPrice() {
        return previousPrice;
    }

    public void setPreviousPrice(double previousPrice) {
        this.previousPrice = previousPrice;
    }

    // Getter and Setter for currentPrice
    public double getCurrentPrice() {
        return currentPrice;
    }

    public void setCurrentPrice(double currentPrice) {
        this.currentPrice = currentPrice;
    }

    // Public function to get the change percentage
    public double getChangePercent() {
        if (previousPrice == 0) {
            // Avoid division by zero if previous price is zero
            return 0.0;
        }

        // Calculate and return the percentage change
        return ((currentPrice - previousPrice) / previousPrice) * 100;
    }

    public static void main(String[] args) {
        // Create an instance of the Stock class using the constructor with setters
        Stock myStock = new Stock('A', "Example Stock", 50.0, 55.0);

        // Get and print the price change percentage
        double changePercent = myStock.getChangePercent();
        System.out.println("Price Change Percentage: " + changePercent + "%");

        // Update stock information using setters
        myStock.setSymbol('B');
        myStock.setName("Updated Stock");
        myStock.setPreviousPrice(55.0);
        myStock.setCurrentPrice(60.0);

        // Get and print the updated price change percentage
        changePercent = myStock.getChangePercent();
        System.out.println("Updated Price Change Percentage: " + changePercent + "%");
    }
}
