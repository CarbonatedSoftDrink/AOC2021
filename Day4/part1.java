package Day4;

import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;
public class part1 {

    public static void main(String[] args) {
        ArrayList<String> pulledNumbers = new ArrayList<String>();
        ArrayList<String> bingoCards = new ArrayList<String>();
        String[] bingoCard = new String[40];
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