final color buttonForegroundColor = color(255);
final color buttonBackgroundColor = color(0);
final color buttonBackgroundHighlight = color(128);

final color buttonEdgeRoundness = 10;

class Button {

  int X, Y, W, H;
  String Label;

  boolean IsOver = false;

  public Button( String label ) {
    this.Label = label;
  }

  void setPositionAndDimensions( int x, int y, int w, int h ) {
    this.X = x;
    this.Y = y;
    
    this.W = w;
    this.H = h;    
  }

  void display() {
    if ( this.IsOver ) {
      fill( buttonBackgroundHighlight );
    } 
    else {
      fill( buttonBackgroundColor );
    }
    rect( this.X, this.Y, this.W, this.H, buttonEdgeRoundness );

    fill(buttonForegroundColor);
    text( this.Label, this.X, this.Y, this.W, this.H );
  }
  
  void reset() {
    this.IsOver = false;
  }

  void checkIfMouseOver(int mouse_x, int mouse_Y) {
    if (mouse_x >= this.X && mouse_x <= this.X + this.W && 
      mouse_Y >= this.Y && mouse_Y <= this.Y + this.H) {
      this.IsOver = true;
    }
  }
}

