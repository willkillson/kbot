

import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;

import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferInt;


public class Engine extends Canvas implements Runnable{

    public int width;
    public int height;
    public int scale = 1;

    private Thread thread;
    public JFrame frame;
    private boolean running = false;


    //Game Time
    private final double updateRate = 1.0d/60.0d;
    private long nextStateTime;
    private int fps;
    private int ups;

    private BufferedImage image;
    private int[] pixels;

    private Robot robot;
    private Rectangle rect;


    public static void main(String[] args) throws AWTException {
        new Engine();
    }

    public Engine() throws AWTException {

        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        Mat mat = Mat.eye(3, 3, CvType.CV_8UC1);
        System.out.println("mat = " + mat.dump());


        this.width = 2560;
        this.height = 1440;

        this.image = new BufferedImage(this.width,this.height,BufferedImage.TYPE_INT_RGB);
        this.pixels =  ((DataBufferInt)image.getRaster().getDataBuffer()).getData();

        this.robot = new Robot();
        this.rect = new Rectangle(0,0,this.width,this.height);

        Dimension size = new Dimension(width*scale,height*scale);
        setPreferredSize(size);

        frame = new JFrame();

        frame.setResizable(true);
        frame.setTitle("TestBench");

        JPanel p = new JPanel();
        p.setLayout(new BorderLayout());
        p.add(this,BorderLayout.CENTER);

        //// Console
        JTextArea ta = new JTextArea(10,5);

        p.add(new JScrollPane(ta),BorderLayout.SOUTH);
        frame.add(p);

        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        start();


    }

    public synchronized void start(){

        thread = new Thread(this, "Display");
        thread.start();
    }

    public synchronized void stop(){
        running = false;
        try{
            thread.join();
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }

    @Override
    public void run() {



        running = true;
        double accumulator = 0;

        long currentTime = System.currentTimeMillis();
        long lastUpdate = currentTime;

        // Main game loop
        while(running){
            currentTime = System.currentTimeMillis();
            double lastRenderTimeInSeconds = (currentTime - lastUpdate)/ 1000d;
            accumulator += lastRenderTimeInSeconds;
            lastUpdate = currentTime;

            if(accumulator >= updateRate){
                while(accumulator>updateRate){
                    accumulator-=updateRate;
                    ups++;
                }
                render();
                printStats();
            }


        }
    }

    private void printStats(){
        if(System.currentTimeMillis()>nextStateTime){
            System.out.println(String.format("FPS: %d, UPS: %d", fps, ups));
            fps = 0;
            ups = 0;
            nextStateTime = System.currentTimeMillis() + 1000;
        }
    }

    public void render(){
        fps++;
        BufferStrategy bs = getBufferStrategy();
        if(bs==null){
            createBufferStrategy(3);//triple buffering
            return;
        }
//        // Copy all our screen pixels into our pixels buffer
//        for(int i = 0;i<pixels.length;i++){
//            pixels[i] = screen.pixels[i];
//        }

        BufferedImage bi = robot.createScreenCapture(rect);
//        ImageIO.write(bi,"bmp",new File("ss.bmp"));

        Graphics g = bs.getDrawGraphics();
        g.drawImage(bi, 0,0,getWidth(),getHeight(), null);
        g.dispose();
        bs.show();
    }
}