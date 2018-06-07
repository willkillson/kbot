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
    public void TestCrypterCarSet(){
        CrypterCar car = new CrypterCar(true,2,2);

        IntPair testPair = new IntPair(1,1);
        car.visitedPositions.add(testPair);
        assertTrue(car.visitedPositions.contains(testPair));


        car.moveRotateRight();

        testPair.y = 1;
        testPair.x = 1;
        assertTrue(car.visitedPositions.contains(testPair));
        assertEquals(2,car.visitedPositions.size());
    }


}
