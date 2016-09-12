document.addEventListener('DOMContentLoaded', function() {
	
	function getSoundID() {
		var uri = document.baseURI.split('/');
		return Number(uri[uri.length - 2]);
	}
	function changeQuality(quality) {
		select_quality = document.getElementById('id_quality');
		select_quality.selectedIndex = quality;
	}
		
	document.addEventListener('keydown', function(event) {
		switch (event.which) {
			case 13: // enter
				document.getElementById('form_quality').submit();
				break;
			case 37: // left arrow
				sound_id = getSoundID();
				window.location.href = "/browse/" + String(sound_id - 1);
				break;
			case 39: // right arrow
				sound_id = getSoundID();
				window.location.href = "/browse/" + String(sound_id + 1);	
				break;
			case 48: // 0
				changeQuality(0);
				break;
			case 49: // 1
				changeQuality(1);
				break;
			case 50: // 2
				changeQuality(2);
				break;
			case 51: // 3
				changeQuality(3);
				break;
		}
	});
});
