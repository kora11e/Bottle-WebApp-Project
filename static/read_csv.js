function readCSV() {
    var files = document.querySelector('#file').files

    if(files.length > 0){
        var file = files[0]

        var reader = new FileReader()

        reader.readAsText(file)

        reader.onload = function(event){
            var csvdata = event.target.result

            var rowData = csvdata.split('\n')

            var tbody = document.getElementById('tblcsvdata').getElementsByTagName('tbody')[0]
            tbody.innerHTML = ''

            for (var row = 1; row < rowData.length; row++) {
                var newRow = tbody.insertRow()
                rowColData = rowData[row].split(',')

                for (var col=0; col < rowColData.length; col++) {
                    var newCell = newRow.insertCell()
                    newCell.innerHTML = rowColData[col]
                }
            }
        }
    } else {
        alert('Select a file!')
    }
}