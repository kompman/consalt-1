$(document).ready(function(){

	/* Приветствую тебя кодер, посмотри фильм Мост в Терабитию */
	/* футер */
	$('.button_footer').click(function(){
		$('.popup2').arcticmodal();
	});
	/* заказать бесплатную консультацию */
	$('.button_five').click(function(){
		$('.popup').arcticmodal();
	});
	/* получить бесплатную консультацию */
	$('.button_fo').click(function(){
		$('.popup').arcticmodal();
	});
	/* начать соотрудничество */
	$('.button_fre').click(function(){
		$('.popup2').arcticmodal();
	});
	/* звонок топ линия*/
	$('.button_one').click(function(){
		$('.popup2').arcticmodal();
	});

		//дает красный бордер
	function red_border(input_name){ 
		var name = 'input[name="' + input_name + '"]';
		$(name).css({'border':'1px solid red'});
		setTimeout(function(){
			$(name).css({'border':'none'});
		},3000);
	}

	//ajax запрос на обработку формы
	function ajax_zapros(name,phone,name_val,phone_val){ 
		$.ajax({
			type:"POST",
			url:"form.php",
			data:{name_form:name_val,phone_form:phone_val},
			success:success_form,			
			error:error_form
		});

		//В случае возникновения ошибки при отправке формы
		function error_form(error){
			alert("Ошибка, форма не отправлена, обновите страницу и попробуйте снова!");
		}

		//В случае положительной отправки формы
		function success_form(success){
			$('.popup3').arcticmodal();
			$('input[name="' + name + '"]').attr("value","");
			$('input[name="' + phone + '"]').attr("value","");
			yaCounter25531454.reachGoal('идентификатор задается при создании цели'); return true;
		}
	}

	//Обработка форм на валиндность
	function validete_form(name,phone){

		var name_val = $('input[name="' + name + '"]').val();
		var phone_val = $('input[name="' + phone + '"]').val();
		if(name_val.length > 2){
			
		}else{
			red_border(name);
		}

		if(phone_val.length > 3){
			
		}else{
			red_border(phone);
		}

		if(name_val.length > 2 && phone_val.length > 3){
			ajax_zapros(name,phone,name_val,phone_val);//если все окей делаем запрос на отправку данных
		}
	}

	/* Форма попап */
	$('.bt_1').click(function(){
		validete_form("name_popup_1","phone_popup_1");
	});

	/* Форма попап 2*/
	$('.bt_2').click(function(){
		validete_form("name_popup_2","phone_popup_2");
	});

	/* Форма в шапке*/
	$('.bt_3').click(function(){
		validete_form("name_1","phone_1");
	});

	/* big forms */
	$('.bt_4').click(function(){
		validete_form("name_2","phone_2");
	});

	/* Акции время */
	var action_day = 1;/* День */
    var action_Hours = $('#time_hour').text();/* Часы */
    var action_Minutes = $('#time_minutes').text();/* Минуты */
    var action_Seconds = $('#time_second').text();/* Секунды */

    setInterval(function(){
    	action_Seconds = action_Seconds - 1;

		if(action_Seconds < 0){
			action_Seconds = 59;
			action_Minutes = action_Minutes - 1;
		}

		if(action_Minutes < 0){
			action_Hours = action_Hours - 1;
			action_Minutes = 59;
		}

		if(action_Hours < 0){
			action_Hours = 12;
			action_day = action_day - 1;
		}

		if(action_day < 0){
			action_day = 1;
		}

		var hours = action_Hours;
		var minutes = action_Minutes;
		var seconds = action_Seconds;
		var day = action_day;

		if(hours < 10){
			hours = "0" + hours;
		}

		if(minutes < 10){
			minutes = "0" + minutes;
		}

		if(seconds < 10){
			seconds = "0" + seconds;
		}

		if(day < 10){
			day = "0" + day;
		}
		/* Вывод */
		$('.hour p,.hour1 p').html(hours);
		$('.minutes p,.minutes1 p').html(minutes);
		$('.second p,.second1 p').html(seconds);
    },1000);

    /* Анимации */
    /* Если пользователь вошел не с телефонной платформы */
    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {

	}else{
		/* Даем элементам прозрачность чтобы их не было видно до выполнения анимации */
		$('.stats_item,.rezult_item,.client_polychayt_item,.item_yslygi,.cifri_item,.kak_rab,.kak_rab_two').css({'opacity':'0'});

		/* Элементы которые всплывают сразу при загрузке страницы */
		$('.logo_top_linear').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
		$('.top_help,.hats h1').css({'opacity':'1','-webkit-animation-name':'fadeInUp','animation-name':'fadeInUp','-webkit-animation-duration':'1s','animation-duration':'1s'});
		$('.call_top_linear,.button_one').css({'opacity':'1','-webkit-animation-name':'fadeInRight','animation-name':'fadeInRight','-webkit-animation-duration':'1s','animation-duration':'1s'});

		var scroll;
		/* Если пользователь начал двигать скролл */
	    $(window).scroll(function(){
		    scroll = $(window).scrollTop();/* Берем значение скрола */
		    /* СТАТИСТИЧЕСКИЕ ДАННЫЕ */
		    if(scroll > 580){
		    	$('.stats_item_1').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
		    }
		    if(scroll > 700){
		    	$('.stats_item_2').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
		    }
		    if(scroll > 870){
		    	$('.stats_item_3').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
		    }
		    if(scroll > 960){
		    	$('.stats_item_4').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
		    }

		    /* ПОЧЕМУ МЫ ГАРАНТИРУЕМ РЕЗУЛЬТАТ */
		     if(scroll > 1350){
			     setTimeout(function(){
			    	$('.rezult_item1').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
			    setTimeout(function(){
			    	$('.rezult_item2').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },200);	
			    setTimeout(function(){
			    	$('.rezult_item3').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },300);	
			    setTimeout(function(){
			    	$('.rezult_item4').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },400);	
			    setTimeout(function(){
			    	$('.rezult_item5').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },500);	
		    }

		     /* СООТРУДНИЧАЯ С НАМИ */
		     if(scroll > 2250){
			     setTimeout(function(){
			    	$('.client_polychayt_item1').css({'opacity':'1','-webkit-animation-name':'fadeInRight','animation-name':'fadeInRight','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
			    setTimeout(function(){
			    	$('.client_polychayt_item2').css({'opacity':'1','-webkit-animation-name':'fadeInRight','animation-name':'fadeInRight','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },200);	
			    setTimeout(function(){
			    	$('.client_polychayt_item3').css({'opacity':'1','-webkit-animation-name':'fadeInRight','animation-name':'fadeInRight','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },300);	
			    setTimeout(function(){
			    	$('.client_polychayt_item4').css({'opacity':'1','-webkit-animation-name':'fadeInRight','animation-name':'fadeInRight','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },400);	
			    setTimeout(function(){
			    	$('.client_polychayt_item5').css({'opacity':'1','-webkit-animation-name':'fadeInRight','animation-name':'fadeInRight','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },500);	
		    }

		     /* Наши услуги */
		     if(scroll > 3000){
			     setTimeout(function(){
			    	$('.item_yslygi1').css({'opacity':'1','-webkit-animation-name':'fadeInUp','animation-name':'fadeInUp','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
			    setTimeout(function(){
			    	$('.item_yslyg2').css({'opacity':'1','-webkit-animation-name':'fadeInUp','animation-name':'fadeInUp','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },200);	
		    }

		    if(scroll > 3100){
			     setTimeout(function(){
			    	$('.item_yslyg3').css({'opacity':'1','-webkit-animation-name':'fadeInUp','animation-name':'fadeInUp','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
			    setTimeout(function(){
			    	$('.item_yslyg4').css({'opacity':'1','-webkit-animation-name':'fadeInUp','animation-name':'fadeInUp','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },200);	
		    }

		    if(scroll > 3200){
			     setTimeout(function(){
			    	$('.item_yslyg5').css({'opacity':'1','-webkit-animation-name':'fadeInUp','animation-name':'fadeInUp','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
			    setTimeout(function(){
			    	$('.item_yslyg6').css({'opacity':'1','-webkit-animation-name':'fadeInUp','animation-name':'fadeInUp','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },200);	
		    }

		    if(scroll > 3300){
			     setTimeout(function(){
			    	$('.item_yslyg7').css({'opacity':'1','-webkit-animation-name':'fadeInUp','animation-name':'fadeInUp','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
			    setTimeout(function(){
			    	$('.item_yslyg8').css({'opacity':'1','-webkit-animation-name':'fadeInUp','animation-name':'fadeInUp','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },200);	
		    }
		    if(scroll > 3400){
			     setTimeout(function(){
			    	$('.item_yslyg9').css({'opacity':'1','-webkit-animation-name':'fadeInUp','animation-name':'fadeInUp','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
		    }


		     /* О нас в цифрах */
		     if(scroll > 4100){
			     setTimeout(function(){
			    	$('.cifri_item1').css({'opacity':'1','-webkit-animation-name':'bounceIn','animation-name':'bounceIn','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
			    setTimeout(function(){
			    	$('.cifri_item2').css({'opacity':'1','-webkit-animation-name':'bounceIn','animation-name':'bounceIn','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },200);	
			    setTimeout(function(){
			    	$('.cifri_item3').css({'opacity':'1','-webkit-animation-name':'bounceIn','animation-name':'bounceIn','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },300);	
			    setTimeout(function(){
			    	$('.cifri_item4').css({'opacity':'1','-webkit-animation-name':'bounceIn','animation-name':'bounceIn','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },400);	
			    setTimeout(function(){
			    	$('.cifri_item5').css({'opacity':'1','-webkit-animation-name':'bounceIn','animation-name':'bounceIn','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },500);	
		    }

		    /* Как мы работаем */
		    if(scroll > 4550){
			     setTimeout(function(){
			    	$('.kak_rab1').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
		    }

		    if(scroll > 4650){
			     setTimeout(function(){
			    	$('.kak_rab_two1').css({'opacity':'1','-webkit-animation-name':'fadeInRight','animation-name':'fadeInRight','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
		    }
		   

		   	if(scroll > 4800){
			     setTimeout(function(){
			    	$('.kak_rab2').css({'opacity':'1','-webkit-animation-name':'fadeInLeft','animation-name':'fadeInLeft','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
		    }

		    if(scroll > 4900){
			     setTimeout(function(){
			    	$('.kak_rab_two2').css({'opacity':'1','-webkit-animation-name':'fadeInRight','animation-name':'fadeInRight','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
		    }

		    if(scroll > 5050){
			     setTimeout(function(){
			    	$('.kak_rab3').css({'opacity':'1','-webkit-animation-name':'fadeInRight','animation-name':'fadeInRight','-webkit-animation-duration':'1s','animation-duration':'1s'});
			    },100);	
		    }
		});
	}
});	    