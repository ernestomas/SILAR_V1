
#include <AFMotor.h>
#include <Stepper.h>
AF_Stepper crane(50, 2);                //Define Nombre del motor(# de pasos por vueltas, a la puerta M3 M4)
AF_Stepper plate(200, 1);               //Define Nombre del motor(# de pasos por vueltas, a la puerta M1 M2)
const int buttonPin = 2;                //Pin del boton de encendido y apagado 
String altura; 
String posiciones;
String times_inside;
String velocity; 
String sentido;
int ciclos;
int beakers;
volatile byte state = LOW;

void(* resetFunc) (void) = 0;

void setup()
   {
      pinMode(buttonPin,INPUT_PULLUP);
      Serial.begin(9600);            //Comunicación serial con la PC
      delay(30);
      crane.setSpeed(50);            //Define velocidad de giro en rpm de la grua
      plate.setSpeed(6);             //Define velocidad de giro en rpm de la base
      attachInterrupt(digitalPinToInterrupt(buttonPin), resetFunc, CHANGE);   //interruptor
}

void loop() {
  if (Serial.available()){
    String orden = Serial.readString();
    int comilla = orden.indexOf("[");
    int sep1 = orden.indexOf("/");
    posiciones = orden.substring(comilla,sep1);                     //Posiciones de los beakers.                     
    while (posiciones.indexOf(" ")!=-1){
      posiciones.remove(posiciones.indexOf(" "),1);
    }
    int sep2 = orden.indexOf("/",sep1+1);
    altura = orden.substring(sep1+1,sep2);                   //Altura que baja la grua.
    int sep3 = orden.indexOf("/",sep2+1);
    times_inside = orden.substring(sep2+1,sep3);                    //tiempo sumergido.
    int sep4 = orden.indexOf("/",sep3+1);
    velocity = orden.substring(sep3+1,sep4);                    //velocidad de sumergido. 
    int sep5 = orden.indexOf("/",sep4+1);
    sentido = orden.substring(sep4+1,sep5);                          //sentido de giro
    while (sentido.indexOf(" ")!=-1){
      sentido.remove(sentido.indexOf(" "),1);
    }
    int sep6 = orden.indexOf("/",sep5+1);
    ciclos = orden.substring(sep5+1,sep6).toInt();                   //Numero de ciclos
    int sep7 = orden.indexOf("/",sep6+1);
    beakers = orden.substring(sep6+1,sep7).toInt();                  //Numero de beakers
    int f_posiciones[beakers];
    fun(beakers,posiciones,f_posiciones);                            //Posiciones de los beakers.      
        int f_altura[beakers];
    fun(beakers,altura,f_altura);                                    //Altura que baja la grua.
        int f_times_inside[beakers];
    fun(beakers,times_inside,f_times_inside);                         //tiempo sumergido.
        int f_velocity[beakers];
    fun(beakers,velocity,f_velocity);                              //velocidad de sumergido. 
    
    for (int j=0;j<ciclos; j++){
        for (int i=0; i<beakers; i++){
            crane.setSpeed(f_velocity[i]);
            crane.step(f_altura[i], BACKWARD, MICROSTEP);
            delay(1000*f_times_inside[i]);
            crane.step(f_altura[i], FORWARD, MICROSTEP);
            if (i<beakers-1){
              int p=f_posiciones[i+1]-f_posiciones[i];
              for (int k=1; k<=p; k++){
                if (sentido =="FORWARD"){
                  delay(1);
                  plate.step(65, BACKWARD, SINGLE);    //Define (# de pasos a realizar, sentido de giro, método de giro (correspondiente al tipo de motor))
                }else if (sentido =="BACKWARD"){
                  delay(1);
                  plate.step(65, FORWARD, SINGLE);    //Define (# de pasos a realizar, sentido de giro, método de giro (correspondiente al tipo de motor))
                }
              }
            }
        }
        delay(1000);
        int f= f_posiciones[beakers-1]-f_posiciones[0];
        if (sentido =="FORWARD"){
          for (int i=0; i<f; i++){
            plate.step(65, FORWARD, SINGLE);    //Define (# de pasos a realizar, sentido de giro, método de giro (correspondiente al tipo de motor))
            delay(30);
          }
        }else if (sentido =="BACKWARD"){
          for (int i=0; i<f; i++){
            plate.step(65, BACKWARD, SINGLE);   //Define (# de pasos a realizar, sentido de giro, método de giro (correspondiente al tipo de motor))
            delay(30);
          }
        }
    }
  }
}

void fun(int num, String list, int list2[]){
  int pos=0;
  for (int i = 0; i<num; i++){
    int coma = list.indexOf(",",pos+1);
    list2[i]=list.substring(pos+1,coma).toInt(); 
    pos = coma;
  }
}

