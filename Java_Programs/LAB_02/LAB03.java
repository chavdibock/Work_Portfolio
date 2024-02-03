
import java.awt.Color;

import java.awt.Font;

import java.awt.Graphics;

import javax.swing.JFrame;

import javax.swing.JPanel;

/*
 * File: LAB03.java

 * Author: NIkola Georgiev

 * Date: 13.11.2023

 */

public class LAB03 extends JFrame {

    private static final long serialVersionUID = 1L;
    
class TextDrawingPanel extends JPanel{

    @Override
    protected void paintComponent(Graphics g) {

        super.paintComponent(g);
        g.setFont(new Font("Calibri", Font.PLAIN, 24));

        g.setColor(Color.BLUE);
        g.drawString("Nikola Georgiev", 100, 100);

    }

}

   public LAB03() {

        setTitle("Text Drawing Example");
        setSize(400, 300);
        
        // Create a JPanel for drawing text and add it to the JFrame
        TextDrawingPanel drawingPanel = new TextDrawingPanel();
        add(drawingPanel);

    }


    // Main method to launch the application

    public static void main(String[] args) {

        java.awt.EventQueue.invokeLater(() -> {

            new LAB03().setVisible(true);

        });

    }


}
