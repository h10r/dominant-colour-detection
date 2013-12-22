class ImageFolder {

  int X, Y, W, H;

  final int W_MAX = 830;
  final int H_MAX = 500;

  float AspectRatio;

  boolean ImageIsSet;

  String CurrentImagePath;
  String FolderPath;
  ArrayList<String> ListOfImageFiles;

  PImage CurrentImage;

  public ImageFolder() {
    this.ImageIsSet = false;
  }

  void setPositionAndDimensions( int x, int y, int w, int h ) {
    this.X = x;
    this.Y = y;

    this.W = w;
    this.H = h;
  }

  void display() {
    if ( this.ImageIsSet ) {
      image( this.CurrentImage, this.X, this.Y, this.W, this.H );
    } 
    else {
      fill( 192 );
      rect( this.X, this.Y, this.W, this.H );
      fill( 0 );
      text( "Please select an image or folder", this.X + (this.W / 3.0), this.Y + (this.H / 2.0) );
    }
  }

  void setImagePath( String folderOrFilePath ) {

    if ( this.isImageDirectory( folderOrFilePath ) ) {
      this.FolderPath = folderOrFilePath;

      this.CurrentImagePath= this.crawlFolderForImagesAndSetCurrentImage();
    } 
    else {
      this.CurrentImagePath = folderOrFilePath;
    }

    this.setCurrentImage();
  }

  boolean isImageDirectory( String fileName ) {
    if ( splitTokens( fileName, "." ).length != 2) {
      return true;
    }
    return false;
  }

  void setCurrentImage() {
    this.CurrentImage = loadImage( this.CurrentImagePath );

    this.AspectRatio = float( this.CurrentImage.height ) / float( this.CurrentImage.width );

    this.W = this.W_MAX;
    this.H = int( this.W * this.AspectRatio );

    if ( this.H > this.H_MAX ) {
      this.W = int( this.H_MAX / this.AspectRatio );
      this.H = this.H_MAX;
    }    

    this.ImageIsSet = true;
  }

  void previousImage() {
  }

  void nextImage() {
  }

  String crawlFolderForImagesAndSetCurrentImage() {
    String[] allowedImageFileTypes = { 
      "jpeg", "jpg", "png"
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

    return ""; // TODO
  }
}

