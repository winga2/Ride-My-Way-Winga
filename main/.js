//Defining a listener for our button, onclick handler
document.getElementById("add").onclick = function() {
    // we need our text:
    var text = document.getElementById("idea").value; //.value gets input values

    // a quick list element
    var li = "<li>" + text + "</li>";

    //Now use appendChild and add it to the list!
    document.getElementById("list").appendChild(li);
}


//for services offered
function myFunction() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

