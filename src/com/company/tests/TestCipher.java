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
        assertTrue(testCipher.isRotateRight);
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
    public void TestCrypterCarExhaustiveRotationRight(){

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

    @Test
    public void TestEncryptString1(){
        Cipher testCipher = new Cipher("\"WE ARE DISCOVERED. FLEE AT ONCE\" (9, 3) clockwise");
        testCipher.init();
        testCipher.encryptString();

        assertEquals("CEXXECNOTAEOWEAREDISLFDEREV", testCipher.cipherText);
    }

    @Test
    public void TestEncryptString2(){
        Cipher testCipher = new Cipher("\"why is this professor so boring omg\" (6, 5) counter-clockwise");
        testCipher.init();
        testCipher.encryptString();

        assertEquals("TSIYHWHFSNGOMGXIRORPSIEOBOROSS", testCipher.cipherText);
    }

    @Test
    public void TestEncryptString3(){
        Cipher testCipher = new Cipher("\"Solving challenges on r/dailyprogrammer is so much fun!!\" (8, 6) counter-clockwise");
        testCipher.init();
        testCipher.encryptString();

        assertEquals("CGNIVLOSHSYMUCHFUNXXMMLEGNELLAOPERISSOAIADRNROGR", testCipher.cipherText);
    }

    @Test
    public void TestEncryptString4(){
        Cipher testCipher = new Cipher("\"For lunch let's have peanut-butter and bologna sandwiches\" (4, 12) clockwise");
        testCipher.init();
        testCipher.encryptString();

        assertEquals("LHSENURBGAISEHCNNOATUPHLUFORCTVABEDOSWDALNTTEAEN", testCipher.cipherText);
    }

    @Test
    public void TestEncryptString5(){
        Cipher testCipher = new Cipher("\"I've even witnessed a grown man satisfy a camel\" (9,5) clockwise");
        testCipher.init();
        testCipher.encryptString();

        assertEquals("IGAMXXXXXXXLETRTIVEEVENWASACAYFSIONESSEDNAMNW", testCipher.cipherText);
    }

    @Test
    public void TestEncryptString6(){
        Cipher testCipher = new Cipher("\"Why does it say paper jam when there is no paper jam?\" (3, 14) counter-clockwise");
        testCipher.init();
        testCipher.encryptString();

        assertEquals("YHWDSSPEAHTRSPEAMXJPOIENWJPYTEOIAARMEHENAR", testCipher.cipherText);
    }


}
