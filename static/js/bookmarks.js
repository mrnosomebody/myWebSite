window.onload = function () {
    let categoryPopup = document.querySelector('#add_cat_form')
    let linkPopup = document.querySelector('#add_link_form')
    let addCategory = document.querySelector('#add_category')
    let addLink = document.querySelector('#add_link')
    let closeCatPopup = document.querySelector('#closeCatPopup')
    let closeLinkPopup = document.querySelector('#closeLinkPopup')

    addCategory.addEventListener('click', function () {
        categoryPopup.classList.remove('inactive')
    })

    addLink.addEventListener('click', function () {
        linkPopup.classList.remove('inactive')
    })

    closeCatPopup.addEventListener('click', function () {
        categoryPopup.classList.add('inactive')
    })

    closeLinkPopup.addEventListener('click', function () {
        linkPopup.classList.add('inactive')
    })

}