$(document).ready(function(){
  if ($('#id_consistantBlock').val()=='True') {
    $("#roadwayWrapper").show()
    $("#shoulderWrapper").show()
    $("#consistency").show()
    $("#id_consistantBlock").prop("checked", true)
  };
  if ($('#id_consistantBlock').val()=='False') {
    $("#roadwayWrapper").hide()
    $("#shoulderWrapper").hide()
    $("#consistency").hide()
    $("#id_consistantBlock").prop("checked", false)
  };
});

$(document).ready(function(){
    $('input[type="checkbox"]').click(function(){
      if ($('#id_consistantBlock').is(':checked')) {
        $("#roadwayWrapper").show()
        $("#shoulderWrapper").show()
        $("#consistency").show()
      }
      if ($('#id_consistantBlock').is(':checked')==false) {
        $("#roadwayWrapper").hide()
        $("#shoulderWrapper").hide()
        $("#consistency").hide()
      }
    });
});

$( document ).ready(function() {
  $(".alert").fadeOut(3000);
});

$(document).ready(function() {
  $('li.active').removeClass('active');
  $('a[href="' + location.pathname + '"]').closest('li').addClass('active');
});

$(document).ready(function() {
    $("#Get").click(function(){
      var newCoords = $('#coordtext').val();
      var newCoordsArray = newCoords.split(/[\s,]+/,2);
      var newCoordsArrayConv = ol.proj.transform(newCoordsArray, 'EPSG:4326', 'EPSG:3857');
      console.log(newCoordsArrayConv);
      map.getView().setCenter(newCoordsArrayConv)
    });
});

$(document).ready(function() {
    $(".trigger_popup_fricc").click(function(){
       $('.hover_bkgr_fricc').show();
    });
    $('.hover_bkgr_fricc').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
    $('.popupCloseButton').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
});
