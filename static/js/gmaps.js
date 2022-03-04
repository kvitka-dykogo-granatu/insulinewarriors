function initMap() {
    // The location of Uluru
    const kiev = { lat: 50.4021368, lng: 30.2525061 };
    
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 8,
      center: kiev,
    });

    data = [
      {latitude: 50.2021368, longitude: 30.3525061},
      {latitude: 50.3021368, longitude: 30.1525061}
    ];


    data.forEach(e => {
      marker = new google.maps.Marker({
      position: new google.maps.LatLng(e[`latitude`], e[`longitude`]),
      map: map,
      title: e[`address`],
  });
      google.maps.event.addListener(marker, 'click', (function (marker) {
          return function () {
              // infowindow.setContent(`State: ${e[`state`]<br>County: ${e[`location`]}<br>Address: ${e[`address`]}`);
              infowindow.setContent("marker");
              infowindow.open(map, marker);
          }
      })(marker));
  });


  }
