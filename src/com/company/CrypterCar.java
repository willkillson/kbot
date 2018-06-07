package com.company;

import java.util.Set;

enum Direction{
    n,s,e,w;
}

public class CrypterCar {

    public Direction dir;
    public int xPos;
    public int yPos;
    public int xBound;
    public int yBound;
    public boolean isBlocked = false;
    public Set<IntPair> visitedPositions;

    public CrypterCar(String plainText, boolean isRotateRight, int xbound, int ybound){
        if(isRotateRight){
            dir = Direction.s;
        }
        else{
            dir = Direction.w;
        }
        this.xBound = xbound;
        this.yBound = ybound;

        xPos = xBound;//set top right
        yPos = 0;
        IntPair posPair = new IntPair(xPos, yPos);
        visitedPositions.add(posPair);
    }
    public void moveRotateRight(){


        if(isBlocked!=false) {
            IntPair testPos = new IntPair();
            switch (dir) {
                case s:
                    testPos.x = this.xPos;
                    testPos.y = this.yPos+1;
                    if(((yPos+1)==yBound)||(visitedPositions.contains(testPos))){
                        isBlocked=true;
                    }
                    else{
                        yPos++;
                        visitedPositions.add(testPos);
                    }
                    break;
                case e:
                    testPos.x = this.xPos+1;
                    testPos.y = this.yPos;
                    if(((xPos+1)==xBound)||(visitedPositions.contains(testPos))){
                        isBlocked=true;
                    }
                    else{
                        xPos++;
                        visitedPositions.add(testPos);
                    }
                    break;
                case n:
                    testPos.x = this.xPos;
                    testPos.y = this.yPos-1;
                    if(((yPos-1)==-1)||(visitedPositions.contains(testPos))){
                        isBlocked=true;
                    }
                    else{
                        yPos--;
                        visitedPositions.add(testPos);
                    }
                    break;
                case w:
                    testPos.x = this.xPos-1;
                    testPos.y = this.yPos;
                    if(((xPos-1)==-1)||(visitedPositions.contains(testPos))){
                        isBlocked=true;
                    }
                    else{
                        xPos--;
                        visitedPositions.add(testPos);
                    }
                    break;
            }
        }
        else{

            switch(dir){
                case s:
                    break;
                case e:
                    break;
                case n:
                    break;
                case w:
                    break;
            }

        }




    }

}
