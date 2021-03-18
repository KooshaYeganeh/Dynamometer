$(document).ready(function () {
$("#calculate").click(function () { 
    $.post("/gradeability" , {Raduis : $("#raduis").val()  , gravitational_acceleration : $("#gravitational").val(),Friction : $("#friction").val(), Angle : $("#angle").val()},function(data){
        $("#result").append("<p>" + data.toString() + "</p>");
    }
    
});
});