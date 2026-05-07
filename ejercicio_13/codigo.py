from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "purple_store"

# =========================
# BASE DE DATOS SQLITE
# =========================
def get_db_connection():

    conn = sqlite3.connect("products.db")

    conn.row_factory = sqlite3.Row

    return conn

# =========================
# CREAR TABLA
# =========================
def init_db():

    conn = sqlite3.connect("products.db")

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS productos (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            id_proveedor TEXT NOT NULL,

            nombre_producto TEXT NOT NULL,

            codigo TEXT NOT NULL UNIQUE,

            num_producto INTEGER NOT NULL

        )

    """)

    conn.commit()

    conn.close()

# =========================
# HTML
# =========================
HTML = """

<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1">

<title>Purple Inventory Scanner</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{
font-family:Arial;
background:linear-gradient(
135deg,
#b8a4ff,
#cbb8ff,
#e2d7ff
);
color:white;
padding:20px;
overflow-x:hidden;
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
z-index:-1;
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

h1{
text-align:center;
margin-bottom:20px;
font-size:40px;
text-shadow:0 0 15px #b49cff;
}

.card{
background:rgba(255,255,255,0.15);
backdrop-filter:blur(10px);
padding:20px;
border-radius:25px;
margin-bottom:20px;
box-shadow:0 0 20px rgba(255,255,255,0.2);
}

input{
width:100%;
padding:14px;
border:none;
border-radius:15px;
margin-bottom:12px;
font-size:16px;
outline:none;
background:white;
color:#7c5cff;
font-weight:bold;
}

button{
padding:14px;
border:none;
border-radius:15px;
background:#9b7dff;
color:white;
font-weight:bold;
cursor:pointer;
transition:0.3s;
width:100%;
margin-top:5px;
}

button:hover{
transform:scale(1.03);
background:#b49cff;
}

table{
width:100%;
border-collapse:collapse;
margin-top:20px;
overflow:hidden;
border-radius:20px;
background:rgba(255,255,255,0.1);
}

th{
background:#9b7dff;
padding:15px;
}

td{
padding:15px;
text-align:center;
border-bottom:1px solid rgba(255,255,255,0.2);
}

tr:hover{
background:rgba(255,255,255,0.08);
}

.edit-form{
display:flex;
flex-direction:column;
gap:8px;
}

.small{
padding:10px;
font-size:14px;
}

.camera{
background:#b49cff;
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
width:100%;
height:80%;
overflow:hidden;
border-radius:20px;
}

.close{
position:absolute;
bottom:20px;
left:50%;
transform:translateX(-50%);
width:250px;
background:#7c5cff;
}

</style>

</head>

<body>

<div class="stars" id="stars"></div>

<h1>
✨ Purple Inventory Scanner ✨
</h1>

<div class="card">

<form action="/guardar" method="POST">

<input type="text"
name="id_proveedor"
placeholder="ID proveedor"
required>

<input type="text"
name="nombre_producto"
placeholder="Nombre producto"
required>

<input id="codigo"
type="text"
name="codigo"
placeholder="Código de barras"
required>

<button type="button"
class="camera"
onclick="abrir()">

📷 Escanear Código

</button>

<input type="number"
name="num_producto"
placeholder="Cantidad"
required>

<button>
Guardar Producto
</button>

</form>

</div>

<div class="card">

<table>

<tr>

<th>ID</th>
<th>Proveedor</th>
<th>Producto</th>
<th>Código</th>
<th>Cantidad</th>
<th>Editar</th>

</tr>

{% for p in productos %}

<tr>

<td>{{p.id}}</td>

<td>{{p.id_proveedor}}</td>

<td>{{p.nombre_producto}}</td>

<td>{{p.codigo}}</td>

<td>{{p.num_producto}}</td>

<td>

<form class="edit-form"
action="/editar/{{p.id}}"
method="POST">

<input class="small"
type="text"
name="nuevo_id_prov"
value="{{p.id_proveedor}}"
required>

<input class="small"
type="text"
name="nuevo_nombre"
value="{{p.nombre_producto}}"
required>

<input class="small"
type="text"
name="nuevo_codigo"
value="{{p.codigo}}"
required>

<input class="small"
type="number"
name="nueva_cantidad"
value="{{p.num_producto}}"
required>

<button class="small">
Actualizar
</button>

</form>

</td>

</tr>

{% endfor %}

</table>

</div>

<!-- MODAL CAMARA -->

<div id="modal" class="modal">

<div id="scanner"></div>

<button class="close"
onclick="cerrar()">

Cerrar Cámara

</button>

</div>

<!-- QUAGGA -->

<script src="https://unpkg.com/@ericblade/quagga2/dist/quagga.min.js"></script>

<script>

/* ESTRELLITAS */

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

/* CAMARA */

let escaneando = false;

function abrir(){

if(escaneando) return;

escaneando = true;

document.getElementById("modal").style.display = "block";

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

alert("Error al abrir cámara");

escaneando = false;

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

cerrar();

}

function cerrar(){

document.getElementById("modal").style.display = "none";

try{
Quagga.stop();
}catch(e){}

escaneando = false;

}

</script>

</body>
</html>

"""

# =========================
# INICIO
# =========================
@app.route("/")
def index():

    conn = get_db_connection()

    productos = conn.execute("""

        SELECT *
        FROM productos
        ORDER BY id DESC

    """).fetchall()

    conn.close()

    return render_template_string(
        HTML,
        productos=productos
    )

# =========================
# GUARDAR
# =========================
@app.route("/guardar", methods=["POST"])
def guardar():

    id_prov = request.form["id_proveedor"]

    nombre = request.form["nombre_producto"]

    codigo = request.form["codigo"]

    cantidad = int(
        request.form["num_producto"]
    )

    conn = get_db_connection()

    producto = conn.execute(

        "SELECT * FROM productos WHERE codigo=?",

        (codigo,)

    ).fetchone()

    # SI YA EXISTE
    if producto:

        total = producto["num_producto"] + cantidad

        conn.execute("""

            UPDATE productos

            SET num_producto=?

            WHERE codigo=?

        """,

        (total, codigo))

    # NUEVO PRODUCTO
    else:

        conn.execute("""

            INSERT INTO productos
            (
                id_proveedor,
                nombre_producto,
                codigo,
                num_producto
            )

            VALUES (?,?,?,?)

        """,

        (
            id_prov,
            nombre,
            codigo,
            cantidad
        ))

    conn.commit()

    conn.close()

    return redirect(url_for("index"))

# =========================
# EDITAR
# =========================
@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):

    id_prov = request.form["nuevo_id_prov"]

    nombre = request.form["nuevo_nombre"]

    codigo = request.form["nuevo_codigo"]

    cantidad = int(
        request.form["nueva_cantidad"]
    )

    conn = get_db_connection()

    conn.execute("""

        UPDATE productos

        SET

        id_proveedor=?,
        nombre_producto=?,
        codigo=?,
        num_producto=?

        WHERE id=?

    """,

    (
        id_prov,
        nombre,
        codigo,
        cantidad,
        id
    ))

    conn.commit()

    conn.close()

    return redirect(url_for("index"))

# =========================
# EJECUTAR
# =========================
if __name__ == "__main__":

    init_db()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
