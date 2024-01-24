<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Home Page</title>
    <link rel="stylesheet" href="./static/mainStyle.css">
    <link rel="icon" href="./favicon.ico" type="image/x-icon">
  </head>
  <body>
    <div id='flex'>

%#show Todo
<h1>To do List</h1>
<p>Build with Python in a template</p>
<form action='/database/delete' method='POST'>
%setdefault('icategory', '')

%for row in rows:
%
%   if icategory != row[0]:
%       icategory = row[0]

        <h2>{{row[0]}}</h2>
%   end

<li>{{row[1]}}
<button type='submit' name='delitem' value='{{row[2]}}'>Delete</button>
</li>

%end

</form>
<hr>
<br>
%   include('new_todo.tpl')
    </div>
  </body>
</html>