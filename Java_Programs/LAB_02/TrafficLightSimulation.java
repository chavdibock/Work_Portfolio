
import java.awt.Color;

import java.awt.Graphics;

import javax.swing.JFrame;

import javax.swing.JPanel;

import javax.swing.Timer;

import java.awt.event.ActionEvent;

import java.awt.event.ActionListener;

/*
 * File: ShapeDrawingExample.java

 * Author: NIkola Georgiev

 * Date: 13.11.2023

 */
public class TrafficLightSimulation extends JFrame {

    private static final long serialVersionUID = 1L;

    class TrafficLightPanel extends JPanel {

        private Color currentColor;

        public TrafficLightPanel() {

            currentColor = Color.yellow; // Initial color is red

        }

        // Method to change the traffic light color
        public void changeLight() {
            /*
            if (currentColor.equals(Color.RED)) {

                currentColor = Color.YELLOW;

            } else if (currentColor.equals(Color.YELLOW)) {

                currentColor = Color.GREEN;

            } else {

                currentColor = Color.RED;

            }

        }
            
             */

            if (currentColor.equals(Color.YELLOW)) {

                currentColor = Color.RED;
            }else if (currentColor.equals(Color.RED)){
                currentColor = Color.GREEN;
            } else if (currentColor.equals(Color.GREEN)){
                currentColor = Color.YELLOW;
            }

        }

        // Override the paintComponent method for custom drawing
        @Override

        protected void paintComponent(Graphics g
        ) {

            super.paintComponent(g);

            // Draw the traffic light background
            g.setColor(Color.BLACK);

            g.fillRect(50, 50, 100, 300);

            // Draw the traffic light circles with the current color
            g.setColor(currentColor);
            g.fillOval(75, 75, 50, 50); // Red light

            changeLight();
            g.setColor(currentColor);

            g.fillOval(75, 175, 50, 50); // Yellow light

            changeLight();
            g.setColor(currentColor);

            g.fillOval(75, 275, 50, 50); // Green light
            changeLight();
        }

    }

    public TrafficLightSimulation() {

        setTitle("Traffic Light Simulation");

        setSize(200, 400);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create a TrafficLightPanel and add it to the JFrame
        TrafficLightPanel lightPanel = new TrafficLightPanel();

        add(lightPanel);

        // Create a timer to change the traffic light color every 2000 milliseconds (2 seconds)
        Timer timer = new Timer(2000, new ActionListener() {

            public void actionPerformed(ActionEvent e) {

                lightPanel.changeLight(); // Change the traffic light color

                lightPanel.repaint(); // Repaint the panel to reflect the changes

            }

        });

        timer.start(); // Start the timer

    }

    // Main method to launch the application
    public static void main(String[] args) {

        // Use SwingUtilities.invokeLater to ensure GUI updates are done on the event dispatch thread
        javax.swing.SwingUtilities.invokeLater(new Runnable() {

            public void run() {

                new TrafficLightSimulation().setVisible(true); // Make the window visible

            }

        });

    }
}
