import com.company.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestCipher {

    @Test
    public void TestCipherConstructor(){
        Cipher testCipher = new Cipher("\"WE ARE DISCOVERED. FLEE AT ONCE\" (9, 3) clockwise");

        assertEquals("WE ARE DISCOVERED. FLEE AT ONCE",testCipher.plainText);
        assertEquals(9,testCipher.demX);
        assertEquals(3,testCipher.demY);
        assertEquals("clockwise",testCipher.rotation);
    }

    @Test
    public void TestPlainTextRemoveCharacters(){
        Cipher testCipher = new Cipher("\"WE ARE DISCOVERED. FLEE AT ONCE\" (9, 3) clockwise");
        testCipher.init();

        testCipher.print();
        assertEquals("WEAREDISCOVEREDFLEEATONCE",testCipher.plainText);

    }

    @Test
    public void TestCrypterCarSetContainsStepping(){
        CrypterCar car = new CrypterCar(true,2,2);
        IntPair testPair = new IntPair(1,0);//starting
        assertTrue(car.visitedPositions.contains(testPair));

        testPair.x = 1;
        testPair.y = 1;
        car.moveRotateRight();
        assertTrue(car.visitedPositions.contains(testPair));

        testPair.x = 0;
        testPair.y = 1;
        car.moveRotateRight();
        assertTrue(car.visitedPositions.contains(testPair));

        testPair.x = 0;
        testPair.y = 0;
        car.moveRotateRight();
        assertTrue(car.visitedPositions.contains(testPair));

        assertEquals(4,car.visitedPositions.size());


    }

    

    @Test
    public void TestCrypterCarExhaustive(){

        for(int i =2;i<=20;i++ ){
            for(int j = 2;j<=20;j++){

                CrypterCar car = new CrypterCar(true,j,i);


                int index = 0;
                while(index<(i*j)-1){
                    car.moveRotateRight();
                    index++;
                }
                assertEquals(i*j,car.visitedPositions.size());
            }
        }


    }


}
