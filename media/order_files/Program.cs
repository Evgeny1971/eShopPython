<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Maps Quest Demo</title>
    <style>
        /* Basic styling */
        body, html {
            height: 100%;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        #map {
            height: 80%;
            width: 100%;
        }
        #info {
            padding: 10px;
            text-align: center;
        }
        #status {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="info">
        <h2>Welcome to the Van Gogh Quest</h2>
        <p>Find the location of the "Sunflowers" painting in Amsterdam.</p>
        <button onclick="startQuest()">Start Quest</button>
        <div id="status"></div>
    </div>
    <div id="map"></div>

    <!-- Google Maps API -->
    <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBuImtLS1A2933QJOZ-ScwDVeEfDYF9aSw&libraries=places&callback=initMap"></script>

    <!-- Main JavaScript -->
    <script>
        let map;
        let targetLocation = { lat: 52.358, lng: 4.881 }; // Coordinates of Van Gogh Museum in Amsterdam

        function initMap() {
            map = new google.maps.Map(document.getElementById('map'), {
                center: { lat: 52.3676, lng: 4.9041 }, // Amsterdam center
                zoom: 14
            });
        }

        function startQuest() {
            const status = document.getElementById('status');
            status.innerText = "Navigate to the location of 'Sunflowers' painting.";

            map.addListener('center_changed', function () {
                checkLocation(map.getCenter());
            });
        }

        function checkLocation(currentLocation) {
            const distance = google.maps.geometry.spherical.computeDistanceBetween(
                new google.maps.LatLng(currentLocation.lat(), currentLocation.lng()),
                new google.maps.LatLng(targetLocation.lat, targetLocation.lng)
            );

            const status = document.getElementById('status');
            if (distance < 50) { // 50 meters tolerance
                status.innerText = "Bingo! You've found the 'Sunflowers'!";
                map.setZoom(18);
            } else {
                status.innerText = "Keep searching...";
            }
        }
    </script>
</body>
</html>

