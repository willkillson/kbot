package com.company;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Cipher {

    public String plainText;
    public int demX;
    public int demY;
    public String rotation;
    public char[][] cipherArray;


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

        this.plainText = this.plainText.toUpperCase();
        this.cipherArray = new char[this.demY][this.demX];

        int index = 0;
        for(int i = 0;i< this.demY;i++){
            for(int j = 0;j<this.demX;j++, index++){
                this.cipherArray[i][j]= 'X';
                if(index<plainText.length()){
                    this.cipherArray[i][j]= plainText.charAt(index);
                }
            }
        }



    }


    public void print(){
        for(int i = 0;i< this.demY;i++){
            for(int j = 0;j<this.demX;j++){
                System.out.print(this.cipherArray[i][j]+" ");
            }
            System.out.print("\n");
        }

    }



}
