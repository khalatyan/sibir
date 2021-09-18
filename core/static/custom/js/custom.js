window.onscroll = function () {
    if (window.screen.width > 992) {
        if (document.documentElement.scrollTop > 150) {
            let headerTop = document.querySelector('.header-desktop')
            // headerTop.classList.add('shrinked', 'py-1')
            document.querySelector('.header-desktop').classList.add('shrinked')
            document.querySelector('.header-desktop').classList.remove('py-2')
        }
        else {
            let headerTop = document.querySelector('.header-desktop')
            // headerTop.classList.remove('shrinked', 'py-1')
            document.querySelector('.header-desktop').classList.remove('shrinked')
            document.querySelector('.header-desktop').classList.add('py-2')
        }
    }
}


$('img.lazyload').lazyload()
$('iframe.lazyload').lazyload()


function initGalleryImageGallery() {
    $('.gallery-image-list').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'Загрузка #%curr%...',
        gallery: {
            enabled: true,
            tPrev: 'Назад',
            tNext: 'Вперёд',
            tCounter: '<span class="mfp-counter">%curr% из %total%</span>',
            preload: [0, 1],
        },
        image: {
            tError: 'Не удалось загрузить изображение <a href="%url%">#%curr%</a>.',
            titleSrc: function(item) {
                return item.el.attr('title') + '<small>' + item.el.attr('description')  + '</small>';
            }
        }
    })
}

initGalleryImageGallery()


$(document).ready(function(){
    const slider = $("#slider_logo").owlCarousel({
        items: 1,
        loop:true,
        margin:35,
        nav:true,
        responsive:{
            0:{
                items:2
            },
            600:{
                items:2
            },
            1000:{
                items:4
            }
        }
    });
});

$(document).ready(function(){
    const slider = $("#services").owlCarousel({
        items: 1,
        loop:true,
        margin:35,
        nav:true,
        responsive:{
            0:{
                items:1
            }
        }
    });
});


jQuery(document).ready(function () {
   $( ".contact-form" ).submit(function( event ) {
      event.preventDefault();

      var orderform = $(this);
      var success = $(this).next();
      var ajaxloader = $(this).prev();
      var form_data = new FormData(orderform[0])

      ajaxloader.show();
      orderform.hide();

      $.ajax({
        type: "POST",
        url: "send_message_ajax/",
        dataType    : 'json',
        enctype: 'multipart/form-data',
        cache : false,
        processData: false,
        contentType: false,
        data: form_data,
        success: function (data) {
            if (data == 0) {
              ajaxloader.hide();
              orderform.show();
              success.html('<div class="alert-warning mt-2">  Пожалуйста, заполните все поля </div>').show('slow');
            } else {
              ajaxloader.hide();
              success.html('<div class="alert alert-default">Готово! Форма успешно отправлена. <br> В ближайшее время мы с Вами свяжемся.</div>').show('slow');
            }
        },
        error: function () {
          ajaxloader.hide();
          success.html('<div class="alert alert-warning mt-2">Нам не удалось отправить форму!</div>').show('slow');
      }
    });

    });

});


function addZero(num) {
  if (num & num.length < 2) {
    return '0' + num;
  }

  return num;
}
function setcookie(name, value, expires, path, domain, secure) {
	document.cookie =	name + "=" + escape(value) +
						((expires) ? "; expires=" + (new Date(expires)) : "") +
						((path) ? "; path=" + path : "") +
						((domain) ? "; domain=" + domain : "") +
						((secure) ? "; secure" : "");
}


function getcookie(name) {
	var cookie = " " + document.cookie;
	var search = " " + name + "=";
	var setStr = null;
	var offset = 0;
	var end = 0;

	if (cookie.length > 0)
	{
		offset = cookie.indexOf(search);

		if (offset != -1)
		{
			offset += search.length;
			end = cookie.indexOf(";", offset)

			if (end == -1)
			{
				end = cookie.length;
			}

			setStr = unescape(cookie.substring(offset, end));
		}
	}

	return(setStr);
}

var action_time = getcookie("action_time")

var now = new Date();

if (!action_time){
  var now = new Date();
  now.setMinutes(now.getHours() + 2272);
  setcookie('action_time', now, (new Date).getTime() + (6 * 30 * 24 * 60 * 60 * 1000));
  setcookie('action_time_year', now.getFullYear(), (new Date).getTime() + (6 * 30 * 24 * 60 * 60 * 1000));
  setcookie('action_time_month', now.getMonth(), (new Date).getTime() + (6 * 30 * 24 * 60 * 60 * 1000));
  setcookie('action_time_day', now.getDate(), (new Date).getTime() + (6 * 30 * 24 * 60 * 60 * 1000));
  setcookie('action_time_hour', now.getHours(), (new Date).getTime() + (6 * 30 * 24 * 60 * 60 * 1000));
  setcookie('action_time_minute', now.getMinutes(), (new Date).getTime() + (6 * 30 * 24 * 60 * 60 * 1000));
}

$('.countdown').downCount({
    date: addZero((Number(getcookie("action_time_month")) + 1).toString()) + '/' + addZero(getcookie("action_time_day")) +
      '/' + addZero(getcookie("action_time_year")) + ' ' + addZero(getcookie("action_time_hour")) +
      ':' + addZero(getcookie("action_time_minute")) + ':00',
    offset: +8
}, function () {
  $('#action_timer').addClass('d-none');
  $('#action-text').html('Оставьте заявку и получите скидку 5%!')
  $('input#action_input').val('Оставьте заявку и получите скидку 5%!');
});


function perexod(id) {
  var top = $("#" + id).offset().top; // получаем координаты блока
  $('body, html').animate({scrollTop: top - 70}, 800); // плавно переходим к блоку
}

function perexod_mob(id) {
  $('.navbar-toggler').addClass("collapsed");
  $('.navbar-collapse').removeClass("collapse");
  $('.navbar-collapse').addClass("collapsing");
  var top = $("#" + id).offset().top; // получаем координаты блока
  $('body, html').animate({scrollTop: top - 100}, 800); // плавно переходим к блоку
}

let sections = $('section'),
nav = $('nav'),
nav_height = nav.outerHeight();
$(window).on('scroll', function () {
    $('nav a').removeClass('active');
    let cur_pos = $(this).scrollTop();
    sections.each(function() {
        let top = $(this).offset().top - nav_height - 180,
        bottom = top + $(this).outerHeight();
        if (cur_pos >= top && cur_pos <= bottom) {
            nav.find('a').removeClass('active');
            sections.removeClass('active');
            $(this).addClass('active');
            nav.find('a[hreff="#'+$(this).attr('id')+'"]').addClass('active');
        }
    });
});
nav.find('a').on('click', function () {
    let $el = $(this),
    id = $el.attr('hreff');
    $('html, body').animate({
        scrollTop: $(id).offset().top - nav_height
    }, 600);
    return false;
});
