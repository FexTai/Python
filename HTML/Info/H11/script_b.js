let x = Number(document.getElementById("var1").value) + Number(document.getElementById("var2").value);

function addieren() {
    document.getElementById("ergebnis").innerHTML = 
    Number(document.getElementById("var1").value) + 
    Number(document.getElementById("var2").value);
} 

function subtrahieren() {
    document.getElementById("ergebnis").innerHTML =
        Number(document.getElementById("var1").value) - 
        Number(document.getElementById("var2").value);
} 

function dividieren() {
    document.getElementById("ergebnis").innerHTML =
        Number(document.getElementById("var1").value) / 
        Number(document.getElementById("var2").value);
} 

function multiplizieren() {
    document.getElementById("ergebnis").innerHTML =
        Number(document.getElementById("var1").value) * 
        Number(document.getElementById("var2").value);
} 