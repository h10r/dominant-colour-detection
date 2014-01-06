
import de.bezier.data.sql.*;

class Database {

  SQLite db;

  public Database( PApplet parent ) {
    this.db = new SQLite( parent, "tonks.db" );
  }

  void read() {
    if ( this.db.connect() )
    {
      String[] tableNames = this.db.getTableNames();

      println( tableNames[0] );
    }
  }

  Image find( String filename ) {
    String query = "SELECT * FROM images WHERE filename='" + filename + "'";
    this.db.query( query );

    Image t = new Image( "" );
    this.db.setFromRow( t );

    return t;
  }

  /*
  *
   * INSERT INTO images VALUES( NULL, TIME('now'), "random/path/whatever.png", "red,red-orange,blue", "some,clever,tags" );
   *
   */

  void insert( Image img ) {
    String query = "INSERT INTO images " + String.format( " VALUES( NULL, TIME('now'), %s, %s, %s );", img.Filename, img.Colors, img.Tags );
    this.db.query( query );
  }

  void listAllImages() {
    this.db.query( "SELECT * FROM images" );

    while ( this.db.next () )
    {
      Image t = new Image( "" );
      this.db.setFromRow( t );
      println( t );
    }
  }

  void delete( Image img ) {
  }

  void write() {
  }
}


/*
*
 * Just use "sqlite3 tonks.db" on the command line to drop and create tables
 *
 * "CREATE TABLE IF NOT EXISTS images ( Id INTEGER PRIMARY KEY, time TIME, filename STRING, colors STRING, tags STRING );"
 *
 *
 *
 */

class Image
{
  public String Filename;
  public String Colors;
  public String Tags;

  public Image( String newFilename ) {
    this.Filename = newFilename;
    this.Colors = "";
    this.Tags = "";
  }

  void addColor( String newColor ) {
    this.Colors = this.Colors + "," + newColor;
  }
}

