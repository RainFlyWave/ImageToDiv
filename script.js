let fetchedData;
const canvas = document.getElementById('canvas')

function colorGenDiv() {
    const allDivs = document.getElementsByClassName('pixel')
    console.log('kolor')

    for (let z = 0; z < allDivs.length; z++) {
        allDivs[z].style.backgroundColor = fetchedData.imageData[z]

    }

}

function generateDiv(width, height) {
    for (let i = 0; i < height; i++) {
        let xDiv = document.createElement('div')
        xDiv.setAttribute('class', 'flexDiv')
        canvas.appendChild(xDiv)
        for (let j = 0; j < width; j++) {
            let hDiv = document.createElement('div')
            hDiv.setAttribute('class', 'pixel')
            xDiv.appendChild(hDiv)
        }
    }
    colorGenDiv()
}

async function fetchData() {
    const URL = 'package.json'
    await fetch(URL)
        .then(response => response.json())
        .then(data => fetchedData = data)
    generateDiv(fetchedData.width, fetchedData.height)

}
