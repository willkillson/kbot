package com.company;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Cipher {

    public String plainText;
    public int demX;
    public int demY;
    public char[][] cipherArray;
    public boolean isRotateRight = false;


    public String cipherText = "";



    public Cipher(String input){

        Pattern pattern = Pattern.compile("\"(.*)\" [(](\\d+), ?(\\d+)[)] ?(.*)");
        Matcher matcher = pattern.matcher(input);
        matcher.find();

        this.plainText = matcher.group(1);
        this.demX = Integer.parseInt(matcher.group(2));
        this.demY = Integer.parseInt(matcher.group(3));
        String rotation = matcher.group(4);

        if(rotation.equals("clockwise")){
            this.isRotateRight = true;
        }
        else{
            this.isRotateRight = false;
        }
    }

    public void init(){
        plainText = plainText.replaceAll("\\s*+", "");
        plainText = plainText.replaceAll("\"*+", "");
        plainText = plainText.replaceAll("[.]*+", "");
        plainText = plainText.replaceAll("[?]*+", "");
        plainText = plainText.replaceAll("[!]*+", "");
        plainText = plainText.replaceAll("[']*+", "");
        plainText = plainText.replaceAll("[-]*+", "");
        plainText = plainText.replaceAll("[/]*+", "");

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

    public void encryptString(){

        CrypterCar car = new CrypterCar(isRotateRight,demX,demY);
        int index = 0;
        IntPair pair = new IntPair(-1,-1);
        cipherText+= cipherArray[0][demX-1];
        while(index<demX*demY-1){
            if(isRotateRight) {
                pair = car.moveRotateRight();
            }
            else{
                pair = car.moveRotateLeft();
            }
            cipherText+= cipherArray[pair.y][pair.x];
            index++;
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
