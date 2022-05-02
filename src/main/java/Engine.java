

import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;
import org.kbot.VisionManager;
import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;

import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferInt;
import java.io.File;


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

    private VisionManager visionManager;


    public static void main(String[] args) throws AWTException, TesseractException {
        new Engine();
    }

    public Engine() throws AWTException, TesseractException {
        //TODO:
        // playing with tesseract
//        File title = new File("./images/title.png");
//        File white_item = new File("./images/white_item.png");
//        File gray_item = new File("./images/gray_item.png");
//        File blue_item = new File("./images/blue_item.png");

//        Tesseract tesseract = new Tesseract();
//        tesseract.setDatapath("src/main/resources/tessdata_fast");
//        tesseract.setLanguage("eng");
//        tesseract.setPageSegMode(1);
//        tesseract.setOcrEngineMode(1);
//
//        System.out.println( "title: " + tesseract.doOCR(title));
//        System.out.println( "white_item: " + tesseract.doOCR(white_item));
//        System.out.println( "gray_item: " +tesseract.doOCR(gray_item));
//        System.out.println( "blue_item: " +tesseract.doOCR(blue_item));

        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);

        this.visionManager = new VisionManager();


        this.width = 1278;
        this.height = 666;

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

        Mat mat2 = VisionManager.bufferedImageToMat(bi);
        Mat mat = this.visionManager.find(mat2,"a5_stash");
        bi = VisionManager.Mat2BufferedImage(mat);


//        ImageIO.write(bi,"bmp",new File("ss.bmp"));

        Graphics g = bs.getDrawGraphics();
        g.drawImage(bi, 0,0,getWidth(),getHeight(), null);
        g.dispose();
        bs.show();
    }
}