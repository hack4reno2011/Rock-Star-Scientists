markers = []

initialize = ->
  latlng = new google.maps.LatLng(39.51697, -119.81543)
  myOptions = 
    zoom: 14
    center: latlng
    mapTypeId: google.maps.MapTypeId.HYBRID
  
  map = new google.maps.Map(document.getElementById("map_canvas"), myOptions)
  
  google.maps.event.addListener map, 'click', ->
    console.log 'clicked' + ' ' + bounds
  
  google.maps.event.addListener map, 'rightclick', (event) ->
    console.log 'right clicked'
    console.log 'the current bounds are: ' + bounds.getNorthEast() + ',' + bounds.getSouthWest()
  
  google.maps.event.addListener map, 'dragstart', ->
    console.log 'started dragging'
  
  google.maps.event.addListener map, 'drag', ->
    console.log 'dragging'
  
  google.maps.event.addListener map, 'dragend', ->
    console.log 'endeddragging'  
  
    
    
  points =  [
  		{"county": "WASHOE", "id": "865", "latitude": 39.500010000000003, "longform": "237 LINDEN ST", "longitude": -119.79511100000001, "modified": "2011-10-15T16:07:44.891129", "municipality": "RENO", "number": 237, "number_suffix": "", "resource_uri": "/api/rawaddress/865/", "state": "NV", "street": "LINDEN", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "170", "latitude": 39.500048, "longform": "2250 KOLDEWEY DR", "longitude": -119.83842199999999, "modified": "2011-10-15T16:07:44.361850", "municipality": "RENO", "number": 2250, "number_suffix": "", "resource_uri": "/api/rawaddress/170/", "state": "NV", "street": "KOLDEWEY", "street_prefix": "", "street_suffix": "", "street_type": "DR", "unit": "", "zip4": null, "zip_code": 89509}, {"county": "WASHOE", "id": "581", "latitude": 39.500056999999998, "longform": "755 SKYLINE BLVD", "longitude": -119.822973, "modified": "2011-10-15T16:07:44.682045", "municipality": "RENO", "number": 755, "number_suffix": "", "resource_uri": "/api/rawaddress/581/", "state": "NV", "street": "SKYLINE", "street_prefix": "", "street_suffix": "", "street_type": "BLVD", "unit": "", "zip4": null, "zip_code": 89509}, {"county": "WASHOE", "id": "917", "latitude": 39.500179000000003, "longform": "2100 HELLABY LN", "longitude": -119.748543, "modified": "2011-10-15T16:07:44.928797", "municipality": "RENO", "number": 2100, "number_suffix": "", "resource_uri": "/api/rawaddress/917/", "state": "NV", "street": "HELLABY", "street_prefix": "", "street_suffix": "", "street_type": "LN", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "111", "latitude": 39.500342000000003, "longform": "2450 LYMBERY ST", "longitude": -119.80336800000001, "modified": "2011-10-15T16:07:44.310494", "municipality": "RENO", "number": 2450, "number_suffix": "", "resource_uri": "/api/rawaddress/111/", "state": "NV", "street": "LYMBERY", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89509}, {"county": "WASHOE", "id": "985", "latitude": 39.500391, "longform": "2450 LYMBERY ST", "longitude": -119.80327699999999, "modified": "2011-10-15T16:07:44.978934", "municipality": "RENO", "number": 2450, "number_suffix": "", "resource_uri": "/api/rawaddress/985/", "state": "NV", "street": "LYMBERY", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89509}, {"county": "WASHOE", "id": "283", "latitude": 39.500512999999998, "longform": "446 GROVE ST", "longitude": -119.791753, "modified": "2011-10-15T16:07:44.455240", "municipality": "RENO", "number": 446, "number_suffix": "", "resource_uri": "/api/rawaddress/283/", "state": "NV", "street": "GROVE", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "337", "latitude": 39.500753000000003, "longform": "2450 LYMBERY ST", "longitude": -119.803192, "modified": "2011-10-15T16:07:44.494153", "municipality": "RENO", "number": 2450, "number_suffix": "", "resource_uri": "/api/rawaddress/337/", "state": "NV", "street": "LYMBERY", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89509}, {"county": "WASHOE", "id": "443", "latitude": 39.500852000000002, "longform": "2450 LYMBERY ST", "longitude": -119.803129, "modified": "2011-10-15T16:07:44.571248", "municipality": "RENO", "number": 2450, "number_suffix": "", "resource_uri": "/api/rawaddress/443/", "state": "NV", "street": "LYMBERY", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89509}, {"county": "WASHOE", "id": "340", "latitude": 39.501058, "longform": "197 GROVE ST", "longitude": -119.79668700000001, "modified": "2011-10-15T16:07:44.496377", "municipality": "RENO", "number": 197, "number_suffix": "", "resource_uri": "/api/rawaddress/340/", "state": "NV", "street": "GROVE", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "715", "latitude": 39.501067999999997, "longform": "175 GROVE ST", "longitude": -119.796913, "modified": "2011-10-15T16:07:44.781609", "municipality": "RENO", "number": 175, "number_suffix": "", "resource_uri": "/api/rawaddress/715/", "state": "NV", "street": "GROVE", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "716", "latitude": 39.501067999999997, "longform": "175 GROVE ST", "longitude": -119.796913, "modified": "2011-10-15T16:07:44.782336", "municipality": "RENO", "number": 175, "number_suffix": "", "resource_uri": "/api/rawaddress/716/", "state": "NV", "street": "GROVE", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "855", "latitude": 39.501159000000001, "longform": "2490 WRONDEL WAY", "longitude": -119.795981, "modified": "2011-10-15T16:07:44.883872", "municipality": "RENO", "number": 2490, "number_suffix": "", "resource_uri": "/api/rawaddress/855/", "state": "NV", "street": "WRONDEL", "street_prefix": "", "street_suffix": "", "street_type": "WAY", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "285", "latitude": 39.501289, "longform": "2305 KIETZKE LN", "longitude": -119.78942600000001, "modified": "2011-10-15T16:07:44.456705", "municipality": "RENO", "number": 2305, "number_suffix": "", "resource_uri": "/api/rawaddress/285/", "state": "NV", "street": "KIETZKE", "street_prefix": "", "street_suffix": "", "street_type": "LN", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "503", "latitude": 39.501356999999999, "longform": "2305 KIETZKE LN", "longitude": -119.790324, "modified": "2011-10-15T16:07:44.616353", "municipality": "RENO", "number": 2305, "number_suffix": "", "resource_uri": "/api/rawaddress/503/", "state": "NV", "street": "KIETZKE", "street_prefix": "", "street_suffix": "", "street_type": "LN", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "102", "latitude": 39.501358000000003, "longform": "197 GROVE ST", "longitude": -119.79678199999999, "modified": "2011-10-15T16:07:44.302709", "municipality": "RENO", "number": 197, "number_suffix": "", "resource_uri": "/api/rawaddress/102/", "state": "NV", "street": "GROVE", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "108", "latitude": 39.501358000000003, "longform": "175 GROVE ST", "longitude": -119.797172, "modified": "2011-10-15T16:07:44.307937", "municipality": "RENO", "number": 175, "number_suffix": "", "resource_uri": "/api/rawaddress/108/", "state": "NV", "street": "GROVE", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "452", "latitude": 39.501368999999997, "longform": "197 GROVE ST", "longitude": -119.79668700000001, "modified": "2011-10-15T16:07:44.578837", "municipality": "RENO", "number": 197, "number_suffix": "", "resource_uri": "/api/rawaddress/452/", "state": "NV", "street": "GROVE", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "539", "latitude": 39.501372000000003, "longform": "685 GROVE ST", "longitude": -119.78645899999999, "modified": "2011-10-15T16:07:44.644958", "municipality": "RENO", "number": 685, "number_suffix": "", "resource_uri": "/api/rawaddress/539/", "state": "NV", "street": "GROVE", "street_prefix": "", "street_suffix": "", "street_type": "ST", "unit": "", "zip4": null, "zip_code": 89502}, {"county": "WASHOE", "id": "540", "latitude": 39.501410999999997, "longform": "2305 KIETZKE LN", "longitude": -119.790324, "modified": "2011-10-15T16:07:44.645891", "municipality": "RENO", "number": 2305, "number_suffix": "", "resource_uri": "/api/rawaddress/540/", "state": "NV", "street": "KIETZKE", "street_prefix": "", "street_suffix": "", "street_type": "LN", "unit": "", "zip4": null, "zip_code": 89502}]
      
  bounds = new google.maps.LatLngBounds()
  
  addMarker = (location) ->
    console.log 'adding a marker at: ' + location.longform
    position = new google.maps.LatLng(location.latitude,location.longitude)
    console.log position.lat + ' ' + position.lng
    marker = new google.maps.Marker( 
      title: location.longform
      content: location.longform
      position: position
      map: map
      draggable: false
      raiseOnDrag: true
    bounds.extend position    
    )
    google.maps.event.addListener marker, 'click', ->
      console.log 'marker clicked'
      closeInfos()
      info = new google.maps.InfoWindow(content: @content)
      info.open map, this
      infos[0] = info
      
    closeInfos = ->
      if infos.length > 0
        infos[0].set 'marker', null
        infos[0].close
        infos.length = 0
    
  (addMarker x for x in points)
  
  
  #enable code below to fit to bounds
  #map.fitBounds bounds
  
infos = []



  
    