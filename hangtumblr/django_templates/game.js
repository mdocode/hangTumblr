var game(){
    initialize: function (varInits){
	window.onkeypress = this.keyboardInput;
    }

    drawfunc: function(){
	return false;
    }

    round: 0;

    drawInterval: 3000;

    draw: function (interval){
	start = Date().getTime();
	result = drawfunc();
	return Date().getTime()-start;
    }
    
    
    keyboard: function (keypress){
	return keypress;
    }

    keyboardInput: function(e){
	evt = document.event? event : e
	var letter = evt.keyCode? evt.keyCode : evt.charCode;
	this.keyboard(letter)
    }
}

