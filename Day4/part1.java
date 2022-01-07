package Day4;

import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;
public class part1 {

    public static void determine(){
        boolean bingo = false;

    }

    public static void main(String[] args) {
        ArrayList<String> pulledNumbers = new ArrayList<String>();
        ArrayList<String> bingoCards = new ArrayList<String>();
        String[] bingoCard = new String[40];
        int[] winningIndexes = new int[25];
        int[] row1 = {0, 1, 2, 3, 4};
        int[] row2 = {5, 6, 7, 8, 9};
        int[] row3 = {10, 11, 12, 13, 14};
        int[] row4 = {15, 16, 17, 18, 19};
        int[] row5 = {20, 21, 22, 23, 24};
        int[] col1 = {0, 5, 10, 15, 20};
        int[] col2 = {1, 6, 11, 16, 21};
        int[] col3 = {2, 7, 12, 17, 22};
        int[] col4 = {3, 8, 13, 18, 23};
        int[] col5 = {4, 9, 14, 19, 24};
        int cardIndex = -1;
        int cardMax = -1;
        int cardScore = -1;

        try{
            File mine = new File("Day4/input.txt");
            Scanner reader = new Scanner(mine);
            // Grab all the bingo numbers
            String data = reader.next();
            String[] holdingList = data.split(",");
            for (int i = 0; i < holdingList.length; i++){
                pulledNumbers.add(holdingList[i]);
            }

            /*
            data = reader.next();
            holdingList = data.split(" ");
            for (int i = 0; i < holdingList.length; i++){
                bingoCards.add(holdingList[i]);
            }
            */

            //data = reader.next();
            int i = 0;
            while(i < 25){
                data = reader.next();
                bingoCards.add(data);
                i++;
            }
        }
        catch (FileNotFoundException e){
            System.out.println("Couldn't locate the file.");
        }

        System.out.println("Hello");
        for (int i = 0; i < bingoCards.size(); i++){
            System.out.println(bingoCards.get(i) + "/");
        }
    }
}