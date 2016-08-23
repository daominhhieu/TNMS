#include <VirtualWire.h> 

void setup()
{
  Serial.begin(9600);
  Serial.println("Ready.........");
  vw_set_ptt_inverted(true);
  vw_setup(1024);
  vw_set_tx_pin(6);
}

void loop()
{
  char text[20] = "";
  byte i = 0;
  while (digitalRead(11) == 0 && digitalRead(12) == 0){
  }
  while (digitalRead(11)==1)
  {
    char ch[20] = "I love you";
    text[i] = ch[i];
    i++;
    delay(10);
    
  }
  while (digitalRead(12)==1)
  {
    char ch[20] = "I hate you";
    text[i] = ch[i];
    i++;
    delay(10);
    
  }
  Serial.print("sent: ");
  Serial.println(text);
  vw_send((byte *)text, sizeof(text));
  vw_wait_tx();
  delay(100);
}
