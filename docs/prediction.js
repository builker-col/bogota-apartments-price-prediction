document.getElementById('predictionForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    fetch('https://bogota-apartments-predict.onrender.com/chapinero/predict', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            const formattedPrediction = formatNumberWithCommas(parseInt(data.prediction));
            document.getElementById('predictionResult').innerText = `Precio de venta aproximado: $${formattedPrediction} COP`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

// Función para formatear el número con separadores de miles
function formatNumberWithCommas(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}