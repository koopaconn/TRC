var mousePositionControl = new ol.control.MousePosition({
  coordinateFormat: ol.coordinate.createStringXY(4),
  projection: 'EPSG:4326',
  className: 'custom-mouse-position',
  target: document.getElementById('mouse-position'),
  undefinedHTML: '&nbsp;',
  div: 'pos'
});

var styles = [
'RoadOnDemand',
'Aerial',
'AerialWithLabelsOnDemand',
'CanvasDark',
'OrdnanceSurvey'
];
var layers = [];
var i, ii;
for (i = 0, ii = styles.length; i < ii; ++i) {
layers.push(new ol.layer.Tile({
  visible: true,
  preload: Infinity,
  source: new ol.source.BingMaps({
    key: 'AnPQ1fbsTyHMacJNIMlC24CKcFU6Mt8mwFwsQG4Pvvp7iaILrWU0b4PWFiSPdomK',
    imagerySet: styles[i]
  })
}));
}

var centerpos = [-10527334, 4735743];

var map = new ol.Map({
controls: ol.control.defaults().extend([mousePositionControl]),
layers: layers,
target: 'map',
view: new ol.View({
  // projection: 'EPSG:4326',
  center: centerpos,
  zoom: 8
})
});


var select = document.getElementById('layer-select');
function onChange() {
  var style = select.value;
  for (var i = 0, ii = layers.length; i < ii; ++i) {
    layers[i].setVisible(styles[i] === style);
  }
}
select.addEventListener('change', onChange);
onChange();

// ************
// ************

var measurementRadios = $('[type=radio]');
var resultElement = $('#js-result');
var measuringTool;

var enableMeasuringTool = function() {
  map.removeInteraction(measuringTool);

  var geometryType = measurementRadios.filter(':checked').val();
  var html = geometryType === 'Polygon' ? '<sup>2</sup>' : '';

  measuringTool = new ol.interaction.Draw({
    type: geometryType,
    source: layers[0].getSource()
  });

  measuringTool.on('drawstart', function(event) {
    layers[0].getSource().clear();

    event.feature.on('change', function(event) {
      var measurement = geometryType === 'Polygon' ? event.target.getGeometry().getArea() : event.target.getGeometry().getLength();

      var measurementFormatted = measurement > 100 ? (measurement / 1000 * 0.621371).toFixed(2) + ' mi' : (measurement.toFixed(2)*3.28084) + ' ft';

      resultElement.html(measurementFormatted + html);
    });
  });

  map.addInteraction(measuringTool);
};

measurementRadios.on('change', enableMeasuringTool);

enableMeasuringTool();
