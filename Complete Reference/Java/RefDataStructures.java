import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RefDataStructures {
    public static void main(String[] args) {
        // int[] a = { 1, 2, 3, 4 };
        List<Integer> x = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4));
        x.forEach((z) -> {
            System.out.println(z);
        });
    }
}
