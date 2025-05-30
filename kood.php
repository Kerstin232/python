<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minu esimene PHP</title>
</head>
<body>
    <H1> Massiivid </H1>
<?php
    $cars = array(
        "Subaru","BMW","Acura","Mercedes-Benz","Lexus","GMC","Volvo","Toyota","Volkswagen","Volkswagen","GMC","Jeep","Saab","Hyundai","Subaru","Mercedes-Benz",
        "Honda","Kia","Mercedes-Benz","Chevrolet","Chevrolet","Porsche","Buick","Dodge","GMC","Dodge","Nissan","Dodge","Jaguar","Ford","Honda","Toyota","Jeep",
        "Kia","Buick","Chevrolet","Subaru","Chevrolet","Chevrolet","Pontiac","Maybach","Chevrolet","Plymouth","Dodge","Nissan","Porsche","Nissan","Mercedes-Benz",
        "Suzuki","Nissan","Ford","Acura","Volkswagen","Lincoln","Mazda","BMW","Mercury","Mitsubishi","Ram","Audi","Kia","Pontiac","Toyota","Acura","Toyota","Toyota",
        "Chevrolet","Oldsmobile","Acura","Pontiac","Lexus","Chevrolet","Cadillac","GMC","Jeep","Audi","Acura","Acura","Honda","Dodge","Hummer","Chevrolet","BMW",
        "Honda","Lincoln","Hummer","Acura","Buick","BMW","Chevrolet","Cadillac","BMW","Pontiac","Audi","Hummer","Suzuki","Mitsubishi","Jeep","Buick","Ford"
    );

    //echo $cars [0];
    //print_r($cars);
    var_dump($cars);

    // echo count ($cars);
    $total_cars = count($cars);

    for ($i=0; $i <= $total_cars; $i++) { 
        echo $cars[$i]. "<br>";
    }
?>







<h1>Matemaatika</h1> 
    <form action= "#" method="get">
        arv 1 <input type= "number" name="nr1"><br>
        arv 2 <input type= "number" name="nr2"><br>
        <input type="submit" value="arvuta">
    </form>   
    <?php
        #Ülesanne 3
        if(!empty($_GET['nr1']) && !empty($_GET['nr2'])) {
            $arv1 = $_GET['nr1'];
            $arv2 = $_GET['nr2'];
            if ($arv2==0) { 
                echo "nulliga ei saa jagada!";
            } else{ $tehe = $arv1 / $arv2;
            }
            
            $tehe = $arv1 + $arv2;
        }
        

            echo "vastus: $tehe";




    #Ülesanne 2
    $fname="MARI";
    $Lname="Maasikas";
    $name= $fname." ".$lname;
    $age=20;
    $height=1.60;

    echo"<p>".$name." on ".$age." aastane ja".$height." +pikk</p>";

    echo $fname." ".$lname;
    


    #Ülesanne 1
    #tekst"komentaar"
        echo "<h1>Tere maailm</H1>";
        /*
        komentaar
        */
        echo "Dr. Alban - \" It's my life\"";
        echo "<br/>";
        echo 'Dr. Alban - " It\'s my life"'; 



    ?>
</body>
</html>
