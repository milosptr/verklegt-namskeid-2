const main = () => {

    // Create business account
    const selectExistingCompany = document.getElementById('select-existing-company')
    const selectCustomCompany = document.getElementById('select-custom-company')
    const existingCompanySection = document.getElementById('existing-company')
    const customCompanySection = document.getElementById('custom-company')

    if (selectExistingCompany) {
        selectExistingCompany.addEventListener('click', () => {
            selectExistingCompany.classList.add('bg-[#6C37BD]')
            selectCustomCompany.classList.remove('bg-[#6C37BD]')
            existingCompanySection.classList.remove('hidden')
            customCompanySection.classList.add('hidden')

            existingCompanySection.querySelectorAll('input').forEach((input) => {
                input.required = true
            })
            existingCompanySection.querySelectorAll('select').forEach((select) => {
                select.required = true
            })
            customCompanySection.querySelectorAll('input').forEach((input) => {
                input.required = false
            })
            customCompanySection.querySelectorAll('select').forEach((select) => {
                select.required = false
            })
            customCompanySection.querySelectorAll('textarea').forEach((select) => {
                select.required = false
            })
        })
    }
    if (selectCustomCompany) {
        selectCustomCompany.addEventListener('click', () => {
            selectCustomCompany.classList.add('bg-[#6C37BD]')
            selectExistingCompany.classList.remove('bg-[#6C37BD]')
            existingCompanySection.classList.add('hidden')
            customCompanySection.classList.remove('hidden')

            existingCompanySection.querySelectorAll('input').forEach((input) => {
                input.required = false
            })
            existingCompanySection.querySelectorAll('select').forEach((select) => {
                select.required = false
            })
            customCompanySection.querySelectorAll('input').forEach((input) => {
                input.required = true
            })
            customCompanySection.querySelectorAll('select').forEach((select) => {
                select.required = true
            })
            customCompanySection.querySelectorAll('textarea').forEach((select) => {
                select.required = true
            })
        })
    }
}

window.addEventListener('load', main)
