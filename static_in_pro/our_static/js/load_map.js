/**
 * Created by hannahpark on 15-11-13.
 */

var map;
var markers = []; // initialize markers
var lastInputtedCoordinate = null;
var allCoordinates = [];
var tempAllCoordinates = [];
var displayedCoordinates = [];

//clear old markers and make a map with a new one
function makeNewMarkerMap(pos, title){
    markers.forEach(function(marker) {
        marker.setMap(null);
    });
    markers = [];
    markers.push(new google.maps.Marker({
        position: pos,
        map: map,
        title: title
    }));
    map.setCenter(pos);
    map.setZoom(17);
    lastInputtedCoordinate = pos;
}

function initMap() {
    jQuery.getJSON('/coordwithid_test', function (data) {
        jQuery.each(data, function (index, value) {
            var myCoordinate = {lat: value.lat, lng: value.lng, key: value.key};
            allCoordinates.push(myCoordinate);
        });
    });
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 49.261226, lng: -123.1139271},
        zoom: 12
    });
    var input = document.getElementById('pac-input');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input); // places search bar inside map
    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map); // prioritizes nearby locations
    autocomplete.addListener('place_changed', function() {
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("Autocomplete's returned place contains no geometry");
            return;
        } else {
            makeNewMarkerMap(place.geometry.location, place.name);
        }
    });
}

function trackCurrentLocation(){
    if(navigator.geolocation) {
        browserSupportFlag = true;
        navigator.geolocation.getCurrentPosition(function(position) {
            var LatLng = {lat: position.coords.latitude,lng:position.coords.longitude};
            makeNewMarkerMap(LatLng, "Your Current Location");
        }, function() {
            handleNoGeolocation(browserSupportFlag);
        });
    }
    // Browser doesn't support Geolocation
    else {
        browserSupportFlag = false;
        handleNoGeolocation(browserSupportFlag);
    }
    function handleNoGeolocation(errorFlag) {
        if (errorFlag == true) {
            alert("Geolocation service failed.");
            initialLocation = vancouver;
        } else {
            alert("Your browser doesn't support geolocation. ");
            initialLocation = vancouver;
        }
        map.setCenter(initialLocation);
    }
}


/*
function testing() {
    jQuery.getJSON('/coordwithid_test', function (data) {
        jQuery.each(data, function (index, value) {
            var myLatLng = {lat: value.lat, lng: value.lng};
            var marker = new google.maps.Marker
            ({
                position: myLatLng,
                map: map,
                title: 'All coordinates from DB'
            });
        });
    });
}
*/

function doStuff() {
    tempAllCoordinates = allCoordinates.slice();
    if (lastInputtedCoordinate == null)
        alert("Please set a location!");
    for (var i = 0; i < 3; i++) {
        getClosestPoint(lastInputtedCoordinate, tempAllCoordinates);
    }
    alert(displayedCoordinates.length);
    jQuery.each(displayedCoordinates, function (index, value) {
        var myLatLng = {lat: value.lat, lng: value.lng};
        var marker = new google.maps.Marker
        ({
            position: myLatLng,
            map: map,
            title: value.key.toString()
        });
    });
}

function getClosestPoint(selectedLatLng, points) {
    var closestPoint = null;
    var distance = null;
    var tempDistance = null;

    jQuery.each(points, function(index, value) {
        tempDistance = getDistance(selectedLatLng, value);
        if (distance == null) {
            distance = tempDistance;
            closestPoint = value;
        }
        else if (tempDistance < distance) {
            distance = tempDistance;
            closestPoint = value;
        }
    });
    filterByKey(closestPoint.key);
}

function filterByKey(key) {
    for(var i = 0; i < tempAllCoordinates.length; i++){
        if (tempAllCoordinates[i].key == key){
            displayedCoordinates.push(tempAllCoordinates[i]);
            tempAllCoordinates.splice(i,1);
            i--;
        }
    }
    alert(displayedCoordinates.length);
    alert(tempAllCoordinates.length);
}

function getDistance(selectedLatLng, otherLatLng) {
    var lat1 = selectedLatLng.lat;
    var lng1 = selectedLatLng.lng;
    var lat2 = otherLatLng.lat;
    var lng2 = otherLatLng.lng;
    var sidea = Math.abs(lat1 - lat2);
    var sideb = Math.abs(lng1 - lng2);
    return (Math.sqrt(sidea*sidea+sideb*sideb));
}