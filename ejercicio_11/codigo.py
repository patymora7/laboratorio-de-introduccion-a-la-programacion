from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Scanner Neon</title>

<script src="https://unpkg.com/@zxing/library@latest"></script>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg,#0f172a,#020617);
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    color:white;
}

.container{
    width:95%;
    max-width:420px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border:1px solid rgba(255,255,255,0.1);
    border-radius:25px;
    padding:25px;
    text-align:center;
    box-shadow:0 0 30px rgba(0,255,170,0.2);
}

h1{
    font-size:28px;
    margin-bottom:10px;
    color:#00ffaa;
}

.sub{
    color:#94a3b8;
    margin-bottom:20px;
    font-size:14px;
}

.video-box{
    position:relative;
    border-radius:20px;
    overflow:hidden;
    border:2px solid #00ffaa;
    box-shadow:0 0 20px rgba(0,255,170,0.5);
}

video{
    width:100%;
    display:block;
}

.scan-line{
    position:absolute;
    width:100%;
    height:3px;
    background:#00ffaa;
    box-shadow:0 0 15px #00ffaa;
    animation:scan 2s linear infinite;
}

@keyframes scan{
    0%{
        top:0;
    }
    100%{
        top:100%;
    }
}

.resultado{
    margin-top:20px;
    padding:15px;
    border-radius:15px;
    background:#111827;
    border:1px solid rgba(0,255,170,0.3);
    color:#00ffaa;
    font-size:17px;
    word-wrap:break-word;
    min-height:70px;
}

.btn{
    margin-top:18px;
    padding:12px 20px;
    border:none;
    border-radius:12px;
    background:#00ffaa;
    color:black;
    font-weight:bold;
    cursor:pointer;
    transition:0.3s;
}

.btn:hover{
    transform:scale(1.05);
    box-shadow:0 0 15px #00ffaa;
}

.footer{
    margin-top:18px;
    color:#64748b;
    font-size:12px;
}

</style>
</head>

<body>

<div class="container">

    <h1>Scanner Neon</h1>
    <div class="sub">
        Escanea QR y códigos de barras
    </div>

    <div class="video-box">
        <div class="scan-line"></div>
        <video id="video" autoplay playsinline></video>
    </div>

    <div class="resultado" id="resultado">
        Iniciando cámara...
    </div>

    <button class="btn" onclick="reiniciar()">
        Reiniciar escáner
    </button>

    <div class="footer">
        Flask + ZXing
    </div>

</div>

<script>

const codeReader = new ZXing.BrowserMultiFormatReader();
const video = document.getElementById("video");
const resultado = document.getElementById("resultado");

let lastResult = "";

async function iniciar(){

    try{

        await codeReader.decodeFromConstraints(
            {
                video:{
                    facingMode:{ ideal:"environment" }
                }
            },
            video,
            (result, err) => {

                if(result){

                    if(result.text !== lastResult){

                        lastResult = result.text;

                        resultado.innerHTML = `
                            <b>Resultado:</b><br><br>
                            ${result.text}
                        `;

                        new Audio(
                            "https://actions.google.com/sounds/v1/cartoon/clang_and_wobble.ogg"
                        ).play();

                        if(result.text.startsWith("http")){

                            setTimeout(()=>{
                                window.open(result.text,"_blank");
                            },800);

                        }

                    }

                }

                if(err && !(err instanceof ZXing.NotFoundException)){
                    console.error(err);
                }

            }
        );

    }catch(error){

        resultado.innerHTML = "❌ No se pudo acceder a la cámara";
        console.error(error);

    }

}

function reiniciar(){
    lastResult = "";
    resultado.innerHTML = "Escaneando...";
}

iniciar();

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
