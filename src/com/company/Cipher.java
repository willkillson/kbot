package com.company;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Cipher {

    public String plainText;
    public int demX;
    public int demY;
    public String rotation;


    public String cipherText;



    public Cipher(String input){

        Pattern pattern = Pattern.compile("\"(.*)\" [(](\\d), (\\d)[)] (.*)");
        Matcher matcher = pattern.matcher(input);
        matcher.find();

        this.plainText = matcher.group(1);
        this.demX = Integer.parseInt(matcher.group(2));
        this.demY = Integer.parseInt(matcher.group(3));
        this.rotation = matcher.group(4);
    }

    public void init(){
        plainText = plainText.replaceAll("\\s*+", "");
        plainText = plainText.replaceAll("\"*+", "");
        plainText = plainText.replaceAll("[.]*+", "");
        plainText = plainText.replaceAll("[?]*+", "");
        plainText = plainText.replaceAll("[!]*+", "");
    }




}
