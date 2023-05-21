void setup() {
  Serial.begin(9600); //Porta padrão
}

void loop() {
  if (Serial.available()) {
    int valor = Serial.read();
    Serial.println(valor);
  }
}