<p>Add new task to the To do List:</p>
<form action='/new' method='POST'>
    <select name='newcategory'>
        <option value='Activities'>Activities</option>
        <option value='Projects'>Projects</option>
        <option value='Shopping' selected>Shopping</option>
    </select>
    <input type='text' size='25' name='theitem'>
    <input type='submit' name='save' value='save'>
</form>