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

}
