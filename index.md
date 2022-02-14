---
Title: Washington State Birding Site Impressions
---

A site dedicated to keeping track of impressions about various birding locations.

## Map
 
Locations
<style>
  #map {
   height: 400px;
   width: 100%;
   overflow: hidden;
   float: left;
   border: thin solid #333;
   }
</style>
<div id="map"></div>
<div id="capture"></div>
<script>
  var map;
  var src = 'https://jalangle.github.io/wabirding/sites.kml';

  function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
      center: new google.maps.LatLng(47.601927, -122.338229),
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
src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCVeQCLZtsZYDKOPqtX7tkNII3qYjPiNME&callback=initMap">
</script>

## Sites

{% for birding_site in site.sites %}
### [{{birding_site.Title}}]({{site.baseurl}}{{birding_site.url}})

{% endfor %}

## Meta
[Repository]({{site.github.repository_url}}) at [Build Revision]({{site.github.repository_url}}/commit/{{site.github.build_revision}})