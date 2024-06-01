const hamburgerMenu = document.querySelector('#hamburger-menu');
const closeBtn = document.querySelector('#close-btn');
const navbar = document.getElementById('navbar');
const featuresBtn = document.querySelector('#features-btn');
const featuresUl = document.querySelector('#features-ul');
const companyUl = document.querySelector('#company-ul');
const companyBtn = document.querySelector('#company-btn');

hamburgerMenu.addEventListener('click', ()=>{
    navbar.style.display = 'block'
})

closeBtn.addEventListener('click', ()=>{
    navbar.style.display = 'none'
})

featuresBtn,addEventListener('click', ()=>{
    featuresUl.style.display = (featuresUl.style.display === 'block') ? 'none' : 'block'
})

companyBtn,addEventListener('click', ()=>{
    companyUl.style.display = (companyUl.style.display === 'block') ? 'none' : 'block'
})
