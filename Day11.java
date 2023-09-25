import java.util.Scanner;

public class Day11 {
    public static void printNumbersInRange(int low, int high) {
        if (low > high) {
            System.out.println("Invalid range. The low number should be less than or equal to the high number.");
            return;
        }

        System.out.println("Numbers between " + low + " and " + high + ":");
        for (int i = low; i <= high; i++) {
            System.out.print(i + " ");
        }
        System.out.println(); // Move to the next line for better formatting
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the low number: ");
        int low = scanner.nextInt();

        System.out.print("Enter the high number: ");
        int high = scanner.nextInt();

        scanner.close();

        printNumbersInRange(low, high);
    }
}
