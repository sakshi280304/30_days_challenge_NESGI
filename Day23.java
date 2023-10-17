import java.util.ArrayList;
import java.util.List;

public class App {

    public static List<String> splitString(String input, char delimiter) {
        List<String> result = new ArrayList<>();
        StringBuilder currentSubstring = new StringBuilder();

        for (char character : input.toCharArray()) {
            if (character == delimiter) {

                result.add(currentSubstring.toString());

                currentSubstring = new StringBuilder();
            } else {

                currentSubstring.append(character);
            }
        }

        result.add(currentSubstring.toString());

        return result;
    }

    public static void main(String[] args) {

        String inputString = "This,is,a,custom,split,function";
        char delimiter = ',';

        List<String> result = splitString(inputString, delimiter);

        System.out.println("Original String: " + inputString);
        System.out.println("Result after splitting: " + result);
    }
}
