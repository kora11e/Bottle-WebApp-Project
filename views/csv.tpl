<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>CSV Reader</title>
    <link rel="stylesheet" href="./static/mainStyle.css">
    <link rel="icon" href="./favicon.ico" type="image/x-icon">
    <script src='./static/read_csv.js'></script>
  </head>
  <body>
    <div>
      <div>
        <input type='file' name='file' id='file' accept='.csv'><br><br>
        <input type='button' id='btnsubmit' value='Submit' onclick='readCSVFile()'>
      </div>

      <br><br>
      <table id='tblcsvdata' border='1' style='border-collapse: collapse'>
        <thead>
          <th>Order_Date</th>
          <th>Ship_Date</th>
          <th>Ship_Mode</th>
          <th>Postal_Code</th>
          <th>Region</th>
          <th>Product_Reference</th>
          <th>Category</th>
          <th>Sub_Category</th>          
          <th>Sales</th>
          <th>Quantity</th>
          <th>Profit</th>
          <th>State</th>
        </thead>
        <tbody></tbody>
      </table>
    </div>
    <script src='./static/read_csv.js'></script>
  </body>
</html>