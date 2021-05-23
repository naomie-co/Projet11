
//initialize the leaflet map
var mymap = L.map('mapid');


function display_map(start_lat, start_long){
	//Map configuration
	console.log(start_lat, start_long);
	mymap.setView([start_lat, start_long], 7);

	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibmFvbWllLWNvIiwiYSI6ImNrb2toNWxmcjE0bDMycXJtN3JyeWh5MTUifQ.qd_YdCTV7VRg3TkhvhsFVw', {
	    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	    maxZoom: 18,
	    id: 'mapbox/streets-v11',
	    tileSize: 512,
	    zoomOffset: -1,
	    accessToken: 'pk.eyJ1IjoibmFvbWllLWNvIiwiYSI6ImNrb2toNWxmcjE0bDMycXJtN3JyeWh5MTUifQ.qd_YdCTV7VRg3TkhvhsFVw'
	}).addTo(mymap);	
}


function add_marker(latitude, longitude, name){
	//Creates a marker
	var marker = L.marker([latitude, longitude]).addTo(mymap.invalidateSize());
			    	
	//Add a pop-up when user clicks on a marker
	marker.bindPopup(name);

}

display_map(lat1, long1);

//add markers for each ccordinata
coordinates.forEach((item, index)=> {
	add_marker(item[0], item[1], item[2]);
})

