const int readoutIN = A0;

int sensorvalue = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(readoutIN, INPUT);


}

void loop() {
  // put your main code here, to run repeatedly:
  
  sensorvalue = analogRead(readoutIN);
  delay(100);

  Serial.print(sensorvalue);
  Serial.print("\n");
}
