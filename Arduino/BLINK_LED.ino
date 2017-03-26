//BLINK LED

const int LED = 13;
const int led12 = 12;

void setup(){
  
  pinMode(LED, OUTPUT);
  pinMode(led12, OUTPUT);
  
}

void loop(){

  digitalWrite(LED, HIGH);
  digitalWrite(led12, HIGH);
  delay(1000);
  digitalWrite(LED, LOW);
  digitalWrite(led12, LOW);
  delay(1000);
  
}

