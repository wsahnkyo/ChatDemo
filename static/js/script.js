$(document).ready(function() {
	    // 当用户按下回车键时发送消息
    $('#message-input').on('keydown', function(event) {
        if (event.keyCode === 13 && !event.shiftKey) { // 检查是否按下了回车键且没有按住Shift键
            event.preventDefault(); // 阻止默认行为，防止表单提交等
            var message = $(this).val();
            if (message.trim() !== '') {
                addMessage('User', message);
                $(this).val('');
                var response = getResponse(message);
                addMessage('AI', response);
            }
        }
    });
	 $('.item').on('click', function() {
                var title = $(this).find('.details h3').text();
                var description = $(this).find('.details p').text();
                alert('标题: ' + title + '\n描述: ' + description);
            });
    $('#send-button').click(function() {
        var message = $('#message-input').val();
        if (message.trim() !== '') {
            addMessage('User', message);
            $('#message-input').val('');
            var response = getResponse(message);
            addMessage('AI', response);
        }
    });

    function addMessage(sender, message) {
		var messageClass = sender === 'User' ? 'user' : 'ai';
		var avatarClass = sender === 'User' ? 'user-avatar' : 'ai-avatar';
		$('#chat-messages').append('<div class="message ' + messageClass + '">' +
									'<div class="avatar ' + avatarClass + '"></div>' +
									'<div class="text">' + message + '</div>' +
									'</div>');
        $('#chat-messages').scrollTop($('#chat-messages')[0].scrollHeight);

    }

    function getResponse(userInput) {
        // 这里可以是你的 AI 对话逻辑
        return 'Hello, you said: ' + userInput;
    }
});