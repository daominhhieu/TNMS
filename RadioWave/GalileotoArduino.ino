#include <SPI.h>
#include <RF24.h>

int cur;
int pre = 0;
const uint64_t pipe[2] = {0xF0F0F0F0E1LL,0xE8E8F0F0E1LL};
RF24 radio(9,10);
void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.setDataRate(RF24_1MBPS);
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(76);
  radio.openWritingPipe(pipe[0]);
  radio.openReadingPipe(1, pipe[1]);
  radio.enableDynamicPayloads();
  radio.powerUp();
  // put your setup code here, to run once:
}
void loop() {
  Serial.println("Sending a string");
      const char text[32] = "GETSTRING";
      radio.write(text, sizeof(text));
      Serial.print("We sent our mess: ");
      Serial.write(text);    
      Serial.println("");
  radio.startListening();
  Serial.println("Starting loop");
  char receivedMessage[32] = {0};
  radio.read(receivedMessage, sizeof(receivedMessage));
  Serial.println(receivedMessage);
  Serial.println("Turning off the radio");
  delay(500);
  // put your main code here, to run repeatedly:
  radio.stopListening();
}
