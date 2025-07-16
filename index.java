import java.util.*;

class index{

  //These will be used throughout
  public static String name;
  public static String bodyPart;


  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.println("Welcome to the Space Pirate Adventure. You are the captain of the dreaded Donkey Hotey. Once your ship ruled the depths of space, but you've fallen on hard times. What is your name? ");
    name = scan.nextLine();
    System.out.print(name);
  }
}