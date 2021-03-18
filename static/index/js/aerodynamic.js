$(document).ready(function () {
    $("#button").click(function () { 
        console.log( {Height : $("#height").val() , Width : $("#width").val()});
        $.post("/aerodynamic/area" , {Height : $("#height").val() , Width : $("#width").val()},function(data){
            $("#demo").append("<p>" + data.toString() + "</p>");
        });
        
    });


    $("#dbutton").click(function () { 
        console.log({Drag_Coefficient : $("#coefficient").val() ,  Height : $("#height").val() , Width : $("#width").val() , Speed : $("#speed").val()})
        $.post("/aerodynamic/drag" , {Drag_Coefficient : $("#coefficient").val() ,  Height : $("#height").val() , Width : $("#width").val() , Speed : $("#speed").val()},function(data){

            $("#result").append("<p>" + data.toString() + "</p>");
        });
        
    });
});
















