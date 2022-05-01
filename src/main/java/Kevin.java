import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class Kevin {

    public static void main(String[] args) throws AWTException, IOException {

        System.out.println("hello world!");
        // Create an instance of Robot class
        Robot robot = new Robot();
        Rectangle rect = new Rectangle(0,0,100,100);
        BufferedImage bi = robot.createScreenCapture(rect);
        ImageIO.write(bi,"bmp",new File("ss.bmp"));

    }
}
