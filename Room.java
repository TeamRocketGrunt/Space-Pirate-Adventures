import java.util.*;

public class Room {
  private String description;
  private Map<String, Room> exists;

  public Room(String description){
    this.description = description;
    exits = new HashMap<>();
  }

  public void setExit(String direction, Room room){
    exits.put(direction,room);
  }
}
