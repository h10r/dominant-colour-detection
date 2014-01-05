
import de.bezier.data.sql.*;

class Database {

  SQLite db;

  public Database( PApplet parent ) {
    db = new SQLite( parent, "tonks.db" );

    this.read();
  }

  void read() {
    if ( db.connect() )
    {
      String[] tableNames = db.getTableNames();

      println( tableNames[0] );

      db.query( "SELECT * FROM %s", tableNames[0] );

      while (db.next ())
      {
        Image t = new Image();
        db.setFromRow( t );
        println( t );
      }
    }
  }

  void write() {
  }
}


class Image
{
  public String fieldOne;
  public int fieldTwo;

  public String toString()
  {
    return String.format("fieldOne: %s fieldTwo: %d", fieldOne, fieldTwo);
  }
}

