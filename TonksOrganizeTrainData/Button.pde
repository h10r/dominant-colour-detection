
class Button {
  
  final PImage CachedCheckboxImageUnchecked = loadImage("images/unchecked.png");
  final PImage CachedCheckboxImageChecked = loadImage("images/checked.png");

  int X, Y, W, H;
  String Label;

  boolean IsOver = false;
  
  boolean IsCheckable = false;
  boolean IsChecked = false;

  color ButtonForegroundColor = color(255);
  color ButtonBackgroundColor = color(0);
  color ButtonBackgroundHighlight = color(128);

  color ButtonEdgeRoundness = 10;

  color ButtonTextOffsetX = 32;
  color ButtonTextOffsetY = 7;

  ClickHandler Handler;

  public Button( String label ) {
    this.Label = label;
  }

  void setPositionAndDimensions( int x, int y, int w, int h ) {
    this.X = x;
    this.Y = y;

    this.W = w;
    this.H = h;
  }

  void setBackgroundAndHighlightColors( color buttonCustomBackground, color buttonCustomHighlight ) {
    this.ButtonBackgroundColor = buttonCustomBackground;
    this.ButtonBackgroundHighlight = buttonCustomHighlight;
  }

  void setClickHandler( ClickHandler handler ) {
    this.Handler = handler;
  }
  
  void setCheckable( boolean isCheckable ) {
    this.IsCheckable = isCheckable;
  }

  void display() {
    if ( this.IsOver ) {
      fill( this.ButtonBackgroundHighlight );
    } 
    else {
      fill( this.ButtonBackgroundColor );
    }
    rect( this.X, this.Y, this.W, this.H, this.ButtonEdgeRoundness );

    if ( this.IsCheckable ) {
      image( CachedCheckboxImageUnchecked, this.X + 5, this.Y + 5, 20, 20 );
    }

    fill( this.ButtonForegroundColor );
    text( this.Label, this.X + this.ButtonTextOffsetX, this.Y + this.ButtonTextOffsetY, this.W, this.H );
  }

  void reset() {
    this.IsOver = false;
  }

  void buttonPressed() {
    println( "buttonPressed" );
    if ( this.Handler != null ) {
      this.IsChecked = true;
      this.Handler.run();
    }
  }

  void checkIfMouseOver(int mouse_x, int mouse_Y) {
    if (mouse_x >= this.X && mouse_x <= this.X + this.W && 
      mouse_Y >= this.Y && mouse_Y <= this.Y + this.H) {
      this.IsOver = true;
    }
  }
}

