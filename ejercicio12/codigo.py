from flask import Flask, render_template_string, request, redirect
import random

app = Flask(__name__)

# ======================
# PRODUCTOS
# ======================
productos = {
    "7501031311309":{"nombre":"Leche Lala","precio":28},
    "7501055302568":{"nombre":"Pan Bimbo","precio":35},
    "7501000101010":{"nombre":"Cereal Zucaritas","precio":72},
    "1234567890123":{"nombre":"Refresco Coca Cola","precio":18},
    "7502001122334":{"nombre":"Chocolate Carlos V","precio":16},
    "7503004455667":{"nombre":"Sabritas","precio":22},
    "7504009988771":{"nombre":"Agua Bonafont","precio":14},
    "7505001122445":{"nombre":"Galletas Oreo","precio":20}
}

carrito = []

# ======================
# HTML
# ======================
HTML = '''

<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1">

<title>Pink Store</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{
font-family:Arial;
background:linear-gradient(135deg,#ff4fa3,#ff85c1,#ffc1dd);
overflow:hidden;
color:white;
}

/* ESTRELLITAS */

.stars{
position:fixed;
width:100%;
height:100%;
top:0;
left:0;
pointer-events:none;
overflow:hidden;
}

.star{
position:absolute;
color:white;
animation:float 6s linear infinite;
opacity:0.8;
}

@keyframes float{

0%{
transform:translateY(100vh) rotate(0deg);
opacity:0;
}

20%{
opacity:1;
}

100%{
transform:translateY(-120vh) rotate(360deg);
opacity:0;
}

}

header{
background:rgba(255,255,255,0.15);
backdrop-filter:blur(10px);
padding:20px;
text-align:center;
font-size:30px;
font-weight:bold;
letter-spacing:2px;
box-shadow:0 4px 15px rgba(0,0,0,0.2);
}

.main{
display:flex;
height:90vh;
gap:20px;
padding:20px;
}

.left{
flex:1;
background:rgba(255,255,255,0.15);
backdrop-filter:blur(12px);
border-radius:25px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
padding:20px;
box-shadow:0 0 20px rgba(255,255,255,0.2);
}

.right{
flex:2;
background:rgba(255,255,255,0.12);
backdrop-filter:blur(12px);
border-radius:25px;
padding:20px;
overflow:auto;
box-shadow:0 0 20px rgba(255,255,255,0.2);
}

input{
padding:15px;
font-size:18px;
border:none;
border-radius:15px;
width:85%;
margin-bottom:15px;
outline:none;
background:white;
color:#ff1493;
font-weight:bold;
}

button{
padding:14px;
border:none;
border-radius:15px;
cursor:pointer;
font-weight:bold;
transition:0.3s;
font-size:16px;
}

button:hover{
transform:scale(1.06);
}

.scan{
background:#ff1493;
color:white;
width:220px;
}

.camera{
background:#ff69b4;
color:white;
width:220px;
margin-top:12px;
}

.clear{
background:#ff1744;
color:white;
margin-top:12px;
width:220px;
}

table{
width:100%;
border-collapse:collapse;
overflow:hidden;
border-radius:20px;
background:rgba(255,255,255,0.1);
}

th{
background:#ff1493;
padding:15px;
font-size:18px;
}

td{
padding:15px;
text-align:center;
border-bottom:1px solid rgba(255,255,255,0.2);
}

tr:hover{
background:rgba(255,255,255,0.1);
}

.total{
margin-top:20px;
font-size:32px;
font-weight:bold;
text-align:right;
color:white;
text-shadow:0 0 10px #ff1493;
}

.modal{
display:none;
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.9);
z-index:9999;
}

#scanner{
height:80%;
border-radius:20px;
overflow:hidden;
margin:20px;
}

.modal button{
position:absolute;
bottom:25px;
left:50%;
transform:translateX(-50%);
background:#ff1744;
color:white;
width:220px;
}

.productos{
margin-top:20px;
display:grid;
grid-template-columns:repeat(auto-fit,minmax(180px,1fr));
gap:15px;
}

.card{
background:rgba(255,255,255,0.15);
padding:15px;
border-radius:20px;
text-align:center;
box-shadow:0 0 15px rgba(255,255,255,0.15);
}

.card h3{
margin-bottom:10px;
}

.card button{
margin-top:10px;
width:100%;
background:#ff1493;
color:white;
}

</style>

</head>

<body>

<div class="stars" id="stars"></div>

<header>
✨ Pink Point Of Sale ✨
</header>

<div class="main">

<div class="left">

<form action="/escanear" method="post">

<input id="codigo"
name="codigo"
placeholder="Escanea o escribe código"
autofocus>

<button class="scan">
Agregar producto
</button>

</form>

<button class="camera" onclick="abrir()">
📷 Escanear cámara
</button>

<br>

<a href="/limpiar">

<button class="clear">
🗑 Vaciar carrito
</button>

</a>

</div>

<div class="right">

<table>

<tr>
<th>Producto</th>
<th>Cantidad</th>
<th>Total</th>
</tr>

{% for p in carrito %}

<tr>

<td>{{p.nombre}}</td>

<td>{{p.cantidad}}</td>

<td>${{p.precio * p.cantidad}}</td>

</tr>

{% endfor %}

</table>

<div class="total">
💖 Total: ${{total}}
</div>

<h2 style="margin-top:25px;">
⭐ Productos ⭐
</h2>

<div class="productos">

{% for codigo,p in productos.items() %}

<div class="card">

<h3>{{p.nombre}}</h3>

<p>${{p.precio}}</p>

<form action="/escanear" method="post">

<input type="hidden"
name="codigo"
value="{{codigo}}">

<button>
Agregar
</button>

</form>

</div>

{% endfor %}

</div>

</div>

</div>

<!-- MODAL CAMARA -->

<div id="modal" class="modal">

<div id="scanner"></div>

<button onclick="cerrar()">
Cerrar cámara
</button>

</div>

<!-- LIBRERIA -->

<script src="https://unpkg.com/@ericblade/quagga2/dist/quagga.min.js"></script>

<script>

let escaneando = false;

/* =====================
CAMARA
===================== */

function abrir(){

if(escaneando) return;

escaneando = true;

document.getElementById("modal").style.display="block";

Quagga.init({

inputStream:{
type:"LiveStream",
target:document.querySelector('#scanner'),
constraints:{
facingMode:"environment"
}
},

decoder:{
readers:[
"ean_reader",
"code_128_reader",
"upc_reader"
]
}

},

function(err){

if(err){

alert("Error cámara");

escaneando=false;

return;

}

Quagga.start();

});

Quagga.onDetected(detectar);

}

function detectar(data){

let codigo = data.codeResult.code;

document.getElementById("codigo").value = codigo;

Quagga.offDetected(detectar);

Quagga.stop();

escaneando = false;

cerrar();

document.forms[0].submit();

}

function cerrar(){

document.getElementById("modal").style.display="none";

try{
Quagga.stop();
}catch(e){}

escaneando=false;

}

/* =====================
ESTRELLITAS
===================== */

function crearEstrella(){

const star = document.createElement("div");

star.classList.add("star");

star.innerHTML = "✦";

star.style.left =
Math.random()*100 + "vw";

star.style.fontSize =
(Math.random()*20+10)+"px";

star.style.animationDuration =
(Math.random()*5+4)+"s";

document.getElementById("stars")
.appendChild(star);

setTimeout(()=>{
star.remove();
},7000);

}

setInterval(crearEstrella,250);

</script>

</body>
</html>

'''

# ======================
# PAGINA PRINCIPAL
# ======================
@app.route("/")
def inicio():

    total = sum(
        p["precio"] * p["cantidad"]
        for p in carrito
    )

    return render_template_string(
        HTML,
        carrito=carrito,
        total=total,
        productos=productos
    )

# ======================
# ESCANEAR
# ======================
@app.route("/escanear", methods=["POST"])
def escanear():

    codigo = request.form["codigo"]

    # PRODUCTO EXISTENTE
    if codigo in productos:

        prod = productos[codigo]

    # PRODUCTO INVENTADO
    else:

        prod = {
            "nombre":"Producto Rosa "+codigo[-4:],
            "precio":random.randint(15,80)
        }

    # SI YA EXISTE
    for p in carrito:

        if p["codigo"] == codigo:

            p["cantidad"] += 1

            return redirect("/")

    # NUEVO PRODUCTO
    carrito.append({

        "codigo":codigo,
        "nombre":prod["nombre"],
        "precio":prod["precio"],
        "cantidad":1

    })

    return redirect("/")

# ======================
# LIMPIAR
# ======================
@app.route("/limpiar")
def limpiar():

    carrito.clear()

    return redirect("/")

# ======================
# EJECUTAR
# ======================
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
