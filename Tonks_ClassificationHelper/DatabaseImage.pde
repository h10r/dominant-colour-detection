/*
 *
 * Just use "sqlite3 tonks.db" on the command line to drop and create tables
 *
 * "CREATE TABLE IF NOT EXISTS images ( Id INTEGER PRIMARY KEY, time TIME, filename STRING, colors STRING, tags STRING );"
 *
 *
 *
 */

class DatabaseImage
{
  public String Filename;
  public String Colors;
  public String Tags;

  public DatabaseImage( String newFilename ) {
    this.Filename = newFilename;
    this.Colors = "";
    this.Tags = "";
  }

  void addOrRemoveColor( String newColor ) {
    println( this.Colors.indexOf(newColor) );

    if ( this.Colors == "" ) {
      this.Colors = newColor;
    } else {
      this.Colors = this.Colors + "," + newColor;
    }
    
    println( this.Colors );
  }
  
  void setTags( String newTags ) {
    this.Tags = newTags;
  }

}

