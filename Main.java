public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5, 6, 7};

        int max = numbers[0];


        for (int i = 0; i < numbers.length; i++) {
            if (max < numbers[i]){
                max=numbers[i];
            }
        }
        System.out.println("Maximum number is : "+max);
    }
}
