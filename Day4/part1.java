package Day4;

import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;
public class part1 {

    public static void main(String[] args) {
        ArrayList<String> pulledNumbers = new ArrayList<String>();
        ArrayList<String> bingoCards = new ArrayList<String>();
        ArrayList<String> holdingList2 = new ArrayList<String>();

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
            while (reader.hasNext()){
                data = reader.next();
                pulledNumbers.add(data);
            }
            */
        }
        catch (FileNotFoundException e){
            System.out.println("Couldn't locate the file.");
        }

        System.out.println("Hello");
        for (int i = 0; i < pulledNumbers.size(); i++){
            System.out.println(pulledNumbers.get(i) + "/");
        }
        System.out.println(pulledNumbers.get(6));
    }
}