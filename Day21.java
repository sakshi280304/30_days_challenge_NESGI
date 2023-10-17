public class App {

    public static boolean areRotations(String str1, String str2) {

        if (str1.length() != str2.length()) {
            return false;
        }

        String concatenated = str1 + str1;

        return concatenated.contains(str2);
    }

    public static void main(String[] args) {
 
        String s1 = "abcd";
        String s2 = "cdab";

        if (areRotations(s1, s2)) {
            System.out.println(s1 + " and " + s2 + " are rotations of each other.");
        } else {
            System.out.println(s1 + " and " + s2 + " are not rotations of each other.");
        }
    }
}
