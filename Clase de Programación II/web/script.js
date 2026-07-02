document.addEventListener("DOMContentLoaded", function () {

    console.log("Sistema de Facturación cargado correctamente.");

    mostrarFecha();

    actualizarHora();

    setInterval(actualizarHora, 1000);

});

function mostrarFecha() {

    const fecha = new Date();

    const opciones = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric"
    };

    const elemento = document.getElementById("fecha");

    if (elemento) {
        elemento.textContent = fecha.toLocaleDateString("es-ES", opciones);
    }

}

function actualizarHora() {

    const hora = new Date();

    const elemento = document.getElementById("hora");

    if (elemento) {
        elemento.textContent = hora.toLocaleTimeString("es-ES");
    }

}

function abrirRepositorio() {

    const confirmar = confirm(
        "¿Desea abrir el repositorio del proyecto en GitHub?"
    );

    if (confirmar) {
        window.open(
            "https://github.com/TU_USUARIO/TU_REPOSITORIO",
            "_blank"
        );
    }

}

function volverArriba() {

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}

document.querySelectorAll('a[href^="#"]').forEach(function (enlace) {

    enlace.addEventListener("click", function (e) {

        e.preventDefault();

        const destino = document.querySelector(
            this.getAttribute("href")
        );

        if (destino) {

            destino.scrollIntoView({
                behavior: "smooth"
            });

        }

    });

});

function mostrarBienvenida() {

    alert("Bienvenido al Sistema de Facturación.");

}
