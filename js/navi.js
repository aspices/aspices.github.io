    
function closeNav() {
  document.getElementById("myNav").style.width = "0%";
  document.getElementById("example-two").style.visibility = "visible";
}

   
$(document).ready(function () {

  $('.navbar .dropdown-item').on('click', function (e) {
      var $el = $(this).children('.dropdown-toggle');
      var $parent = $el.offsetParent(".dropdown-menu");
      $(this).parent("li").toggleClass('open');

      if (!$parent.parent().hasClass('navbar-nav')) {
          if ($parent.hasClass('show')) {
              $parent.removeClass('show');
              $el.next().removeClass('show');
              $el.next().css({"top": -999, "left": -999});
          } else {
              $parent.parent().find('.show').removeClass('show');
              $parent.addClass('show');
              $el.next().addClass('show');
              $el.next().css({"top": $el[0].offsetTop, "left": $parent.outerWidth() - 4});
          }
          e.preventDefault();
          e.stopPropagation();
      }
  });

  $('.navbar .dropdown').on('hidden.bs.dropdown', function () {
      $(this).find('li.dropdown').removeClass('show open');
      $(this).find('ul.dropdown-menu').removeClass('show open');
  });
});


$(document).ready(function() {
  $(window).bind('scroll', function () {
      if ($(window).scrollTop() > 50) {
          $('.es_toplast_sec').addClass('position-fixed');
          $('.mobile_menu_bar').addClass('position-fixed');
          $('.mobile_menu_bar').addClass('full_width');
          
      } else {
          $('.es_toplast_sec').removeClass('position-fixed');
          $('.mobile_menu_bar').removeClass('position-fixed');
          $('.mobile_menu_bar').removeClass('full_width');
      }
  });
});


window.onload=function(){
  $('.dropdown').click(function(){
    $(this).siblings(".submenu").toggleClass('hide');
    });
  }

  $("#example-two").on("click", function() {
  var el = $(this);
  if (el.text() == el.data("text-swap")) {
  el.text(el.data("text-original"));
  document.getElementById("myNav").style.width = "0%";
  document.getElementById("myNav").style.visibility = "hidden";
  } else {
  el.data("text-original", el.text());
  el.text(el.data("text-swap"));
  document.getElementById("myNav").style.width = "100%";
  document.getElementById("myNav").style.height = "100%";
  document.getElementById("myNav").style.visibility = "visible";
  }
});


$('body').scrollspy({ target: '#navbar-example' })


