#define buzzerPin 9
#define firePin 12
void setup() 
{
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
  pinMode(firePin, INPUT);
}

void loop()
{
  if(!(digitalRead(firePin)))
  {
    Serial.println("Fire Detected!");
    digitalWrite(buzzerPin, HIGH);
    delay(500);
    digitalWrite(buzzerPin, LOW);
    delay(500);
  }
}
