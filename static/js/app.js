const main = () => {
    alert('Hello, World!')

    // Create business account
    const selectExistingCompany = document.getElementById('select-existing-company')
    const selectCustomCompany = document.getElementById('select-custom-company')

    if (selectExistingCompany) {
        selectExistingCompany.addEventListener('click', () => {
            document.getElementById('existing-company').classList.toggle('hidden')
        })
    }
    if (selectCustomCompany) {
        selectCustomCompany.addEventListener('click', () => {
            document.getElementById('custom-company').classList.toggle('hidden')
        })
    }
}

window.addEventListener('load', main)
