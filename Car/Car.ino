#include <LiquidCrystal_I2C.h>
#include <TimerOne.h>
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);
int a = 0;
int redL = 8;
int whiteL = 7;
int stateL;
int stateR;
int leftL = 12;
int rightL = 13;
int val;
int valR = 0;
int valL = 0;
int x = 11;
int y = 11;
int z = 11;
int E1 = 5;
int M1 = 4;
int E2 = 6;
int M2 = 7;
boolean ledstate = HIGH;
int count;
void setup() {
  pinMode(rightL, OUTPUT);
  pinMode(leftL, OUTPUT);
  pinMode(redL, OUTPUT);
  pinMode(whiteL, OUTPUT);
  pinMode(11, OUTPUT);
  Timer1.initialize(1000000);
  Timer1.pwm(9, 512);
  Timer1.attachInterrupt(defineL);
  lcd.begin (16,2);
  pinMode(M1, OUTPUT);
  pinMode(E1, OUTPUT);
  pinMode(M2, OUTPUT);
  pinMode(E2, OUTPUT);
  Serial.begin(9600);
}
void defineL(){
  digitalWrite(x, !digitalRead(x));
  digitalWrite(y, HIGH);
  digitalWrite(z, HIGH);
}  
void loop() {
  while(Serial.available() == 0);
  val = Serial.read();
  backL(val, valL, valR);
  slowL(val, valL, valR);
  if(val > 55 && val < 111){
    if(val > 85){
      valL = map(val, 86, 110, 0, 250);
      stateL = 1;
    }
    else{
      stateL = 0;
      valL = map(val, 60, 85, 250, 0);
    }
  }
  if(val < 55){
    if(val > 25){
      valR = map(val, 26, 50, 0, 250);
      stateR = 1;
    }
    else{
      stateR = 0;
      valR = map(val, 0, 25, 250, 0);
    }
  }
  MotorState(stateL, stateR ,valL,valR);
  lcd.setCursor(0,0);
  lcd.write("Right");
  lcd.setCursor(12,0);
  lcd.write("Left");
  lcd.setCursor(0,1);
  lcd.print(valR);
  lcd.write("  ");
  lcd.setCursor(12,1);
  lcd.print(valL);
  lcd.write("  ");
  x = Light(val);
}
void MotorState(int sL, int sR, int s2, int s3){
    digitalWrite(M1, sL);
    digitalWrite(M2, sR);
    analogWrite(E1, s2);
    analogWrite(E2, s3);
}
int Light(int LSignal){
  int SigX = 11;
  if (LSignal == 112){
    digitalWrite(rightL, LOW);
    SigX = leftL;
  }
  if (LSignal == 113){
    digitalWrite(leftL, LOW);
    SigX = rightL;
  }
  if (LSignal == 114){
    digitalWrite(leftL, LOW);
    digitalWrite(rightL, LOW);
  }
  return SigX;
}
int slowL (int v, int vL, int vR){
  int stL = 11;
  if(26 < v < vR || 86 < v < vL){
    stL = redL;
  }
  return stL;
}
int backL (int v, int vL, int vR){
  int bkL = 11;
  if(v < vR < 26 || v < vL < 86){
    bkL = whiteL;
  }
  return bkL;
}

