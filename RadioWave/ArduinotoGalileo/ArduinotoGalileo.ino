#include <SPI.h>
#include <RF24.h>

RF24 radio(9,10 );
void setup() {
  Serial.begin(9600);
  
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(76);
  radio.setDataRate(RF24_1MBPS);
  radio.openReadingPipe(1, 0xF0F0F0F0E1LL);
  const uint64_t pipe = 0xE8E8F0F0E1LL;
  radio.openWritingPipe(pipe);
  radio.enableDynamicPayloads();
  radio.powerUp();
  
  // put your setup code here, to run once:

}

void loop() {
  radio.startListening();
  Serial.println("Starting loop");
  char receivedMessage[32] = {0};
  if (radio.available()){
    while (radio.available()){
      radio.read(receivedMessage, sizeof(receivedMessage));
    }
    Serial.println(receivedMessage);
    Serial.println("Turning off the radio");
    radio.stopListening();

    String stringMessage(receivedMessage);

    if (stringMessage == "GETSTRING"){
      Serial.println("Sending a string");
      const char text[32] = "Hello World";
      radio.write(text, sizeof(text));
      Serial.print("We sent our mess: ");
      Serial.write(text);    
      Serial.println("");
    }
  }
  delay(100);
  // put your main code here, to run repeatedly:

}
