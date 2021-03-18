function calculate(){

    var a,b,c,d,e,result1,result2;


    a  = document.getElementById('inner_friction').value;
    b  = document.getElementById('outer_friction').value;
    c  = document.getElementById('pressure_                                                                                                                                                    .                                        ..3. force').value;
    d  = document.getElementById('number_of_clutch').value;
    e  = document.getElementById('friction_coefficient').value;



    result1 = ((2*(parseFloat(b))**3-(parseFloat(a))**3)/3*((parseFloat(b))**2-(parseFloat(a))**2));
    result2 =((parseFloat(c)) * ((2*((parseFloat(b))**3 - (parseFloat(a))**3) /3*((parseFloat(b))**2 - (parseFloat(a))**2)) * (parseFloat(e)) * (parseFloat(d))))
    
    document.getElementById('result1').innerHTML = result1;
    document.getElementById('result2').innerHTML = result2;
}