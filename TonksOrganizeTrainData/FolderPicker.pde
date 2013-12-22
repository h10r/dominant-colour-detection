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
      println("User selected " + selection.getAbsolutePath());
    }
  }
  
  void run() {
    println( "run() folderPicker" );
    this.show();
  }
}

