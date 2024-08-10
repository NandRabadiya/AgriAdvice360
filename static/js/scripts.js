document.addEventListener('DOMContentLoaded', function() {
    const map = L.map('map').setView([20.5937, 78.9629], 5);  // Center map on India

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    let marker;

    map.on('click', function(e) {
        const lat = e.latlng.lat;
        const lng = e.latlng.lng;

        if (marker) {
            marker.setLatLng(e.latlng);
        } else {
            marker = L.marker(e.latlng).addTo(map);
        }

        document.getElementById('latitude').value = lat;
        document.getElementById('longitude').value = lng;
    });

    const stateSelect = document.getElementById('state');
    const stateCoords = {
        "Andaman and Nicobar Islands": [11.6230, 92.6626],
        "Andhra Pradesh": [15.9129, 79.7400],
        "Arunachal Pradesh": [27.1331, 93.6053],
        "Assam": [26.2006, 92.9376],
        "Bihar": [25.0961, 85.3131],
        "Chandigarh": [30.7333, 76.7794],
        "Chhattisgarh": [21.2787, 81.8661],
        "Dadra and Nagar Haveli and Daman and Diu": [20.3978, 79.6580],
        "Delhi": [28.6139, 77.2090],
        "Goa": [15.2993, 74.1240],
        "Gujarat": [22.2587, 71.1924],
        "Haryana": [29.0588, 76.0856],
        "Himachal Pradesh": [31.1048, 77.1734],
        "Jharkhand": [23.6102, 85.2799],
        "Karnataka": [15.3173, 75.7139],
        "Kerala": [10.8505, 76.2711],
        "Ladakh": [34.1526, 77.5771],
        "Lakshadweep": [10.5726, 72.6370],
        "Madhya Pradesh": [22.9734, 78.6569],
        "Maharashtra": [19.7515, 75.7139],
        "Manipur": [24.6637, 93.0356],
        "Meghalaya": [25.4670, 91.3662],
        "Mizoram": [23.1645, 92.9376],
        "Nagaland": [26.1584, 94.5624],
        "Odisha": [20.9517, 85.0985],
        "Puducherry": [11.9416, 79.8083],
        "Punjab": [31.1471, 75.3412],
        "Rajasthan": [27.0238, 74.2179],
        "Sikkim": [27.5330, 88.5126],
        "Tamil Nadu": [11.1271, 78.6569],
        "Telangana": [17.3616, 78.4747],
        "Tripura": [23.8478, 91.2867],
        "Uttar Pradesh": [26.8467, 80.9462],
        "Uttarakhand": [30.0668, 79.0193],
        "West Bengal": [22.9868, 87.8550]
    };

    stateSelect.addEventListener('change', function() {
        const coords = stateCoords[this.value];
        if (coords) {
            map.setView(coords, 7);
        }
    });
});
