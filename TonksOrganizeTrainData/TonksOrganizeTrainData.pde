/**
 *
 * Allow to set color circle
 * 
 */

PFont f;

TextInput textInput;

ArrayList<Button> buttons;
ArrayList<Label> labels;

FolderPicker folderPicker;

void setup() {
  size(1024, 600);

  f = createFont("Consolas",12,true);
  textFont(f);

  textInput = new TextInput();
  textInput.setPositionAndDimensions( 10, height - 100, 800, 90 );

  buttons = new ArrayList<Button>();
  setupButtons();
  
  labels = new ArrayList<Label>();
  setupLabels();
  
  folderPicker = new FolderPicker();
}

void setupButtons() {
  Button b0 = new Button( "Test" );
  b0.setPositionAndDimensions( width - 140, 40, 125, 30 );
  buttons.add( b0 );

  Button b1 = new Button( "Test" );
  b1.setPositionAndDimensions( width - 140, 80, 125, 30 );
  buttons.add( b1 );
}

void setupLabels() {
  Label l0 = new Label( "Colors in image:" );
  l0.setPositionAndDimensions( width - 140, 20 );
  labels.add( l0 );

  Label l1 = new Label( "Tag as:" );
  l1.setPositionAndDimensions( 10, height - 110 );
  labels.add( l1 );
}

void draw() {
  update(mouseX, mouseY);

  background( 168 );

  for (int i = buttons.size()-1; i >= 0; i--) {
    Button b = buttons.get(i);    
    b.display();
  }
  
  for (int i = labels.size()-1; i >= 0; i--) {
    Label l = labels.get(i);    
    l.display();
  }
  
  textInput.display();
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
  // make this on button click
  folderPicker.show();
}

void mouseReleased() {
  for (int i = buttons.size()-1; i >= 0; i--) {
    Button b = buttons.get(i);
    b.reset();
  }
}

void keyPressed() {
  if (keyCode == BACKSPACE || keyCode == DELETE) {
      textInput.backspace();
  } else {
    textInput.addKey( key );
  }
}

void folderSelected(File selection) {
  folderPicker.folderSelected( selection );
}


