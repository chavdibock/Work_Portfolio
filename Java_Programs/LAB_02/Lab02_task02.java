/*
 * File: Lab02_task02.java

 * Author: NIkola Georgiev

 * Date: 13.11.2023

 */

public class Sportsman {
    private String name;
    private String sport;
    private int rankOrNumber;

    // Constructor with 3 parameters to initialize data members using setters
    public Sportsman(String name, String sport, int rankOrNumber) {
        setName(name);
        setSport(sport);
        setRankOrNumber(rankOrNumber);
    }

    // Accessor method for name
    public String getName() {
        return name;
    }

    // Mutator method for name
    public void setName(String name) {
        this.name = name;
    }

    // Accessor method for sport
    public String getSport() {
        return sport;
    }

    // Mutator method for sport
    public void setSport(String sport) {
        this.sport = sport;
    }

    // Accessor method for rankOrNumber
    public int getRankOrNumber() {
        return rankOrNumber;
    }

    // Mutator method for rankOrNumber
    public void setRankOrNumber(int rankOrNumber) {
        this.rankOrNumber = rankOrNumber;
    }

    public static void main(String[] args) {
        // Create an instance of the Sportsman class and initialize it with your favorite sportsman
        Sportsman favoriteSportsman = new Sportsman("Usain Bolt", "Athletics", 1);

        // Display information about the favorite sportsman
        System.out.println("Favorite Sportsman:");
        System.out.println("Name: " + favoriteSportsman.getName());
        System.out.println("Sport: " + favoriteSportsman.getSport());
        System.out.println("Rank or Number: " + favoriteSportsman.getRankOrNumber());
    }
}
