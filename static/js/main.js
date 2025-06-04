// Obtener API de la raza del ganado.
const obtenerAPIRaza = async() => {
    try {
        const respuesta = await fetch("http://127.0.0.1:8000/dashboard/statistics/graph/race");
        return await respuesta.json();
    }
    catch (e) {
        alert(e);
    }
};

// Obtener API del sexo del ganado.
const obtenerAPISexo = async() => {
    try {
        const respuesta = await fetch("http://127.0.0.1:8000/dashboard/statistics/graph/sex");
        return await respuesta.json();
    }
    catch (e) {
        alert(e);
    }
};

// Obtener API del precio por kilogramo del ganado.
const obtenerAPIPrecioPorKilo = async() => {
    try {
        const respuesta = await fetch("http://127.0.0.1:8000/dashboard/statistics/graph/price-by-kg");
        return await respuesta.json();
    }
    catch (e) {
        alert(e);
    }
};

// Inicializar gráfica de la raza del ganado.
const inicializarGraficaRaza = async() => {
    const grafica = echarts.init(document.getElementById("chart"));
    grafica.setOption(await obtenerAPIRaza());
    grafica.resize();
};

// Inicializar gráfica del sexo del ganado.
const inicializarGraficaSexo = async() => {
    const grafica = echarts.init(document.getElementById("chart2"));
    grafica.setOption(await obtenerAPISexo());
    grafica.resize();
};

// Inicializar gráfica del precio por kilogramo del ganado.
const inicializarGraficaPrecioPorKilo = async() => {
    const grafica = echarts.init(document.getElementById("chart3"));
    grafica.setOption(await obtenerAPIPrecioPorKilo());
    grafica.resize();
};

// Cargar las gráficas.
window.addEventListener("load", async() => {
    await inicializarGraficaRaza();
    await inicializarGraficaSexo();
    await inicializarGraficaPrecioPorKilo();
});