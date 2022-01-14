<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Starbucks Website Landing Page</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <section>
        <div class="circle"></div>
        <header>
            <a href="#"><img src="img/logo.png" alt="" class="logo"></a>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Menu</a></li>
                <li><a href="#">What's New</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </header>
        <div class="content">
            <div class="textBox">
                <h2>It's not just Coffee<br>It's <span>Starbucks</span></h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit, sed do eiusmod
                    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.</p>
                <a href="#">Learn More</a>
            </div>
            <div class="imgBox">
                <img src="img/img1.png" class="starbucks" alt="">
            </div>
        </div>
        <ul class="thumb">
            <li><img src="img/thumb1.png" alt="" onclick="imgSlider('img/img1.png');changeCirclecolor('#017143')"></li>
            <li><img src="img/thumb2.png" alt="" onclick="imgSlider('img/img2.png');changeCirclecolor('#eb7495')"></li>
            <li><img src="img/thumb3.png" alt="" onclick="imgSlider('img/img3.png');changeCirclecolor('#d752b1')"></li>
        </ul>
        <ul class="sci">
            <li><a href="#"><img src="img/facebook.png" alt=""></a></li>
            <li><a href="#"><img src="img/twitter.png" alt=""></a></li>
            <li><a href="#"><img src="img/instagram.png" alt=""></a></li>
        </ul>
    </section>
    <script>
        function imgSlider(anything){
            document.querySelector('.starbucks').src = anything;
        }
        function changeCirclecolor(color){
            const circle = document.querySelector('.circle');
            circle.style.background = color;
        }
    </script>
</body>
</html>