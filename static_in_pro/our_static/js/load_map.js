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
            var LatLng = {lat: place.geometry.location.lat(),lng:place.geometry.location.lng()};
            makeNewMarkerMap(LatLng, place.name);
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

function findThreeRoutes() {
    tempAllCoordinates = allCoordinates.slice();
    if (lastInputtedCoordinate == null)
        alert("Please set a location!");
    for (var i = 0; i < 1; i++) {
        getClosestPoint(lastInputtedCoordinate, tempAllCoordinates);
    }
    jQuery.each(displayedCoordinates, function (index, value) {
        var myLatLng = {lat: value.lat, lng: value.lng};
        var marker = new google.maps.Marker
        ({
            position: myLatLng,
            map: map,
            title: value.key.toString()
        });
    });
    map.setZoom(12);
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




var tc = [];

function test() {
    //filter so you dont have keys
    jQuery.each(displayedCoordinates, function (index, value) {
        var testCoordinate = {lat: value.lat, lng: value.lng};
        tc.push(testCoordinate);
    });

    var testCoordinates = [];
    for (var x = 0; x < (tc.length/2); x++){
        testCoordinates.push(tc[x]);
    }


    //find closestpoints and draw
    //for(var i = 0; i < testCoordinates.length; i++){
    var eCoords = [];
    var sCoord = lastInputtedCoordinate;

    for (var i = 0; i < 13; i++) {
        //alert(JSON.stringify(sCoord));
        var cPoint = getTestClosest(sCoord, testCoordinates);
        //alert(JSON.stringify(cPoint));
        eCoords.push(cPoint);
        //alert(JSON.stringify(eCoords[i]));
        //alert(JSON.stringify(testCoordinates.length));

        for(var j = 0; j < testCoordinates.length; j++){
            if(cPoint == testCoordinates[j]){ //This gets rid of duplicates...for now


                //alert(JSON.stringify(testCoordinates[j]));
                testCoordinates.splice(j, 1);
                j--;
            }
        }
        alert(JSON.stringify(testCoordinates.length));

        sCoord = cPoint;
        cPoint = null;


        //testCoordinates.splice(i, 1);
        //i--;
    }



    var flightPath = new google.maps.Polyline({
        path: eCoords,
        geodesic: true,
        strokeColor: '#FF0000',
        strokeOpacity: 1.0,
        strokeWeight: 2
    });

    flightPath.setMap(map);
    testCoordinates = [];


    function getTestClosest(selectedLatLng, points) {
        var closestPoint = null;
        var distance = null;
        var tempDistance = null;

        jQuery.each(points, function (index, value) {
            tempDistance = getDistance(selectedLatLng, value);
            if (distance == null) {
                distance = tempDistance;
                closestPoint = value;
            }
            else if (tempDistance < distance && distance != 0) {
                distance = tempDistance;
                closestPoint = value;
            }
        });
        return closestPoint;
    }

    //  var flightPlanCoordinates = [
    //  {lat: 37.772, lng: -122.214},
    //  {lat: 37.772, lng: -122.214},
    //  {lat: 37.772, lng: -122.214},
    //  {lat: 37.772, lng: -122.214}
    //];
    //
    //  for(var j = 0; j < flightPlanCoordinates.length; j++){
    //          if({lat: 37.772, lng: -122.214}.toString() == flightPlanCoordinates[j].toString()){
    //
    //              alert(JSON.stringify(flightPlanCoordinates[j]));
    //              flightPlanCoordinates.splice(j, 1);
    //              j--;
    //          }
    //      }
    //  alert(JSON.stringify(flightPlanCoordinates));
    //
    //
    //  //
    //  //var ss = [];
    //  //
    //  // jQuery.each(flightPlanCoordinates, function (index, value) {
    //  //    var s = {lat: value.lat, lng: value.lng};
    //  //    ss.push(s);
    //  //});


}



