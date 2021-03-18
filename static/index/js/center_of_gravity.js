function Frontreact(){
    var result1,a;
    a = document.getElementById('frontmass').value;
    result1 = parseFloat(a)*9.81;
    document.getElementById('front').innerHTML = result1;
}

function Reartreact(){
    var b,result2;
    b = document.getElementById('reartmasss').value;
    result2 = parseFloat(b)*9.81;
    document.getElementById('rear').innerHTML = result2;

}

function rearbase(){
    var a,c,d,result3;
    a = document.getElementById('frontmass').value;
    c = document.getElementById('wheelbase').value;
    d = document.getElementById('totalmass').value;
    result3 = ((parseFloat(a) * 9.81) * parseFloat(c))/(parseFloat(d) * 9.81);
    document.getElementById('base1').innerHTML = result3;
}

function frontbase(){
    var a,c,d,result4;
    a = document.getElementById('frontmass').value;
    c = document.getElementById('wheelbase').value;
    d = document.getElementById('totalmass').value;
    result4 = (parseFloat(c) - ((parseFloat(a) * 9.81) * parseFloat(c))/(parseFloat(d) * 9.81));
    document.getElementById('base2').innerHTML = result4;
}

