// Entrada
let edad1 = parseInt(prompt("Ingrese la edad del primer hermano:"));
let edad2 = parseInt(prompt("Ingrese la edad del segundo hermano:"));
let edad3 = parseInt(prompt("Ingrese la edad del tercer hermano:"));
let mayor;
if (edad1 >= edad2 && edad1 >= edad3) {
    mayor = edad1;
} else if (edad2 >= edad1 && edad2 >= edad3) {
    mayor = edad2;
} else {
    mayor = edad3;
}
console.log("El hermano mayor tiene " + mayor + " años.");
