var mymap = L.map('map').setView([22.7196, 75.8577], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(mymap);

mapMarkers1 = [];
routes = [];


var source = new EventSource('/topic/geodata');
source.addEventListener('message', function(e){

  console.log('Message');
  obj = JSON.parse(e.data);
  console.log(obj);

  // code for putting markers on geolocation(lat,long) 
  if(obj.busline == '00001') {
    for (var i = 0; i < mapMarkers1.length; i++) {
      mymap.removeLayer(mapMarkers1[i]);
      mymap.removeLayer(routes[i]);
    }
    marker1 = L.marker([obj.current.latitude, obj.current.longitude]).addTo(mymap);
    var polyline = L.polyline(obj.route,{
      weight: 3,
      color: 'red',
      opacity: 0.5
  })
    polyline.addTo(mymap);
    mapMarkers1.push(marker1);
    routes.push(polyline)
  }
}, false);