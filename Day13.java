public class Day13 {
    public static void generatePermutations(String str) {
        generatePermutationsHelper(str, "");
    }

    private static void generatePermutationsHelper(String remaining, String currentPermutation) {
        if (remaining.isEmpty()) {
           
            System.out.println(currentPermutation);
        } else {
            for (int i = 0; i < remaining.length(); i++) {
                
                char chosen = remaining.charAt(i);

                String newRemaining = remaining.substring(0, i) + remaining.substring(i + 1);

                generatePermutationsHelper(newRemaining, currentPermutation + chosen);
            }
        }
    }

    public static void main(String[] args) {
        String input = "abc";
        generatePermutations(input);
    }
}
