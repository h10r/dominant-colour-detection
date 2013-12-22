/**
 *
 * Allow to set color circle
 * 
 */

PFont f;
ArrayList<Button> buttons;
TextInput textInput;

void setup() {
  size(1024, 600);

  f = createFont("Consolas",12,true);
  textFont(f);

  textInput = new TextInput();
  textInput.setPositionAndDimensions( 10, height - 100, 800, 90 );

  buttons = new ArrayList<Button>();

  setupButtons();
}

void setupButtons() {
  Button b0 = new Button( "Test" );
  b0.setPositionAndDimensions( 6*width/7, 60, 125, 30 );
  buttons.add( b0 );

  Button b1 = new Button( "Test" );
  b1.setPositionAndDimensions( 6*width/7, 120, 125, 30 );
  buttons.add( b1 );
}

void draw() {
  update(mouseX, mouseY);

  background( 168 );

  for (int i = buttons.size()-1; i >= 0; i--) {
    Button b = buttons.get(i);    
    b.display();
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



