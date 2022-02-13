---
---

# Impressions of Washington State Birding Locations


# Map
    <div id="map"></div>
    <div id="capture"></div>
    <script>
      var map;
      var src = 'https://developers.google.com/maps/documentation/javascript/examples/kml/westcampus.kml';

      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: new google.maps.LatLng(-19.257753, 146.823688),
          zoom: 2,
          mapTypeId: 'terrain'
        });

        var kmlLayer = new google.maps.KmlLayer(src, {
          suppressInfoWindows: true,
          preserveViewport: false,
          map: map
        });
        kmlLayer.addListener('click', function(event) {
          var content = event.featureData.infoWindowHtml;
          var testimonial = document.getElementById('capture');
          testimonial.innerHTML = content;
        });
      }
    </script>
    <script async
    src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
    </script>


# Meta
Repository: {{ site.github.repository_url }}
Build Revision: {{ site.github.build_revision }}