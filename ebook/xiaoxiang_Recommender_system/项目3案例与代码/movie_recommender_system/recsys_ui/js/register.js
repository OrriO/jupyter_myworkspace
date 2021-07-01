
/*
[青春, 喜剧, 情色, 科幻, 经典, 恐怖, 励志, 灾难, 同性, 犯罪, 西部, 传记, 惊悚, 冒险, 文艺, 女性, 奇幻, 歌舞, 历史, 悬疑, 黑帮, 音乐, 魔幻, 剧情, 感人, 武侠, 爱情, 战争, 动作, 搞笑]
*/
/**
 * @author Dong Changqing
 * 登录
 */
function register() {
	var register_username = $("#register_username").val();
	var register_password = $("#register_password").val();
	var register_school = $("#register_school").val();
	var register_age = $("#register_age").val();
	var register_sex = $("input[name='register_sex']:checked").val();
	var register_occupation = $("#register_occupation").val();
	var register_preference = "";
	
	$("input[name='register_preference']").each(function() {
        if ($(this).prop('checked')) {
        	console.log($(this).val());
        	register_preference = register_preference + $(this).val() + "|";
        }
	});
	
	if(register_preference.length > 0) {
		register_preference = register_preference.substring(0,register_preference.length - 1) 
	}
	var register_region = $("#register_region").val();
	$.ajax({
		type: 'GET',
		url: 'http://www.technologyx.cn/systemUser/insert2',
		contentType: 'application/json',
		dataType:'jsonp',
		jsonp:'jsonpcallback',
		jsonpCallback:"jsonpcallback",
		data:{
			"username":register_username,
			"password":register_password,
			"school":register_school,
			"age":register_age,
			"sex":register_sex,
			"occupation":register_occupation,
			"preference":register_preference,
			"region":register_region
		},
		jsonp:'jsonpcallback',
		jsonpCallback:"jsonpcallback",
		error: function(XmlHttpRequest,textStatus,errorThrown){
			window.location.href = "login.html";
		},
		success: function(msg){	
			console.log(msg);
			window.location.href = "login.html";
		}		
	});
}


