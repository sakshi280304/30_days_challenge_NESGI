import java.util.Scanner;

public class App {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a numeric string: ");
        String numericString = scanner.nextLine();

        try {

            int intValue = Integer.parseInt(numericString);

            System.out.println("Converted integer value: " + intValue);
        } catch (NumberFormatException e) {

            System.out.println("Error: Not a valid numeric string.");
        }
    }
}
