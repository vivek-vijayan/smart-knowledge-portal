// Create root and chart
var root = am5.Root.new("chartdiv");
var chart = root.container.children.push(
  am5map.MapChart.new(root, {
    panX: "rotateX",
    wheelY: "zoom",
    minZoomLevel: 1,
    maxZoomLevel: 1,
    panY: "rotateY",
    projection: am5map.geoOrthographic(),
  })
);

// Create polygon series
var polygonSeries = chart.series.push(
  am5map.MapPolygonSeries.new(root, {
    geoJSON: am5geodata_worldLow,
  })
);

var SercoLocations = {
  type: "FeatureCollection",
  features: [
    {
      type: "Feature",
      properties: {
        name: "North America",
      },
      geometry: {
        type: "Point",
        coordinates: [-107.489495, 56.826076],
      },
    },
    {
      type: "Feature",
      properties: {
        name: "United Kingdom",
      },
      geometry: {
        type: "Point",
        coordinates: [-2.372308, 53.983164],
      },
    },
    {
      type: "Feature",
      properties: {
        name: "Middle East",
      },
      geometry: {
        type: "Point",
        coordinates: [16.680295, 13.184333],
      },
    },
    {
      type: "Feature",
      properties: {
        name: "ASPAC Region",
      },
      geometry: {
        type: "Point",
        coordinates: [115.779242, 38.257686],
      },
    },
    {
      type: "Feature",
      properties: {
        name: "ASPAC Region",
      },
      geometry: {
        type: "Point",
        coordinates: [141.635299, -4.006842],
      },
    },
    {
      type: "Feature",
      properties: {
        name: "ASPAC Region",
      },
      geometry: {
        type: "Point",
        coordinates: [134.076705, -22.644527],
      },
    },
  ],
};

var sercoPointSeries = chart.series.push(
  am5map.MapPointSeries.new(root, {
    geoJSON: SercoLocations,
  })
);

sercoPointSeries.bullets.push(function () {
  var circle = am5.Circle.new(root, {
    radius: 10,
    fill: am5.color(0xff0000),
    tooltipText: "{name}",
  });

  circle.events.on("click", function (ev) {
    console.log(ev.target.dataItem);
  });

  return am5.Bullet.new(root, {
    sprite: circle,
  });
});


// CG
var CapgeminiLocation = {
    type: "FeatureCollection",
    features: [
      {
        type: "Feature",
        properties: {
          name: "Mumbai",
        },
        geometry: {
          type: "Point",
          coordinates: [ 73.217633, 19.069711],
        },
      },
      {
        type: "Feature",
        properties: {
          name: "Bangalore",
        },
        geometry: {
          type: "Point",
          coordinates: [ 77.832130, 13.082448],
        },
      },
      {
        type: "Feature",
        properties: {
          name: "Pune",
        },
        geometry: {
          type: "Point",
          coordinates: [74.157201, 18.622726],
        },
      },
      {
        type: "Feature",
        properties: {
          name: "Hyderabad",
        },
        geometry: {
          type: "Point",
          coordinates: [80.434690, 17.632116],
        },
      },
      
    ],
  };
  
  var capgeminiPointSeries = chart.series.push(
    am5map.MapPointSeries.new(root, {
      geoJSON: CapgeminiLocation,
    })
  );
  
  capgeminiPointSeries.bullets.push(function () {
    var circle = am5.Circle.new(root, {
      radius: 5,
      fill: am5.color("#004085"),
      tooltipText: "{name}",
    });
  
    circle.events.on("click", function (ev) {
      console.log(ev.target.dataItem);
    });
  
    return am5.Bullet.new(root, {
      sprite: circle,
    });
  });
  ///

var backgroundSeries = chart.series.unshift(
  am5map.MapPolygonSeries.new(root, {})
);

backgroundSeries.mapPolygons.template.setAll({
  fill: am5.color("#ffffff"),
  stroke: am5.color(0xd4f1f9),
});

backgroundSeries.data.push({
  geometry: am5map.getGeoRectangle(90, 180, -90, -180),
});

polygonSeries.mapPolygons.template.states.create("hover", {
  fill: am5.color("#ff0000"),
});
