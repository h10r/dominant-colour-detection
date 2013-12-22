class FolderPicker extends ClickHandler {

  String[] InputFileContents;
  String FolderPath;

  ArrayList<String> listOfImageFiles;

  public FolderPicker() {
  }

  void show() {
    selectFolder("Select a file : ", "folderSelected");
  }

  void folderSelected(File selection) {
    if (selection == null) {
      println("Window was closed or the user hit cancel.");
    } 
    else {
      this.FolderPath = selection.getAbsolutePath();

      println("User selected: " + this.FolderPath);

      this.crawlFolderForImages();
    }
  }

  void run() {
    println( "run() folderPicker" );
    this.show();
  }

  void crawlFolderForImages() {
    String[] allowedImageFileTypes = { 
      "jpeg", "jpg", "tif", "tiff", "png"
    };

    listOfImageFiles = new ArrayList<String>();

    File file = new File( this.FolderPath );
    if (file.isDirectory()) {
      String[] filenames = file.list();

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
              listOfImageFiles.add( filenames[ i ] );
            }
          }
        }
      }
    }
  }
}

