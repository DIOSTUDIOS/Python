(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
'use strict';

(function ($) {
    "use strict";

    /* slim menu 最新最全最好的Bootstrap模板：http://www.bootstrapmb.com*/

    if ('.slimmenu'.length > 0) {
        $('.slimmenu').slimmenu({
            resizeWidth: '991',
            collapserTitle: 'Main Menu',
            animSpeed: 'medium',
            indentChildren: true
        });
    }

    /* sticky header */

    function fixed_top_menu() {

        var windows = $(window);

        windows.on("scroll", function () {

            var header_height = $(".header-area").height();

            var scrollTop = windows.scrollTop();

            if (scrollTop > header_height) {

                $(".header-area").addClass("sticky");
            } else {

                $(".header-area").removeClass("sticky");
            }
        });
    }

    fixed_top_menu();

    /* Testimonial-Slider */

    if ('.testimonial-slider'.length > 0) {
        $(".testimonial-slider").owlCarousel({
            autoplay: true,
            dots: false,
            loop: true,
            margin: 30,
            lazyLoad: true,
            center: true,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 2
                },
                1200: {
                    items: 3
                }
            }
        });
    }

    /*  Custom multi js*/

    if (".custom-multi-select".length > 0) {
        $('.custom-multi-select').select2();
    }

    /*  magnificPopup */

    $('.video-play').magnificPopup({
        type: 'iframe'
    });

    /*  Preloader js*/

    $(window).on('load', function () {

        var preLoder = $("#preloader");
        preLoder.fadeOut(1000);
    });

    /* highlight js */

    if ('pre code'.length > 0) {
        document.querySelectorAll('pre code').forEach(function (block) {
            hljs.highlightBlock(block);
        });
    }

    /*  AOS animation*/

    AOS.init({
        once: true

    });
})(jQuery);

},{}]},{},[1])
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIm5vZGVfbW9kdWxlcy9icm93c2VyLXBhY2svX3ByZWx1ZGUuanMiLCJzcmMvanMvYXBwLmpzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7QUNBQyxXQUFTLENBQVQsRUFBWTtBQUNUOztBQUdBOztBQUVBLFFBQUssV0FBRCxDQUFjLE1BQWQsR0FBdUIsQ0FBM0IsRUFBOEI7QUFDMUIsVUFBRSxXQUFGLEVBQWUsUUFBZixDQUF3QjtBQUNwQix5QkFBYSxLQURPO0FBRXBCLDRCQUFnQixXQUZJO0FBR3BCLHVCQUFXLFFBSFM7QUFJcEIsNEJBQWdCO0FBSkksU0FBeEI7QUFRSDs7QUFFRDs7QUFFQSxhQUFTLGNBQVQsR0FBMEI7O0FBRXRCLFlBQUksVUFBVSxFQUFFLE1BQUYsQ0FBZDs7QUFFQSxnQkFBUSxFQUFSLENBQVcsUUFBWCxFQUFxQixZQUFXOztBQUU1QixnQkFBSSxnQkFBZ0IsRUFBRSxjQUFGLEVBQWtCLE1BQWxCLEVBQXBCOztBQUVBLGdCQUFJLFlBQVksUUFBUSxTQUFSLEVBQWhCOztBQUVBLGdCQUFJLFlBQVksYUFBaEIsRUFBK0I7O0FBRTNCLGtCQUFFLGNBQUYsRUFBa0IsUUFBbEIsQ0FBMkIsUUFBM0I7QUFFSCxhQUpELE1BSU87O0FBRUgsa0JBQUUsY0FBRixFQUFrQixXQUFsQixDQUE4QixRQUE5QjtBQUVIO0FBQ0osU0FmRDtBQWlCSDs7QUFFRDs7QUFFQTs7QUFFQSxRQUFLLHFCQUFELENBQXdCLE1BQXhCLEdBQWlDLENBQXJDLEVBQXdDO0FBQ3BDLFVBQUUscUJBQUYsRUFBeUIsV0FBekIsQ0FBcUM7QUFDakMsc0JBQVUsSUFEdUI7QUFFakMsa0JBQU0sS0FGMkI7QUFHakMsa0JBQU0sSUFIMkI7QUFJakMsb0JBQVEsRUFKeUI7QUFLakMsc0JBQVUsSUFMdUI7QUFNakMsb0JBQVEsSUFOeUI7QUFPakMsd0JBQVk7QUFDUixtQkFBRztBQUNDLDJCQUFPO0FBRFIsaUJBREs7QUFJUixxQkFBSztBQUNELDJCQUFPO0FBRE4saUJBSkc7QUFPUixzQkFBTTtBQUNGLDJCQUFPO0FBREw7QUFQRTtBQVBxQixTQUFyQztBQW1CSDs7QUFHRDs7QUFFQSxRQUFLLHNCQUFELENBQXlCLE1BQXpCLEdBQWtDLENBQXRDLEVBQXlDO0FBQ3JDLFVBQUUsc0JBQUYsRUFBMEIsT0FBMUI7QUFFSDs7QUFFRDs7QUFFQSxNQUFFLGFBQUYsRUFBaUIsYUFBakIsQ0FBK0I7QUFDM0IsY0FBTTtBQURxQixLQUEvQjs7QUFJSDs7QUFFRyxNQUFFLE1BQUYsRUFBVSxFQUFWLENBQWEsTUFBYixFQUFxQixZQUFXOztBQUU1QixZQUFJLFdBQVcsRUFBRSxZQUFGLENBQWY7QUFDQSxpQkFBUyxPQUFULENBQWlCLElBQWpCO0FBRUgsS0FMRDs7QUFPQTs7QUFFQSxRQUFLLFVBQUQsQ0FBYSxNQUFiLEdBQXNCLENBQTFCLEVBQTZCO0FBQ3pCLGlCQUFTLGdCQUFULENBQTBCLFVBQTFCLEVBQXNDLE9BQXRDLENBQThDLFVBQUMsS0FBRCxFQUFXO0FBQ3JELGlCQUFLLGNBQUwsQ0FBb0IsS0FBcEI7QUFDSCxTQUZEO0FBR0g7O0FBRUQ7O0FBRUEsUUFBSSxJQUFKLENBQVM7QUFDTCxjQUFNOztBQURELEtBQVQ7QUFNSCxDQTNHQSxFQTJHQyxNQTNHRCxDQUFEIiwiZmlsZSI6ImdlbmVyYXRlZC5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzQ29udGVudCI6WyIoZnVuY3Rpb24oKXtmdW5jdGlvbiByKGUsbix0KXtmdW5jdGlvbiBvKGksZil7aWYoIW5baV0pe2lmKCFlW2ldKXt2YXIgYz1cImZ1bmN0aW9uXCI9PXR5cGVvZiByZXF1aXJlJiZyZXF1aXJlO2lmKCFmJiZjKXJldHVybiBjKGksITApO2lmKHUpcmV0dXJuIHUoaSwhMCk7dmFyIGE9bmV3IEVycm9yKFwiQ2Fubm90IGZpbmQgbW9kdWxlICdcIitpK1wiJ1wiKTt0aHJvdyBhLmNvZGU9XCJNT0RVTEVfTk9UX0ZPVU5EXCIsYX12YXIgcD1uW2ldPXtleHBvcnRzOnt9fTtlW2ldWzBdLmNhbGwocC5leHBvcnRzLGZ1bmN0aW9uKHIpe3ZhciBuPWVbaV1bMV1bcl07cmV0dXJuIG8obnx8cil9LHAscC5leHBvcnRzLHIsZSxuLHQpfXJldHVybiBuW2ldLmV4cG9ydHN9Zm9yKHZhciB1PVwiZnVuY3Rpb25cIj09dHlwZW9mIHJlcXVpcmUmJnJlcXVpcmUsaT0wO2k8dC5sZW5ndGg7aSsrKW8odFtpXSk7cmV0dXJuIG99cmV0dXJuIHJ9KSgpIiwiKGZ1bmN0aW9uKCQpIHtcclxuICAgIFwidXNlIHN0cmljdFwiO1xyXG5cdFxyXG5cdFxyXG4gICAgLyogc2xpbSBtZW51ICovXHJcblx0XHJcbiAgICBpZiAoKCcuc2xpbW1lbnUnKS5sZW5ndGggPiAwKSB7XHJcbiAgICAgICAgJCgnLnNsaW1tZW51Jykuc2xpbW1lbnUoe1xyXG4gICAgICAgICAgICByZXNpemVXaWR0aDogJzk5MScsXHJcbiAgICAgICAgICAgIGNvbGxhcHNlclRpdGxlOiAnTWFpbiBNZW51JyxcclxuICAgICAgICAgICAgYW5pbVNwZWVkOiAnbWVkaXVtJyxcclxuICAgICAgICAgICAgaW5kZW50Q2hpbGRyZW46IHRydWUsXHJcbiAgICAgICAgfSk7XHJcblxyXG5cclxuICAgIH1cclxuXHJcbiAgICAvKiBzdGlja3kgaGVhZGVyICovXHJcblxyXG4gICAgZnVuY3Rpb24gZml4ZWRfdG9wX21lbnUoKSB7XHJcblxyXG4gICAgICAgIHZhciB3aW5kb3dzID0gJCh3aW5kb3cpO1xyXG5cclxuICAgICAgICB3aW5kb3dzLm9uKFwic2Nyb2xsXCIsIGZ1bmN0aW9uKCkge1xyXG5cclxuICAgICAgICAgICAgdmFyIGhlYWRlcl9oZWlnaHQgPSAkKFwiLmhlYWRlci1hcmVhXCIpLmhlaWdodCgpO1xyXG5cclxuICAgICAgICAgICAgdmFyIHNjcm9sbFRvcCA9IHdpbmRvd3Muc2Nyb2xsVG9wKCk7XHJcblxyXG4gICAgICAgICAgICBpZiAoc2Nyb2xsVG9wID4gaGVhZGVyX2hlaWdodCkge1xyXG5cclxuICAgICAgICAgICAgICAgICQoXCIuaGVhZGVyLWFyZWFcIikuYWRkQ2xhc3MoXCJzdGlja3lcIik7XHJcblxyXG4gICAgICAgICAgICB9IGVsc2Uge1xyXG5cclxuICAgICAgICAgICAgICAgICQoXCIuaGVhZGVyLWFyZWFcIikucmVtb3ZlQ2xhc3MoXCJzdGlja3lcIik7XHJcblxyXG4gICAgICAgICAgICB9XHJcbiAgICAgICAgfSk7XHJcblxyXG4gICAgfVxyXG5cclxuICAgIGZpeGVkX3RvcF9tZW51KCk7XHJcblxyXG4gICAgLyogVGVzdGltb25pYWwtU2xpZGVyICovXHJcblx0XHJcbiAgICBpZiAoKCcudGVzdGltb25pYWwtc2xpZGVyJykubGVuZ3RoID4gMCkge1xyXG4gICAgICAgICQoXCIudGVzdGltb25pYWwtc2xpZGVyXCIpLm93bENhcm91c2VsKHtcclxuICAgICAgICAgICAgYXV0b3BsYXk6IHRydWUsXHJcbiAgICAgICAgICAgIGRvdHM6IGZhbHNlLFxyXG4gICAgICAgICAgICBsb29wOiB0cnVlLFxyXG4gICAgICAgICAgICBtYXJnaW46IDMwLFxyXG4gICAgICAgICAgICBsYXp5TG9hZDogdHJ1ZSxcclxuICAgICAgICAgICAgY2VudGVyOiB0cnVlLFxyXG4gICAgICAgICAgICByZXNwb25zaXZlOiB7XHJcbiAgICAgICAgICAgICAgICAwOiB7XHJcbiAgICAgICAgICAgICAgICAgICAgaXRlbXM6IDFcclxuICAgICAgICAgICAgICAgIH0sXHJcbiAgICAgICAgICAgICAgICA3Njg6IHtcclxuICAgICAgICAgICAgICAgICAgICBpdGVtczogMlxyXG4gICAgICAgICAgICAgICAgfSxcclxuICAgICAgICAgICAgICAgIDEyMDA6IHtcclxuICAgICAgICAgICAgICAgICAgICBpdGVtczogM1xyXG4gICAgICAgICAgICAgICAgfVxyXG4gICAgICAgICAgICB9XHJcbiAgICAgICAgfSk7XHJcbiAgICB9XHJcblx0XHJcblx0XHJcbiAgICAvKiAgQ3VzdG9tIG11bHRpIGpzKi9cclxuXHRcclxuICAgIGlmICgoXCIuY3VzdG9tLW11bHRpLXNlbGVjdFwiKS5sZW5ndGggPiAwKSB7XHJcbiAgICAgICAgJCgnLmN1c3RvbS1tdWx0aS1zZWxlY3QnKS5zZWxlY3QyKCk7XHJcblxyXG4gICAgfVxyXG5cclxuICAgIC8qICBtYWduaWZpY1BvcHVwICovXHJcblxyXG4gICAgJCgnLnZpZGVvLXBsYXknKS5tYWduaWZpY1BvcHVwKHtcclxuICAgICAgICB0eXBlOiAnaWZyYW1lJ1xyXG4gICAgfSk7XHJcblx0XHJcblx0LyogIFByZWxvYWRlciBqcyovXHJcblx0XHJcbiAgICAkKHdpbmRvdykub24oJ2xvYWQnLCBmdW5jdGlvbigpIHtcclxuXHJcbiAgICAgICAgdmFyIHByZUxvZGVyID0gJChcIiNwcmVsb2FkZXJcIik7XHJcbiAgICAgICAgcHJlTG9kZXIuZmFkZU91dCgxMDAwKTtcclxuXHJcbiAgICB9KTtcclxuXHRcclxuICAgIC8qIGhpZ2hsaWdodCBqcyAqL1xyXG5cdFxyXG4gICAgaWYgKCgncHJlIGNvZGUnKS5sZW5ndGggPiAwKSB7XHJcbiAgICAgICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgncHJlIGNvZGUnKS5mb3JFYWNoKChibG9jaykgPT4ge1xyXG4gICAgICAgICAgICBobGpzLmhpZ2hsaWdodEJsb2NrKGJsb2NrKTtcclxuICAgICAgICB9KTtcclxuICAgIH1cdFxyXG5cdFxyXG4gICAgLyogIEFPUyBhbmltYXRpb24qL1xyXG5cclxuICAgIEFPUy5pbml0KHtcclxuICAgICAgICBvbmNlOiB0cnVlLFxyXG5cclxuICAgIH0pO1xyXG5cdFxyXG5cclxufShqUXVlcnkpKTsiXX0=
