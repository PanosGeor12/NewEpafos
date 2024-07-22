const navTexts = document.querySelectorAll('.links_text');
const navLinks = document.querySelectorAll('.links');
let icons = document.querySelectorAll('i');
let profile = document.querySelector('.profile_name');
let navbar = document.querySelector('.sidebar');
let schoolName = document.querySelector('#schoolName');
let mainContent = document.querySelector('.main-content');
let toggleButton = document.querySelector('#toggleBtn');
let isSideBarCollapsed;

window.addEventListener('load', ()=>{
  collapseSidebar();
  isSideBarCollapsed = true;
});

toggleButton.addEventListener('click', ()=>{
  if(isSideBarCollapsed != true){
    collapseSidebar();
    isSideBarCollapsed = true;
  }
  else{
    expandSidebar();
    isSideBarCollapsed = false;
  }
});
  
function collapseSidebar(){
  for(let i=0; i<4; i++){
    navTexts[i].classList.remove('expanded')
    navTexts[i].classList.add('collapsed')
    navLinks[i].style.width = '50px';
  } 
  profile.textContent = '';
  schoolName.textContent = '';
  navbar.style.width = '80px';
  mainContent.style.marginLeft = '100px'; 
  toggleButton.classList.add('collapsedBtn');
  toggleButton.classList.remove('expandedBtn');
}

let profileName = profile.textContent;
let clonedName = schoolName.textContent;

function expandSidebar(){
  for(let i=0; i<4; i++){
    navTexts[i].classList.remove('collapsed')
    navTexts[i].classList.add('expanded')
    navLinks[i].style.width = '250px';
  }
  profile.textContent = profileName;
  schoolName.textContent = clonedName;
  navbar.style.width = '280px';
  mainContent.style.marginLeft = '290px';
  toggleButton.classList.add('expandedBtn');
  toggleButton.classList.remove('collapsedBtn'); 
}

