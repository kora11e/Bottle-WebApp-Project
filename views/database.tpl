%#show Todo
<h1>To do List</h1>
<p>Build with Python in a template</p>
<form action='/delete' method='POST'>
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