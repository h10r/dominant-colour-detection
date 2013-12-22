class FolderPicker extends ClickHandler {

  String[] InputFileContents;
  String FolderPath;

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
 
      println("User selected " + this.FolderPath);
      
      println( this.listFileNames() );
    }
  }

  void run() {
    println( "run() folderPicker" );
    this.show();
  }

  /* credit to http://computationalphoto.mlog.taik.fi/2011/03/05/processing-finding-images-in-a-directory-listing/ */
  String[] listFileNames() {

    File file = new File( this.FolderPath );
    if (file.isDirectory()) {
      String[] names = file.list();
      return names;
    }
    else {
      return null;
    }
  }

  String[] findImgFiles( String[] filenames ) {

    String[] outList_of_foundImageFiles = {};
    
    String[] list_of_imageFileSuffixes = { 
      "jpeg", "jpg", "tif", "tiff", "png"
    };

    if ( this.FolderPath.charAt( this.FolderPath.length() -1 ) != '/' ) {
      this.FolderPath = this.FolderPath + '/';
    }

    for ( int file_i = 0; file_i < filenames.length ; file_i++ ) {

      println(" looking at file " + filenames[file_i] + " checking if it might not just be a image file ");

      String[] curr_filenameSplit = splitTokens( filenames[ file_i ], "." );

      for ( int fileSuffix_i = 0 ; fileSuffix_i < list_of_imageFileSuffixes.length ; fileSuffix_i++ ) {
        String examinedFile_filesuffix = curr_filenameSplit[1] ;
        String listOfValid_fileSuffixed = list_of_imageFileSuffixes[fileSuffix_i] ;

        if ( examinedFile_filesuffix.equals( listOfValid_fileSuffixed ) ) {
          outList_of_foundImageFiles = append( outList_of_foundImageFiles, this.FolderPath + filenames[ file_i ] );
        }
      }
    }

    return outList_of_foundImageFiles;
  }
}

