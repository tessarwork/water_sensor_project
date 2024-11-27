#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "TessarDepok_EXT";
const char* password = "passwordnya123"; 
const char* serverName = "http://Macbook-Pro-Grit.local:5000/data";

float random_float(float minValue, float maxValue){ 
  return minValue + (float)random() / (float)(RAND_MAX / (maxValue - minValue));
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while(WiFi.status() != WL_CONNECTED){ 
    delay(500);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to Wifi");

}

void loop() {
  // put your main code here, to run repeatedly:
  if (WiFi.status() == WL_CONNECTED) {
    float sensor1 = random_float(0.0, 100.0);
    float sensor2 = random_float(0.0, 100.0);
    float sensor3 = random_float(0.0, 100.0);

    if(isnan(sensor1) || isnan(sensor2) || isnan(sensor3)){ 
      Serial.println("Error is not a number");
      return;
    } 

    String jsonpayload = "{\"sensor1\":" + String(sensor1) + ", \"sensor2\":" + String(sensor2) + ", \"sensor3\":" + String(sensor3) + "}";
    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    int response_code = http.POST(jsonpayload);

    if (response_code > 0){ 
      String response = http.getString();
      Serial.println(response_code);
      Serial.println(response);

    } else{ 
      Serial.print("Error on sending POST: ");
      Serial.println(response_code);
    }
    http.end();
    

    
    
  }
  delay(3000);

}
