class ImageFolder {

  int X, Y, W, H;

  final int W_MAX = 830;
  final int H_MAX = 500;

  float AspectRatio;

  boolean ImageIsSet;

  int CurrentImageIndex;

  ArrayList<String> CurrentFolder;

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

  void setImagePath( String imagePath ) {

    if ( this.isDirectory( imagePath ) ) {
      this.crawlFolder( imagePath );

      this.CurrentImageIndex = 0;
    } 
    else {
      String[] splitByFileType = split( imagePath, "." );
      
      if ( !this.isOfAllowedFileType( splitByFileType[splitByFileType.length-1] ) ) {
        println( "The file you selected is not an image!" );
        return;
      }
      
      String[] splitPath = splitTokens( imagePath, "/" );
     
      String pathWithoutFilename = "/";
      String filename = "";
      
      for( int s = 0; s < splitPath.length; s++ ) {
        if ( s < splitPath.length - 1 ) {
          pathWithoutFilename += splitPath[s] + "/";
        } else if ( s == splitPath.length - 1 ) {
          filename = splitPath[s];
        }
      }
      
      this.crawlFolder( pathWithoutFilename );
            
      this.CurrentImageIndex = 0;
      // this.CurrentImageIndex = this.findImageIndexFromFilename( fileName );
    }

    // this.setCurrentImage();
  }

  boolean isDirectory( String path ) {
    if ( splitTokens( path, "." ).length != 2) {
      return true;
    }
    return false;
  }

  void setCurrentImage() {
    /*
    this.CurrentImageIndex
    
    this.CurrentImage = loadImage( this.CurrentImagePath );

    this.AspectRatio = float( this.CurrentImage.height ) / float( this.CurrentImage.width );

    this.W = this.W_MAX;
    this.H = int( this.W * this.AspectRatio );

    if ( this.H > this.H_MAX ) {
      this.W = int( this.H_MAX / this.AspectRatio );
      this.H = this.H_MAX;
    }    

    this.ImageIsSet = true;
    */
  }

  void previousImage() {
    if ( !this.ImageIsSet ) {
      println( "Set image folder!" );
      return;
    }

    println( "previousImage" );
  }

  void nextImage() {
    if ( !this.ImageIsSet ) {
      println( "Set image folder!" );
      return;
    }

    println( "nextImage" );
  }

  final String[] allowedFileTypes = { 
    "jpeg", "jpg", "png"
  };

  boolean isOfAllowedFileType( String filePath ) {
    for ( int suffix = 0; suffix < allowedFileTypes.length; suffix++ ) {
      if ( filePath.equals( allowedFileTypes[suffix] ) ) {
        return true;
      }
    }
    return false;
  }

  void crawlFolder( String folderPath ) {

    this.CurrentFolder = new ArrayList<String>();

    File file = new File( folderPath );

    if ( file.isDirectory() ) {
      String[] filenames = file.list();


      for ( int i = 0; i < filenames.length ; i++ ) {
        String[] currentSplitFilename = splitTokens( filenames[ i ], "." );

        println( filenames[ i ] );
        println( currentSplitFilename.length );

        /*
        if ( currentSplitFilename.length == 1 ) { // if directory
         // println( currentSplitFilename[0] );
         // could be extended to recursively open subfolders
         } 
         else if ( currentSplitFilename.length == 2 ) { // if file
         this.CurrentFolder.add( filenames[ i ] );
         }
         
         if ( isOfAllowedFileType( filenames[ i ] ) ) {
         this.CurrentFolder.add( filenames[ i ] );
         }
         
         
         */
      }
    }
  }
  
  int findImageIndexFromFilename() {
    return 1;
  }
  
}

