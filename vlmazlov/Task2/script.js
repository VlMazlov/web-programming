var  task_colors = [];
var color_styles = ['task', 'task red', 'task blue', 'task taupe'];
var unfinished = 0;

function load_tasks() {
	
	var task_list = localStorage.getItem('SimpleToDo.task-list');
	$('#task-list').html(JSON.parse(task_list));

	$('.completed').children('.task-checkbox').prop('checked', true);
	$('.task-div').each(function () {
		$(this).data('initial_color', $(this).css('background-color'));	
	});

	unfinished = $('.task').length - $('.completed').length;
	update();
}

function save_tasks() {
	localStorage.setItem('SimpleToDo.task-list', JSON.stringify($('#task-list').html()));
}

function update() {
	save_tasks();
	$('footer').text(unfinished + ' tasks to do');
}


function edit_task(edit_input) {
	var task_text = edit_input.siblings('.task-text');

	if (edit_input.val() !== "") {
		task_text.text(edit_input.val());
	}

	edit_input.siblings().css('display', 'inline');
	edit_input.siblings('remove').css('display', 'none');
	edit_input.remove();
	update();
}

function add_task(event) 
{
	if (event.preventDefault) 
	{
	    event.preventDefault();
	}

	var new_task = $('#new-task').val();
		
	if (new_task === '') 
	{
		return;
	}

	var task_list = $('#task-list');

	var random_color = color_styles[Math.floor(Math.random() * color_styles.length)];
	var current_task_div = $('<div class="task-div">').addClass(random_color);

	current_task_div.data('initial_color', current_task_div.css('background-color'));	

	current_task_div.append($('<input class="task-checkbox pure-checkbox" type="checkbox">'));
	current_task_div.append($('<span class="task-text">').text(new_task));
	current_task_div.append($('<img class="remove" src="delete.png">'));

	task_list.append(current_task_div);

	++unfinished;

	task_colors.push(random_color);

	$('#new-task').val('');

	update();
}

$(document).ready(
	load_tasks()
);

$(window).unload(function() {
	console.log("unload");
	$.each(function () {
		$(this).mouseout();
		console.log("fix");
	})
});

$('#form').submit(function (event) {
		
	add_task(event);	
});

$(document).on('change', '.task-checkbox', function () 
{

	$(this).parent().toggleClass('completed');

	if ($(this).parent().hasClass('completed')) 
	{
		
		$(this).parent().children('.task-text').css('text-decoration', 'line-through');
		--unfinished;
    
    } 
    else 
    {
        
        $(this).parent().children('.task-text').css('text-decoration', 'none');
		++unfinished;
    
    }

	update();
});

$(document).on('mouseover', '.task-div', function() 
{
		$(this).css('background-color', 'white');
		$(this).css('color', 'black');
		$(this).css('border-style', 'solid');
		$(this).css('border-width', '1px');

		$(this).children('.remove').css('display', 'block');
	
}).on('mouseout', '.task-div', function() 
{
		$(this).css('background-color', $(this).data('initial_color'));
		$(this).css('color', '#fff');
		$(this).css('border-style', 'none');
		
		$(this).children('.remove').css('display', 'none');

		update();
	
});

$(document).on('click', '.remove', function() 
{
		if (!($(this).parent().hasClass('completed'))) 
		{
			--unfinished;
		}

		$($(this).parent()).remove();

		update();
});

$(document).on('mouseover', '.remove', function() 
{

		$(this).css('opacity', 1.0);
	
}).on('mouseout', '.remove', function() 
{
		
		$(this).css('opacity', 0.5);
	
});

$(document).on('click', '.mark-button', function() 
{
		
		$('.task-div').each(function () {
			
			var task_checkbox = $(this).children('.task-checkbox');
			
			if (!($(this).hasClass('completed'))) 
			{
				task_checkbox.prop('checked', 'checked');
				$(this).children('.task-checkbox').change();
			}
		});

		update();
});

$(document).on('click', '.delete-button', function() 
{
		
		$('.completed').each(function () {
			$(this).remove();
		});

		update();
});

$(document).on('dblclick', '.task-text', function() 
{
		if ( $(this).siblings('#edit-task').length !== 0) {
			return;
		}

		$(this).parent().children().each(function() {
			$(this).css('display', 'none');
		});

		$(this).parent().prepend('<input type="text" id="edit-task">');
		$(this).siblings('#edit-task').attr('value', $(this).children('.task-text').text());
		$(this).siblings('#edit-task').select();
});


$(document).on('focusout', '#edit-task', function() 
{ 
	edit_task($(this));
});

$(document).on('keypress', '#edit-task', function(event) 
{ 
	if (event.which === 13) 
	{
		$(this).focusout();
		edit_task($(this));
	}
});
