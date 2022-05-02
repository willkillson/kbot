package org.kbot;


import org.opencv.core.*;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;


public class VisionManager {

    public Map<String, Vision> hayStacks;
    public Map<String, Vision> needles;

    public VisionManager(){
        this.hayStacks = new HashMap<>();
        this.hayStacks.put("default", new Vision("./images/haystack/haystack_a5_town_nearstash.png"));

        this.needles = new HashMap<>();
        this.needles.put("default", new Vision("./images/needle/a5/a5_wp.jpg"));
        this.needles.put("a5_stash", new Vision("./images/needle/a5/a5_stash.jpg"));
    }

    public Mat find(final String visionName) {

        //https://docs.opencv.org/3.4/de/da9/tutorial_template_matching.html

        Vision haystack = this.hayStacks.get(visionName);
        Vision needle = this.needles.get(visionName);
        Mat img_display = new Mat();
        haystack.image_frame.copyTo(img_display);
        Mat result = new Mat();
        int result_cols = haystack.image_frame.cols() - needle.image_frame.cols() + 1;
        int result_rows = haystack.image_frame.rows() - needle.image_frame.rows() + 1;
        result.create(result_rows, result_cols, CvType.CV_32FC1);

        Imgproc.matchTemplate(haystack.image_frame,needle.image_frame,result,haystack.method);
        Core.normalize(result, result, 0, 1, Core.NORM_MINMAX, -1, new Mat());
        Point matchLoc;
        Core.MinMaxLocResult mmr = Core.minMaxLoc(result);
        matchLoc = mmr.maxLoc;

        Imgproc.rectangle(img_display, matchLoc, new Point(matchLoc.x + needle.image_frame.cols(), matchLoc.y + needle.image_frame.rows()),
                new Scalar(0, 0, 0), 2, 8, 0);
        Imgproc.rectangle(result, matchLoc, new Point(matchLoc.x + needle.image_frame.cols(), matchLoc.y + needle.image_frame.rows()),
                new Scalar(0, 0, 0), 2, 8, 0);


        return img_display;
    }

    public Mat find(final Mat mat,final String pNeedle) {

        //https://docs.opencv.org/3.4/de/da9/tutorial_template_matching.html

        this.hayStacks.put("default",new Vision(mat));

        Vision haystack = this.hayStacks.get("default");
        Vision needle = this.needles.get(pNeedle);
        Mat img_display = new Mat();
        haystack.image_frame.copyTo(img_display);
        Mat result = new Mat();
        int result_cols = haystack.image_frame.cols() - needle.image_frame.cols() + 1;
        int result_rows = haystack.image_frame.rows() - needle.image_frame.rows() + 1;
        result.create(result_rows, result_cols, CvType.CV_32FC1);

        Imgproc.matchTemplate(haystack.image_frame,needle.image_frame,result,haystack.method);
        Core.normalize(result, result, 0, 1, Core.NORM_MINMAX, -1, new Mat());
        Point matchLoc;
        Core.MinMaxLocResult mmr = Core.minMaxLoc(result);
        matchLoc = mmr.maxLoc;

        Imgproc.rectangle(img_display, matchLoc, new Point(matchLoc.x + needle.image_frame.cols(), matchLoc.y + needle.image_frame.rows()),
                new Scalar(0, 0, 0), 2, 8, 0);
        Imgproc.rectangle(result, matchLoc, new Point(matchLoc.x + needle.image_frame.cols(), matchLoc.y + needle.image_frame.rows()),
                new Scalar(0, 0, 0), 2, 8, 0);


        return img_display;
    }


    public Mat getHaystackVision(final String visionName){
        return this.hayStacks.get(visionName).image_frame;
    }

    //https://stackoverflow.com/questions/14958643/converting-bufferedimage-to-mat-in-opencv
    public static Mat bufferedImageToMat(BufferedImage image) {

        try{
            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
            ImageIO.write(image, "jpg", byteArrayOutputStream);
            byteArrayOutputStream.flush();
            return Imgcodecs.imdecode(new MatOfByte(byteArrayOutputStream.toByteArray()), Imgcodecs.IMREAD_UNCHANGED);
        } catch (Exception e){
            e.printStackTrace();
            return null;
        }

    }

    public static BufferedImage Mat2BufferedImage(Mat mat) {
        try{
            //Encoding the image
            MatOfByte matOfByte = new MatOfByte();
            Imgcodecs.imencode(".jpg", mat, matOfByte);
            //Storing the encoded Mat in a byte array
            byte[] byteArray = matOfByte.toArray();
            //Preparing the Buffered Image
            InputStream in = new ByteArrayInputStream(byteArray);
            BufferedImage bufImage = ImageIO.read(in);
            return bufImage;
        }catch(Exception e){
            System.out.println(e);
            return null;
        }

    }
}
