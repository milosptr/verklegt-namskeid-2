const main = () => {

    // Profile page
    // Skills
    const addSkillsButton = document.getElementById('add-skill')
    const skillsModal = document.getElementById('skill-modal')
    const skillsModalClose = document.getElementById('close-skill-modal')
    if(addSkillsButton) {
        addSkillsButton.addEventListener('click', () => {
            skillsModal.classList.remove('hidden')
        })
        skillsModalClose.addEventListener('click', () => {
            skillsModal.classList.add('hidden')
        })
    }
    // Experience
    const addExperienceButton = document.getElementById('add-experience')
    const experienceModal = document.getElementById('experience-modal')
    const experienceModalClose = document.getElementById('close-experience-modal')
    if(addExperienceButton) {
        addExperienceButton.addEventListener('click', () => {
            experienceModal.classList.remove('hidden')
        })
        experienceModalClose.addEventListener('click', () => {
            experienceModal.classList.add('hidden')
        })
    }
    // Recommendation
    const addRecommendationButton = document.getElementById('add-recommendation')
    const recommendationModal = document.getElementById('recommendation-modal')
    const recommendationModalClose = document.getElementById('close-recommendation-modal')
    if(addRecommendationButton) {
        addRecommendationButton.addEventListener('click', () => {
            recommendationModal.classList.remove('hidden')
        })
        recommendationModalClose.addEventListener('click', () => {
            recommendationModal.classList.add('hidden')
        })
    }
    // CV
    const addCVButton = document.getElementById('add-cv')
    const cvModal = document.getElementById('cv-modal')
    const cvModalClose = document.getElementById('close-cv-modal')
    if(addCVButton) {
        addCVButton.addEventListener('click', () => {
            cvModal.classList.remove('hidden')
        })
        cvModalClose.addEventListener('click', () => {
            cvModal.classList.add('hidden')
        })
    }

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
