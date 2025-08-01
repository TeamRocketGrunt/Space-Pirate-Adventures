import java.io.*;
import java.util.*;

class index{

  //These will be used throughout
  public static String name;
  public static String bodyPart;


  public static void main(String[] args) throws IOException{
    Scanner scan = new Scanner(System.in);

    File story = new File("story.txt");
    Scanner storyReader = new Scanner(story);
    
    System.out.println(storyReader.nextLine());
    name = scan.nextLine();

    System.out.println(storyReader.nextLine());
    bodyPart = scan.nextLine();

    verify(scan);


  }

  public static void verify(Scanner scan){
    System.out.println("Captain "+name+", you have lost your " +bodyPart+". Is that correct? (Y/N)");
    String answer = scan.nextLine();
    if(answer.toLowerCase().equals("y")){
      System.out.print("Please enter your name: ");
      name = scan.nextLine();
      System.out.print("You lost your: ");
      bodyPart = scan.nextLine();
      verify(scan);
    }
  }
}