%#template for database
<h1>To do List</h1>
<p>The open items are as follows</p>
<form action='/delete' method='post'>
%setdefault('category', '')
%
%for row in rows:
%   if category != row[0]:
%   category = row[0]

    <h2>{{row[0]}}</h2>
%   end

    <li>{{row[1]}}</li>
    <button type='submit' name='delitem' value='{{row[2]}}'>Delete</button>
    </li>
%end
</form>
<hr>
% include('new_todo.tpl')