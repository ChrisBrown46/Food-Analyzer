<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
	<head>
			<meta charset="utf-8" />
			<title></title>
	</head>
	<body style="margin:0px; background-color: #272320;">
		<?php
		 	if($_POST["food"] != ""){
				$foodLocation = $_POST["food"];
				$type = "url";
			}else {
				//$foodLocation = $_POST["foodImage"];
				$foodLocation = $_FILES["foodImage"]["tmp_name"];
				$type = "file";
			}
		?>
		<div style="width:100%; background-color: #272320; display: block;">
			<p style="font-size: 80px; text-align:center; color: teal;"> Food: <?php $food = system('python Analyze_Food.py ' . $foodLocation . ' ' . $type); ?> </p><br>
		</div>
		<div style="width: 33%; display: inline-block; background-color: #5D5D61; height: 100%; margin-top:0px;">
			<p style="margin-left:20px; font-size: xx-large; color: #272320;">Wiki: <?php $test2 = system('python Food_Finder_Wikipedia.py ' . $food); ?></p>
		</div>
		<div style="width: 33%; display: inline-block; background-color: teal; height:100%; margin-left:-4px; margin-top:0px;">
			<p style="margin-left:20px; font-size: xx-large; color: #C8C9C7;">Sides:</p>
		</div>
		<div style="width:33%; display: inline-block; background-color: #5D5D61; height:100%; margin-left:-4px; margin-top:0px;">
			<p style="margin-left:20px; font-size: xx-large; color: #272320;">Nutrition:</p>
		</div>

	</body>
</html>
