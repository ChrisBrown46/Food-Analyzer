<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
  <head>
      <meta charset="utf-8" />
      <title></title>
  </head>
  <body style="background-color: #272320;">
    <form action="Facts.php" method="post" enctype="multipart/form-data">
      <p style="font-size: xx-large; text-align: center; color: teal;"> Input a direct link to an image file on the web </p>
      <input id="url" type="url" name="food" style="display: inline-block; margin-top: 10px; margin-bottom: 0px; margin-left: 40%; margin-right:40%;" />
      <p style="font-size: xx-large; text-align: center; color: teal;">Or choose a file on your local device</p>
      <input id="fileUpload" type="file" name="foodImage" accept="image/*" style="display: inline-block; margin: 0 40%;" />
      <input type="submit" value="Analyze Food" style="margin-top: 30px; margin-left:40%; margin-right:40%; margin-bottom: 0px;" />
    </form>
  </body>
</html>
