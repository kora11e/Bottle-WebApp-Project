<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Home Page</title>
    <link rel="stylesheet" href="./static/style.css">
    <link rel="icon" href="./favicon.ico" type="image/x-icon">
    <script src='./static/read_csv.js'></script>
  </head>
  <body>
    <main>
        <h1>CSV Reader</h1>
    </main>
    <div>
        <br><br>
        <table id='tblcsvdata' border='1' style='border-collapse: collapse'>
            <thead>
                <th>index</th>
                <th>Username</th>
                <th>Name</th>
                <th>Email</th>
            </thead>
            <tbody></tbody>
        </table>
    </div>
  </body>
</html>