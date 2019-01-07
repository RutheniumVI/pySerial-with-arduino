#define output 10 //led connected to pin 10
#define THERMISTOR A0
char input;
String str;
void setup() {
  Serial.begin(9600);
  pinMode(output,OUTPUT);
}

void loop() {
  if(Serial.available()>0){
    while(Serial.available()>0){
      input=Serial.read();
      str+=input;
      delay(1);
    }
    if(str=="on"){
      digitalWrite(output,HIGH);
    }
    if(str=="off"){
      digitalWrite(output, LOW);
    }
    if(str=="get"){
      float average=0;
      for (int i=0; i< 5; i++) {//taking averages of 5
       average += analogRead(THERMISTOR);
       delay(10);
      }
      average /= 5;

      Serial.println(average);
    }
    str="";
  }

}
