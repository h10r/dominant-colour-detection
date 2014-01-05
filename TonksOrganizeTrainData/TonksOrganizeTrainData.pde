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

void setupButtons() {
  Button b0 = new Button( "Test" );
  b0.setPositionAndDimensions( width - 140, 40, 125, 30 );
  buttons.add( b0 );

  Button b1 = new Button( "Test" );
  b1.setPositionAndDimensions( width - 140, 80, 125, 30 );
  buttons.add( b1 );

  Button bFolderSelect = new Button( "Select Folder" );
  bFolderSelect.setPositionAndDimensions( width - 140, height - 90, 125, 30 );
  bFolderSelect.setBackgroundAndHighlightColors( color(46, 204, 113), color(92, 184, 92) );
  bFolderSelect.setClickHandler( folderPicker );
  buttons.add( bFolderSelect );

  Button bSave = new Button( "Save Database" );
  bSave.setPositionAndDimensions( width - 140, height - 50, 125, 30 );
  bSave.setBackgroundAndHighlightColors( color(231, 76, 60), color(236, 112, 99) );
  buttons.add( bSave );
}

void setupLabels() {
  Label l0 = new Label( "Colors in image:" );
  l0.setPositionAndDimensions( width - 140, 20 );
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

