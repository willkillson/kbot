package com.company;

import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;
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

    public Set<IntPair> visitedPositions = new HashSet<IntPair>(){
        @Override
        public boolean contains(Object o) {

            boolean isContained = false;
            for(IntPair ip: this){
                if(ip.x==((IntPair) o).x&&ip.y==((IntPair) o).y){
                    isContained=true;
                }
            }

            return isContained;
        }
    };

    public int totalPositions;

    public CrypterCar(boolean isRotateRight, int xbound, int ybound){
        totalPositions = xbound*ybound;
        if(isRotateRight){
            dir = Direction.s;
        }
        else{
            dir = Direction.w;
        }
        this.xBound = xbound;
        this.yBound = ybound;

        xPos = xBound-1;//set top right
        yPos = 0;
        IntPair posPair = new IntPair(xPos, yPos);
        visitedPositions.add(posPair);
    }
    public IntPair moveRotateRight(){

        IntPair testPos = new IntPair(-1,-1);
        int maxIt = 1;
        for(int i = 0;i<maxIt;i++) {
            if (isBlocked == false) {
                switch (dir) {
                    case s:
                        testPos.x = this.xPos;
                        testPos.y = this.yPos + 1;
                        if (((yPos + 1) == yBound) || (visitedPositions.contains(testPos))) {
                            isBlocked = true;
                            maxIt=3;
                        } else {
                            yPos++;
                            visitedPositions.add(testPos);
                        }
                        break;
                    case e:
                        testPos.x = this.xPos + 1;
                        testPos.y = this.yPos;
                        if (((xPos + 1) == xBound) || (visitedPositions.contains(testPos))) {
                            isBlocked = true;
                            maxIt=3;
                        } else {
                            xPos++;
                            visitedPositions.add(testPos);
                        }
                        break;
                    case n:
                        testPos.x = this.xPos;
                        testPos.y = this.yPos - 1;
                        if (((yPos - 1) == -1) || (visitedPositions.contains(testPos))) {
                            isBlocked = true;
                            maxIt=3;
                        } else {
                            yPos--;
                            visitedPositions.add(testPos);
                        }
                        break;
                    case w:
                        testPos.x = this.xPos - 1;
                        testPos.y = this.yPos;
                        if (((xPos - 1) == -1) || (visitedPositions.contains(testPos))) {
                            isBlocked = true;
                            maxIt=3;
                        } else {
                            xPos--;
                            visitedPositions.add(testPos);
                        }
                        break;
                }
            } else {
                   switch (dir) {
                    case s:
                        dir = Direction.w;
                        break;
                    case e:
                        dir = Direction.s;
                        break;
                    case n:
                        dir = Direction.e;
                        break;
                    case w:
                        dir = Direction.n;
                        break;
                }
                this.isBlocked = false;
            }
        }

        return testPos;
    }
    public IntPair moveRotateLeft(){

        IntPair testPos = new IntPair(-1,-1);
        int maxIt = 1;
        for(int i = 0;i<maxIt;i++) {
            if (isBlocked == false) {
                switch (dir) {
                    case s:
                        testPos.x = this.xPos;
                        testPos.y = this.yPos + 1;
                        if (((yPos + 1) == yBound) || (visitedPositions.contains(testPos))) {
                            isBlocked = true;
                            maxIt=3;
                        } else {
                            yPos++;
                            visitedPositions.add(testPos);
                        }
                        break;
                    case e:
                        testPos.x = this.xPos + 1;
                        testPos.y = this.yPos;
                        if (((xPos + 1) == xBound) || (visitedPositions.contains(testPos))) {
                            isBlocked = true;
                            maxIt=3;
                        } else {
                            xPos++;
                            visitedPositions.add(testPos);
                        }
                        break;
                    case n:
                        testPos.x = this.xPos;
                        testPos.y = this.yPos - 1;
                        if (((yPos - 1) == -1) || (visitedPositions.contains(testPos))) {
                            isBlocked = true;
                            maxIt=3;
                        } else {
                            yPos--;
                            visitedPositions.add(testPos);
                        }
                        break;
                    case w:
                        testPos.x = this.xPos - 1;
                        testPos.y = this.yPos;
                        if (((xPos - 1) == -1) || (visitedPositions.contains(testPos))) {
                            isBlocked = true;
                            maxIt=3;
                        } else {
                            xPos--;
                            visitedPositions.add(testPos);
                        }
                        break;
                }
            } else {
                switch (dir) {
                    case s:
                        dir = Direction.e;
                        break;
                    case e:
                        dir = Direction.n;
                        break;
                    case n:
                        dir = Direction.w;
                        break;
                    case w:
                        dir = Direction.s;
                        break;
                }
                this.isBlocked = false;
            }
        }

        return testPos;
    }

}
