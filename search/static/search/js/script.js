
  		//initialize the leaflet map

  		

		console.log("bonjour");		
		var mymap = L.map('mapid').setView([51.505, -0.09], 13);


		L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibmFvbWllLWNvIiwiYSI6ImNrb2toNWxmcjE0bDMycXJtN3JyeWh5MTUifQ.qd_YdCTV7VRg3TkhvhsFVw', {
		    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		    maxZoom: 18,
		    id: 'mapbox/streets-v11',
		    tileSize: 512,
		    zoomOffset: -1,
		    accessToken: 'pk.eyJ1IjoibmFvbWllLWNvIiwiYSI6ImNrb2toNWxmcjE0bDMycXJtN3JyeWh5MTUifQ.qd_YdCTV7VRg3TkhvhsFVw'
		}).addTo(mymap);
