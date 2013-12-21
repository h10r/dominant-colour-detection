/**
 *
 * Allow to set color circle
 * 
 */

ArrayList<Button> buttons;

void setup() {
  size(1024, 600);

  buttons = new ArrayList<Button>();

  setupButtons();
}

void setupButtons() {

  Button b0 = new Button( "Test" );
  b0.setPositionAndDimensions( width/2, height / 2, 150, 40 );

  buttons.add( b0 );
}

void draw() {
  update(mouseX, mouseY);

  background( 168 );

  for (int i = buttons.size()-1; i >= 0; i--) {
    Button b = buttons.get(i);    
    b.display();
  }
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

