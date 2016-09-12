document.addEventListener('DOMContentLoaded', function() {
	
	function getSoundID() {
		var uri = document.baseURI.split('/');
		return Number(uri[uri.length - 2]);
	}
	
	document.addEventListener('keydown', function(event) {
		if (event.keyIdentifier === 'Left') {
			sound_id = getSoundID();
			window.location.href = "/browse/" + String(sound_id - 1);
		}
		if (event.keyIdentifier === 'Right') {
			sound_id = getSoundID();
			window.location.href = "/browse/" + String(sound_id + 1);	
		}
	});
});
