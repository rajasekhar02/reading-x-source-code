import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class RefDataStructures {
    public static void main(String[] args) {
        // array list iteration
        Integer[] temp = { 1, 2, 3 };
        List<Integer> x = new ArrayList<Integer>(Arrays.asList(3, 2, 1, 4));
        x.add(1);
        x.add(20);
        // x.addAll(Arrays.asList(temp));
        Collections.addAll(x, temp);
        System.out.println("Before Sorting");
        printArrayList(x);
        // array list sort
        x.sort((a, b) -> {
            return a.compareTo(b);
        });
        System.out.println("After Sorting");
        printArrayList(x);
    }

    static void printArrayList(List<Integer> arr) {
        arr.forEach((z) -> {
            System.out.println(z);
        });
    }
}
