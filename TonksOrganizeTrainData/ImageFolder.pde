class ImageFolder {

  int X, Y, W, H;
  
  String FolderPath;
  PImage CurrentImage;

  public ImageFolder( String folderPath ) {
    this.FolderPath = folderPath;

    this.CurrentImage = loadImage("moonwalk.jpg");
  }

  void setPositionAndDimensions( int x, int y, int w, int h ) {
    this.X = x;
    this.Y = y;

    this.W = w;
    this.H = h;
  }

  void displayCurrentImage() {
    image( this.CurrentImage, this.X, this.Y, this.W, this.H );
  }

  void previousImage() {
  }

  void nextImage() {
  }
}

