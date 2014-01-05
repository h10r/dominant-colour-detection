PFont f;

TextInput textInput;

Label lblFilename;

ArrayList<Button> buttons;
ArrayList<Label> labels;

FolderPicker folderPicker;
ImageFolder imageFolder;

KeyHandler keyHandler;

void setup() {
  size(1024, 600);

  f = createFont("OpenSans-Bold", 12, true);
  textFont(f);

  keyHandler = new KeyHandler();

  textInput = new TextInput();
  textInput.setPositionAndDimensions( 10, 540, 800, 55 );

  imageFolder = new ImageFolder();
  imageFolder.setPositionAndDimensions( 10, 10, 830, 500 );
  
  // float imageRation =  this.H / this.W;
  
  folderPicker = new FolderPicker( imageFolder );

  labels = new ArrayList<Label>();
  setupLabels();  

  // make sure the clickHandler are set before setting the buttons
  buttons = new ArrayList<Button>();
  setupButtons();
}

final int MENU_LEFT_X = 850;
final int MENU_LEFT_W = 160;

final int MENU_FIRST_Y = 0;
final int MENU_OFFSET_Y = 35;

void setupButtons() {
  
  Button b1 = new Button( "Yellow" );
  b1.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (1*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b1.setCheckable( true );
  b1.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b1 );
  
  Button b2 = new Button( "Yellow-Orange" );
  b2.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (2*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b2.setCheckable( true );
  b2.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b2 );
  
  Button b3 = new Button( "Orange" );
  b3.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (3*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b3.setCheckable( true );
  b3.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b3 );

  Button b4 = new Button( "Red-Orange" );
  b4.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (4*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b4.setCheckable( true );
  b4.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b4 );

  Button b5 = new Button( "Red" );
  b5.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (5*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b5.setCheckable( true );
  b5.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b5 );

  Button b6 = new Button( "Red-Purple" );
  b6.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (6*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b6.setCheckable( true );
  b6.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b6 );

  Button b7 = new Button( "Purple" );
  b7.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (7*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b7.setCheckable( true );
  b7.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b7 );

  Button b8 = new Button( "Blue-Purple" );
  b8.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (8*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b8.setCheckable( true );
  b8.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b8 );

  Button b9 = new Button( "Blue" );
  b9.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (9*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b9.setCheckable( true );
  b9.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b9 );

  Button b10 = new Button( "Blue-Green" );
  b10.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (10*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b10.setCheckable( true );
  b10.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b10 );

  Button b11 = new Button( "Green" );
  b11.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (11*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b11.setCheckable( true );
  b11.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b11 );

  Button b12 = new Button( "Yellow-Green" );
  b12.setPositionAndDimensions( MENU_LEFT_X, MENU_FIRST_Y + (12*MENU_OFFSET_Y), MENU_LEFT_W, 30 );
  b12.setCheckable( true );
  b12.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  buttons.add( b12 );

  Button bFolderSelect = new Button( "Select Folder" );
  bFolderSelect.setPositionAndDimensions( MENU_LEFT_X, height - 70, MENU_LEFT_W, 30 );
  bFolderSelect.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  bFolderSelect.setClickHandler( folderPicker );
  buttons.add( bFolderSelect );

  Button bSave = new Button( "Save Database" );
  bSave.setPositionAndDimensions( MENU_LEFT_X, height - 35, MENU_LEFT_W, 30 );
  bSave.setBackgroundAndHighlightColors( color(231, 76, 60), color(236, 112, 99) );
  buttons.add( bSave );
}

void setupLabels() {
  Label l0 = new Label( "Colors in image:" );
  l0.setPositionAndDimensions( MENU_LEFT_X, 20 );
  labels.add( l0 );

  Label l1 = new Label( "Tag as (comma-separated values):" );
  l1.setPositionAndDimensions( 10, 530 );
  labels.add( l1 );
  
  lblFilename = new Label( "No file selected" );
  lblFilename.setPositionAndDimensions( 300, 530 );
  labels.add( lblFilename );
}

void draw() {
  update(mouseX, mouseY);

  background( 231, 235, 240 ); // 94 is my desktop background grey

  for (int i = buttons.size()-1; i >= 0; i--) {
    Button b = buttons.get(i);    
    b.display();
  }

  for (int i = labels.size()-1; i >= 0; i--) {
    Label l = labels.get(i);    
    l.display();
  }

  textInput.display();
  
  imageFolder.display();
}

void update(int x, int y) {
  if (mousePressed == true) {
    for (int i = buttons.size()-1; i >= 0; i--) {
      Button b = buttons.get(i);
      b.checkIfMouseOver(mouseX, mouseY);
    }
  }
}

void mousePressed() {
}

void mouseReleased() {
  for (int i = buttons.size()-1; i >= 0; i--) {
    Button b = buttons.get(i);

    if ( b.IsOver ) {
      b.buttonPressed();
    }
     b.reset();
  }
}

void keyPressed() {
  keyHandler.pressed();
}

void folderSelected(File selection) {
  folderPicker.folderSelected( selection );
}

