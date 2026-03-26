from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta_2026"

USUARIO = "admin"
CONTRASENA = "admin2026"

# ================= LOGIN =================
LOGIN_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Login</title>
<style>
body {font-family: Arial; background:#f3f4f6; display:flex; justify-content:center; align-items:center; height:100vh;}
.card {background:white; padding:30px; border-radius:12px; width:300px; box-shadow:0 10px 25px rgba(0,0,0,0.1);}
input, button {width:100%; padding:10px; margin-top:10px;}
button {background:#2563eb; color:white; border:none; border-radius:6px;}
.error {color:red; text-align:center;}
</style>
</head>
<body>

<form class="card" method="post">
<h2>Login</h2>
<input type="text" name="usuario" placeholder="Usuario" required>
<input type="password" name="contrasena" placeholder="Contraseña" required>
<button type="submit">Entrar</button>
{% if error %}<p class="error">{{ error }}</p>{% endif %}
</form>

</body>
</html>
"""

# ================= MENU =================
MENU_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Menú</title>
<style>
body {font-family: Arial; background:#f3f4f6; margin:0; padding:20px;}
h1 {text-align:center;}

.logout {
position:absolute;
top:15px;
right:20px;
font-size:22px;
text-decoration:none;
}

.container {
display:flex;
justify-content:center;
gap:20px;
flex-wrap:wrap;
margin-top:40px;
}

.card {
background:white;
padding:20px;
width:220px;
border-radius:12px;
box-shadow:0 8px 20px rgba(0,0,0,0.1);
text-align:center;
}

.card a {
display:inline-block;
margin-top:10px;
padding:10px;
background:#2563eb;
color:white;
text-decoration:none;
border-radius:6px;
}
</style>
</head>
<body>

<a href="{{ url_for('logout') }}" class="logout">❌</a>

<h1>Menú Principal</h1>

<div class="container">

<div class="card">
<h3>Clasificar Número</h3>
<a href="/numero">Entrar</a>
</div>

<div class="card">
<h3>Categoría de Edad</h3>
<a href="/edad">Entrar</a>
</div>

<div class="card">
<h3>Calcular Tarifa</h3>
<a href="/tarifa">Entrar</a>
</div>

</div>

</body>
</html>
"""

# ================= VISTAS =================

NUMERO_HTML = """
<h2>Clasificar Número</h2>
<form method="post">
<input type="number" name="num" required>
<button>Clasificar</button>
</form>
<p>{{ res }}</p>
<a href="/menu">Volver</a>
"""

EDAD_HTML = """
<h2>Categoría de Edad</h2>
<form method="post">
<input type="number" name="edad" required>
<button>Evaluar</button>
</form>
<p>{{ res }}</p>
<a href="/menu">Volver</a>
"""

TARIFA_HTML = """
<h2>Calcular Tarifa</h2>
<form method="post">
<input type="number" name="monto" required>
<button>Calcular</button>
</form>
<p>{{ res }}</p>
<a href="/menu">Volver</a>
"""

# ================= RUTAS =================

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]

        if usuario == USUARIO and contrasena == CONTRASENA:
            session["autenticado"] = True
            return redirect(url_for("menu"))

        return render_template_string(LOGIN_HTML, error="Datos incorrectos")

    return render_template_string(LOGIN_HTML, error=None)


@app.route("/menu")
def menu():
    if not session.get("autenticado"):
        return redirect(url_for("login"))
    return render_template_string(MENU_HTML)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/numero", methods=["GET", "POST"])
def numero():
    res = ""
    if request.method == "POST":
        n = int(request.form["num"])
        if n > 0:
            res = "Positivo"
        elif n < 0:
            res = "Negativo"
        else:
            res = "Cero"
    return render_template_string(NUMERO_HTML, res=res)


@app.route("/edad", methods=["GET", "POST"])
def edad():
    res = ""
    if request.method == "POST":
        e = int(request.form["edad"])
        if e < 12:
            res = "Niño"
        elif e < 18:
            res = "Adolescente"
        elif e < 60:
            res = "Adulto"
        else:
            res = "Adulto mayor"
    return render_template_string(EDAD_HTML, res=res)


@app.route("/tarifa", methods=["GET", "POST"])
def tarifa():
    res = ""
    if request.method == "POST":
        m = float(request.form["monto"])
        if m > 1000:
            res = f"Total con descuento: {m*0.9}"
        else:
            res = f"Total: {m}"
    return render_template_string(TARIFA_HTML, res=res)


if __name__ == "__main__":
    app.run(debug=True)
