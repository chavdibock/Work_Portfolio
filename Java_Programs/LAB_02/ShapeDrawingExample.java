import java.awt.Color;

import java.awt.Graphics;

import java.awt.Graphics2D;

import java.awt.geom.Ellipse2D;

import javax.swing.JFrame;

import javax.swing.JPanel;

/*
 * File: ShapeDrawingExample.java

 * Author: NIkola Georgiev

 * Date: 13.11.2023

 */
 
 public class ShapeDrawingExample extends JFrame {



    private static final long serialVersionUID = 1L;

// Create a JPanel class for drawing shapes

class ShapeDrawingPanel extends JPanel {



    @Override

    protected void paintComponent(Graphics g) {

        super.paintComponent(g);



        Graphics2D g2d = (Graphics2D) g;



        // Draw a circle using Ellipse2D.Double

        g2d.setColor(Color.green);

        Ellipse2D.Double circle = new Ellipse2D.Double(100, 100, 100, 100);

        g2d.fill(circle);

        // Explanation: Ellipse2D.Double is used to represent a filled ellipse (or circle) with

        // double-precision coordinates. Here, a blue circle is drawn at (50, 50) with a width

        // and height of 100 pixels.



        // Draw an ellipse using Ellipse2D.Double

        g2d.setColor(Color.yellow);

        Ellipse2D.Double ellipse = new Ellipse2D.Double(100, 200, 150, 150);

        g2d.fill(ellipse);

        // Explanation: Ellipse2D.Double is used to represent a filled ellipse with double-precision

        // coordinates. Here, a red ellipse is drawn at (50, 200) with a width of 150 pixels and a

        // height of 100 pixels.

    }

}

    public ShapeDrawingExample() {

        setTitle("Shape Drawing Example");

        setSize(500, 500);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);



        ShapeDrawingPanel drawingPanel = new ShapeDrawingPanel();

        add(drawingPanel);

    }



    // Main method to launch the application

    public static void main(String[] args) {

        javax.swing.SwingUtilities.invokeLater(new Runnable() {

            public void run() {

                new ShapeDrawingExample().setVisible(true);

            }

        });

    }

}
