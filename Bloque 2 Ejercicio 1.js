//Empresa ofrecen tarjetas de invitación
let Pedido = parseInt(prompt("Ingrese el valor del pedido"));
let precioUnitario; 
if (Pedido <=200) {
precioUnitario = 2.00;
} else if (Pedido < 201 && Pedido >= 300) {
    precioUnitario = 1.80;
} else {
    precioUnitario = 1.50;
}
let costototal = Pedido * precioUnitario; 
console.log(`Pedido: ${Pedido}, Precio Unitario: ${precioUnitario}, Total: ${costototal}`)
