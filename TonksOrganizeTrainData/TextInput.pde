final color textInputForegroundColor = color(0);
final color textInputBackgroundColor = color(0,128,0);

final color textInputTextOffsetX = 6;
final color textInputTextOffsetY = 6;


class TextInput {

  int X, Y, W, H;
  
  String inputText;

  public TextInput() {
    clearInput();
  }
  
  void clearInput() {
    this.inputText = "";
  }

  void setPositionAndDimensions( int x, int y, int w, int h ) {
    this.X = x;
    this.Y = y;
    
    this.W = w;
    this.H = h;    
  }

  void display() {
    fill( textInputBackgroundColor );
    rect( this.X, this.Y, this.W, this.H );
    
    fill(textInputForegroundColor);
    text( this.inputText, this.X + textInputTextOffsetX, this.Y + textInputTextOffsetY, this.W, this.H );
  }
  
  void addKey( char newKey ) {
    this.inputText = this.inputText + newKey;
    println( this.inputText ); 
  }
}

