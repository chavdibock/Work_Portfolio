
import java.awt.Color;

import java.awt.Font;

import java.awt.Graphics;

import javax.swing.JFrame;

import javax.swing.JPanel;

/*
 * File: ColorDemo.java

 * Author: NIkola Georgiev

 * Date: 13.11.2023

 */
public class ColorDemo extends JFrame {



    private static final long serialVersionUID = 1L;

class ColorPanel extends JPanel {



    // Override the paintComponent method for custom drawing

    @Override

    protected void paintComponent(Graphics g) {

        super.paintComponent(g);



        // Set color to red

        g.setColor(Color.yellow);



        // Draw a rectangle in red color

        g.fillRect(50, 50, 100, 100);

        // Explanation: Set the color to red using g.setColor(Color.RED). Then, draw a filled rectangle

        // at coordinates (50, 50) with a width of 100 pixels and a height of 100 pixels using g.fillRect.

    }

}

    // Constructor to set up the JFrame

    public ColorDemo() {

        setTitle("Color Demo");

        setSize(400, 300);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);



        // Create a ColorPanel and add it to the JFrame

        ColorPanel colorPanel = new ColorPanel();

        add(colorPanel);

    }



    // Main method to launch the application

    public static void main(String[] args) {

        // Use SwingUtilities.invokeLater to ensure GUI updates are done on the event dispatch thread

        javax.swing.SwingUtilities.invokeLater(() -> {

            new ColorDemo().setVisible(true); // Make the window visible

        });

    }

}