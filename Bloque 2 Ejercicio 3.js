let N = parseInt(prompt("Ingrese el número de pedidos"));
let cantidades = [];   
let totales = [];      
for (let i = 1; i <= N; i++) {
    let Pedidos = parseInt(prompt(`Pedido ${i}: Ingrese la cantidad de tarjetas`));
    let precioUnitario;
    if (Pedidos <= 200) {
        precioUnitario = 2.00;
    } else if (Pedidos <= 300) {
        precioUnitario = 1.80;
    } else {
        precioUnitario = 1.50;
    }
    let preciototal = Pedidos * precioUnitario;
    cantidades.push(Pedidos);
    totales.push(preciototal);
}
for (let i = 0; i < N; i++) {
    console.log(`Pedido ${i + 1}: Cantidad = $${cantidades[i]}, Total = $${totales[i]}`);
}
