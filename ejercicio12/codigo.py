from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# ======================
# PRODUCTOS
# ======================
productos = {
    "7501031311309":{"nombre":"Leche","precio":28},
    "7501055302568":{"nombre":"Pan","precio":35},
    "7501000101010":{"nombre":"Cereal","precio":72},
    "1234567890123":{"nombre":"Refresco","precio":18}
}

carrito = []

HTML = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Punto de Venta</title>

<style>
body{
margin:0;
font-family:Arial;
background:linear-gradient(135deg,#0f172a,#1e293b);
color:white;
}

header{
background:#2563eb;
padding:18px;
text-align:center;
font-size:26px;
font-weight:bold;
letter-spacing:1px;
box-shadow:0 4px 10px rgba(0,0,0,0.3);
}

.main{
display:flex;
height:90vh;
gap:15px;
padding:15px;
}

.left{
flex:1;
background:#111827;
border-radius:15px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
box-shadow:0 0 15px rgba(0,0,0,0.4);
}

.right{
flex:2;
background:#0b1220;
border-radius:15px;
padding:20px;
overflow:auto;
box-shadow:0 0 15px rgba(0,0,0,0.4);
}

input{
padding:14px;
font-size:18px;
border-radius:10px;
border:none;
width:80%;
margin-bottom:12px;
outline:none;
}

button{
padding:12px;
border:none;
border-radius:10px;
cursor:pointer;
font-weight:bold;
transition:0.2s;
}

button:hover{
transform:scale(1.05);
}

.scan{background:#22c55e;color:white;width:200px;}
.camera{background:#f59e0b;color:white;width:200px;margin-top:10px;}
.clear{background:#ef4444;color:white;margin-top:10px;width:200px;}

table{
width:100%;
border-collapse:collapse;
background:#111827;
border-radius:10px;
overflow:hidden;
}

th{
background:#2563eb;
padding:12px;
}

td{
padding:12px;
text-align:center;
border-bottom:1px solid #1f2937;
}

tr:hover{
background:#1f2937;
}

.total{
margin-top:15px;
font-size:26px;
font-weight:bold;
text-align:right;
color:#22c55e;
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
border-radius:10px;
overflow:hidden;
}

.modal button{
position:absolute;
bottom:20px;
left:50%;
transform:translateX(-50%);
background:#ef4444;
color:white;
}

</style>
</head>

<body>

<header>🛒 Punto de Venta</header>

<div class="main">

<div class="left">
<form action="/escanear" method="post">
<input id="codigo" name="codigo" placeholder="Escanear o escribir código" autofocus>
<button class="scan">Agregar producto</button>
</form>

<button class="camera" onclick="abrir()">📷 Escanear cámara</button>
<a href="/limpiar"><button class="clear">🗑 Limpiar carrito</button></a>
</div>

<div class="right">

<table>
<tr><th>Producto</th><th>Cantidad</th><th>Total</th></tr>

{% for p in carrito %}
<tr>
<td>{{p.nombre}}</td>
<td>{{p.cantidad}}</td>
<td>${{p.precio * p.cantidad}}</td>
</tr>
{% endfor %}

</table>

<div class="total">
Total: ${{total}}
</div>

</div>

</div>

<div id="modal" class="modal">
<div id="scanner"></div>
<button onclick="cerrar()">Cerrar cámara</button>
</div>

<script src="https://unpkg.com/@ericblade/quagga2/dist/quagga.min.js"></script>

<script>

let escaneando = false;

function abrir(){
if(escaneando) return;

escaneando = true;
document.getElementById("modal").style.display="block";

Quagga.init({
inputStream:{
type:"LiveStream",
target:document.querySelector('#scanner'),
constraints:{facingMode:"environment"}
},
decoder:{
readers:["ean_reader","code_128_reader"]
}
},function(err){
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
try{Quagga.stop();}catch(e){}
escaneando=false;
}

</script>

</body>
</html>
'''

@app.route("/")
def inicio():
    total = sum(p["precio"]*p["cantidad"] for p in carrito)
    return render_template_string(HTML, carrito=carrito, total=total)

@app.route("/escanear", methods=["POST"])
def escanear():
    codigo = request.form["codigo"]

    if codigo in productos:
        prod = productos[codigo]
    else:
        prod = {"nombre":"Producto "+codigo[-4:], "precio":50}

    for p in carrito:
        if p["codigo"] == codigo:
            p["cantidad"] += 1
            return redirect("/")

    carrito.append({
        "codigo":codigo,
        "nombre":prod["nombre"],
        "precio":prod["precio"],
        "cantidad":1
    })

    return redirect("/")

@app.route("/limpiar")
def limpiar():
    carrito.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
