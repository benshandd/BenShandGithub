function query() {
var x = document.querySelectorAll(".caps");
  var i;
  for(i = 0; i < x.length; i++) {
    if(x[i].innerHTML.includes(y.value)) {
      x[i].style.display = 'block';
    } else {
      x[i].style.display = 'none';
    }
    var text = x[i].innerHTML
    console.log(text[0].toUpperCase() + text.slice(1));
  }
}
