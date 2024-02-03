

/**

 * File: ExceptionDemo.java

 * Author: Nikola Georgiev
 * Date: 12/07/2023

 */

import javax.swing.*;

public class ExceptionDemo {

    public static void main(String[] args) {

        // Declare three integers and a String for user input
        int numerator = 0, denominator = 0, result;
        String inputString;

        try {
            // Prompt the user for two values, convert to integers, and perform division
            inputString = JOptionPane.showInputDialog(null, "Enter a number to be divided");
            numerator = Integer.parseInt(inputString);

            inputString = JOptionPane.showInputDialog(null, "Enter a number to divide into the first number");
            denominator = Integer.parseInt(inputString);

            // Division
            result = numerator / denominator;
        } catch (ArithmeticException exception) {
            // Catch division by 0 exception
            JOptionPane.showMessageDialog(null, "Error: " + exception.getMessage());
            result = 0;
        } finally {
            // Display the result (which might have been set to 0)
            JOptionPane.showMessageDialog(null, numerator + " / " + denominator + "\nResult is " + result);
        }
    }
}

