class ImageFolder {

  int X, Y, W, H;
  
  final int W_MAX = 600;
  final int H_MAX = 450;
  
  String CurrentImagePath;
  String FolderPath;
  ArrayList<String> ListOfImageFiles;
  
  PImage CurrentImage;

  public ImageFolder() {

    // this.CurrentImage = loadImage("moonwalk.jpg");
  }

  void setPositionAndDimensions( int x, int y, int w, int h ) {
    this.X = x;
    this.Y = y;

    this.W = w;
    this.H = h;
  }

  void display() {
    fill(0,0,255);
    rect( this.X, this.Y, this.W, this.H );
    // image( this.CurrentImage, this.X, this.Y, this.W, this.H );
  }
  
  void setImagePath( String folderPath ) {
    println( "setImagePath " + folderPath );
    
    this.FolderPath = folderPath;
  }
  
  void isImageDirectory() {
  
  }

  void previousImage() {
  }

  void nextImage() {
  }
  
  void crawlFolderForImages() {
    String[] allowedImageFileTypes = { 
      "jpeg", "jpg", "tif", "tiff", "png"
    };

    this.ListOfImageFiles = new ArrayList<String>();

    File file = new File( this.FolderPath );
    if (file.isDirectory()) {
      String[] filenames = file.list();

      this.CurrentImagePath = "";

      for ( int i = 0; i < filenames.length ; i++ ) {
        String[] currentSplitFilename = splitTokens( filenames[ i ], "." );

        println( currentSplitFilename.length );

        if ( currentSplitFilename.length == 1 ) { // if directory
          // println( currentSplitFilename[0] );
          // could be extended to recursively open subfolders
        } 
        else if ( currentSplitFilename.length == 2 ) { // if file
          for ( int suffix = 0; suffix < allowedImageFileTypes.length; suffix++ ) {
            if ( currentSplitFilename[1].equals( allowedImageFileTypes[suffix] ) ) {
              this.ListOfImageFiles.add( filenames[ i ] );
            }
            
            if ( this.CurrentImagePath == "" ) {
              this.CurrentImagePath = filenames[ i ];
            }
          }
        }
      }
    }
  }
}

