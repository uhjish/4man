/*!
 * jQuery wmuSlider v2.1
 * 
 * Copyright (c) 2011 Brice Lechatellier
 * http://brice.lechatellier.com/
 *
 * Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
 */
(function(a){a.fn.wmuSlider=function(b){var c={animation:"fade",animationDuration:600,slideshow:true,slideshowSpeed:7000,slideToStart:0,navigationControl:true,paginationControl:true,previousText:"Previous",nextText:"Next",touch:false,slide:"article",items:1};var b=a.extend(c,b);return this.each(function(){var p=a(this);var o=b.slideToStart;var f=p.find(".wmuSliderWrapper");var g=p.find(b.slide);var d=g.length;var k;var l;var e;var j=function(t,u,v){if(e){return false}e=true;o=t;var s=a(g[t]);p.animate({height:s.innerHeight()});if(b.animation=="fade"){g.css({position:"absolute",opacity:0});s.css("position","relative");s.animate({opacity:1},b.animationDuration,function(){e=false})}else{if(b.animation=="slide"){if(!u){f.animate({marginLeft:-p.width()/b.items*t},b.animationDuration,function(){e=false})}else{if(t==0){f.animate({marginLeft:-p.width()/b.items*d},b.animationDuration,function(){f.css("marginLeft",0);e=false})}else{if(!v){f.css("marginLeft",-p.width()/b.items*d)}f.animate({marginLeft:-p.width()/b.items*t},b.animationDuration,function(){e=false})}}}}if(l){l.find("a").each(function(w){if(w==t){a(this).addClass("wmuActive")}else{a(this).removeClass("wmuActive")}})}p.trigger("slideLoaded",t)};if(b.navigationControl){var i=a('<a class="wmuSliderPrev">'+b.previousText+"</a>");i.click(function(s){s.preventDefault();clearTimeout(k);if(o==0){j(d-1,true)}else{j(o-1)}});p.append(i);var m=a('<a class="wmuSliderNext">'+b.nextText+"</a>");m.click(function(s){s.preventDefault();clearTimeout(k);if(o+1==d){j(0,true)}else{j(o+1)}});p.append(m)}if(b.paginationControl){l=a('<ul class="wmuSliderPagination"></ul>');a.each(g,function(s){l.append('<li><a href="#">'+s+"</a></li>");l.find("a:eq("+s+")").click(function(t){t.preventDefault();clearTimeout(k);j(s)})});p.append(l)}if(b.slideshow){var r=function(){if(o+1<d){j(o+1)}else{j(0,true)}k=setTimeout(r,b.slideshowSpeed)};k=setTimeout(r,b.slideshowSpeed)}var h=function(){var s=a(g[o]);p.animate({height:s.innerHeight()});if(b.animation=="slide"){g.css({width:p.width()/b.items});f.css({marginLeft:-p.width()/b.items*o,width:p.width()*g.length})}};var n=function(t,s,u,v){clearTimeout(k);if(s=="move"&&(u=="left"||u=="right")){if(u=="right"){if(o==0){f.css("marginLeft",(-d*p.width()/b.items)+v)}else{f.css("marginLeft",(-o*p.width()/b.items)+v)}}else{if(u=="left"){f.css("marginLeft",(-o*p.width()/b.items)-v)}}}else{if(s=="cancel"){if(u=="right"&&o==0){f.animate({marginLeft:-d*p.width()/b.items},b.animationDuration)}else{f.animate({marginLeft:-o*p.width()/b.items},b.animationDuration)}}else{if(s=="end"){if(u=="right"){if(o==0){j(d-1,true,true)}else{j(o-1)}}else{if(u=="left"){if(o+1==d){j(0,true)}else{j(o+1)}}else{f.animate({marginLeft:-o*p.width()/b.items},b.animationDuration)}}}}}};if(b.touch&&b.animation=="slide"){if(!a.isFunction(a.fn.swipe)){a.ajax({url:"jquery.touchSwipe.min.js",async:false})}if(a.isFunction(a.fn.swipe)){p.swipe({triggerOnTouchEnd:false,swipeStatus:n,allowPageScroll:"vertical"})}}var q=function(){var s=a(g[o]);var t=s.find("img");t.load(function(){f.show();p.animate({height:s.innerHeight()})});if(b.animation=="fade"){g.css({position:"absolute",width:"100%",opacity:0});a(g[o]).css("position","relative")}else{if(b.animation=="slide"){if(b.items>d){b.items=d}g.css("float","left");g.each(function(w){var v=a(this);v.attr("data-index",w)});for(var u=0;u<b.items;u++){f.append(a(g[u]).clone())}g=p.find(b.slide)}}h();p.trigger("hasLoaded");j(o)};q();a(window).resize(h);p.bind("loadSlide",function(t,s){clearTimeout(k);j(s)})})}})(jQuery);