let N = parseInt(prompt("Ingrese el numero de pedidos"));
for (let i = 1; i <= N; i++) {
    let Pedido = parseInt(prompt(`Pedidos: ${i} Ingrese la cantidad de tarjetas`));
    let precioUnitario; 
    if (Pedido <= 200) {
        precioUnitario = 2.00;
    } else if (Pedido > 201 && Pedido <= 300) {
        precioUnitario = 1.80;
    } else {
        precioUnitario = 1.50; 
    }
    let preciototal = Pedido * precioUnitario 
}
console.log(`Pedidos ${i}: Pedido = ${Pedido}, Total = ${preciototal}`)
