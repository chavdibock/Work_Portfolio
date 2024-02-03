/**

 * File: PurchasesArrayList.java

 * Author: Nikola Georgiev
 * Date: 12/07/2023

 */


import java.util.*;

public class PurchasesArrayList {

    public static void main(String[] args) {
        ArrayList<Purchase> purchases = new ArrayList<Purchase>();
        Scanner kb = new Scanner(System.in);
        String category;
        double price;
        final String QUIT = "ZZZ";

        System.out.print("Enter category for purchase or " + QUIT + " to quit >> ");
        category = kb.nextLine();

        while (!category.equals(QUIT)) {
            System.out.print("Enter amount spent >> ");
            price = kb.nextDouble();
            kb.nextLine();
            purchases.add(new Purchase(category, price));
            System.out.print("Enter category for purchase or " + QUIT + " to quit >> ");
            category = kb.nextLine();
        }

        System.out.println();
        System.out.println("Before sort: ");
        display(purchases);

        Collections.sort(purchases);
        
        System.out.println("After sort: ");
        display(purchases);
    }

    public static void display(ArrayList<Purchase> p) {
        for (int x = 0; x < p.size(); ++x)
            System.out.println(" " + p.get(x).getCategory() + " " + p.get(x).getPrice());
        System.out.println();
    }
}