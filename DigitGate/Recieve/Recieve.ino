#include <VirtualWire.h>
byte msg[VW_MAX_MESSAGE_LEN];
byte msgLen = VW_MAX_MESSAGE_LEN;
const int led = 3;
String text="";
void setup() {
  Serial.begin(9600);
  pinMode (led,OUTPUT);
  //vw_set_ptt_inverted(true);
  vw_set_rx_pin(8);
  vw_setup(1024);
  vw_rx_start();
  // put your setup code here, to run once:

}

void loop() {
  if (vw_get_message(msg, &msgLen)){
  for (int i = 0; i < msgLen; i++){
    text += char(msg[i]);
  Serial.println(text);
  if (text == "I love you"){
    digitalWrite (led,1);
  }
  else if (text == "I hate you"){
    digitalWrite (led,0);
  }
  }
  }
  // put your main code here, to run repeatedly:
  text = "";
}
