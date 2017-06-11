var browse = $('#upl');
var add = $('#add');

browse.on('change', function () {
	console.log($(this));
	var files = $(this).get(0).files;
	if (files.length > 0) {
		add.removeAttr('disabled');
	} else {
		add.attr('disabled',true);
	}
	console.log(files);
})