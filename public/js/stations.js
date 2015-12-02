$(document).ready(function(){

  $.ajax({url: "/stations",
    success : function(json){
      loadStations(json);
    }
  });

  $('#calculate-distance').click(function(){

    var from = $("input[name=from]:checked").val();
    var to = $("input[name=to]:checked").val();

    console.log("Searching distance from " + from + " to " + to);
    if (from && to ) {
      duration(from,to);
    } else {
      console.error('Must select from and to destination');
    }
  })
});

var duration = function(from,to){
  $.ajax({url: "/duration/latlon",
    data: {
      from: from,
      to: to
    },
    success : function(json){
      console.log(json);
      alert("Duration: "+ json.duration);
    }
  });
};

var loadStations = function(stations){
  console.log("Loading " + stations.length+ " stations");
  var template = $('#stations-template').html();
   Mustache.parse(template);
   var rendered = Mustache.render(template, stations);

   console.log("Rendered " + rendered);
   $("#stations").html(rendered);
};