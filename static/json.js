fetch("./static/items.json")

.then(function(response){
    return response.json()
})

.then(function(items) {
    let placeholder = document.querySelector('#data-output')
    let out = ''
    for (let item of items) {
        out += `
            <tr>
                <td> ${item.name} </td>
                <td> ${item.price} </td>
                <td> ${item.stock} </td>
            </tr>
        `
    }

    placeholder.innerHTML = JSON.stringify(out)
})