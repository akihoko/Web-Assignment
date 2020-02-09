$('.wrapper').owlCarousel({
    loop: true,
    margin: 5,
    nav: true,
    autoplay: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 3
        }
    }
});

function mouseclick() {
    document.querySelector(".down").style.display = "block";
    document.querySelector(".right").style.display = "none";
}

function mous() {
    document.querySelector(".down").style.display = "none";
    document.querySelector(".right").style.display = "block";
}

document.querySelector(".abcd").click()=true

function priceDetermine()
{
var quantity=document.getElementById('no').value;
var type=document.getElementById('type').value;
if(type=="Budget")
{
document.getElementById('price').value=parseInt(quantity)*40;
}
else if(type=="Medium")
{
   document.getElementById('price').value=parseInt(quantity)*300;
}
else
{
   document.getElementById('price').value=parseInt(quantity)*700;
}
}

