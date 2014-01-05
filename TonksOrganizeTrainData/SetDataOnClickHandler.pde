class SetDataOnClickHandler extends ClickHandler {
  ImageFolder Images;

  String Category;
  String Value;

  public SetDataOnClickHandler( String category, String value  ) {
    this.Category = category;
    this.Value = value;
  }

  void run() {
    println( "run() SetDataOnClickHandler" );
    println( this.Category );
    println( this.Value );
  }  
}

