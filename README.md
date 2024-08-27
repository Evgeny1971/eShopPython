# eShopPython

alert('currentLocation.lat()' + currentLocation.lat());
            alert('currentLocation.lng()' + currentLocation.lng());
            alert('targetLocation.lat' + targetLocation.lat);
            alert('targetLocation.lng' + targetLocation.lng);
            alert(google.maps.geometry.spherical.computeDistanceBetween(
                new google.maps.LatLng(currentLocation.lat(), currentLocation.lng()),
                new google.maps.LatLng(targetLocation.lat, targetLocation.lng)
            ));