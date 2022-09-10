let classes = ["f0", "f1", "f2", "f3", "f4"];
let classIndex = 2;

document.getElementById('aumentar').addEventListener('click', ()=>{
    let previousClass = classIndex;
    classIndex++;
    classIndex = (classIndex== classes.length) ? classes.length - 1: classIndex;
    changeClass(previousClass, classIndex ); 
});

document.getElementById('disminuir').addEventListener('click', ()=>{
    let previousClass = classIndex;
    classIndex--;
    classIndex = (classIndex < 0) ? 0 : classIndex;
    changeClass(previousClass, classIndex);
});

let changeClass = (previous, next)=>{
    if(previous != next){
        let htmlElement = document.querySelector('html');
        htmlElement.classList.remove(classes[previous]);
        htmlElement.classList.add(classes[next]);
        
    }
}
document.getElementById('restaurar').addEventListener( 'click', ()=>{
    location.reload();
});
changeClass()
const cuerpo = document.body;
document.getElementById('dark').addEventListener('click',()=>{ 
    cuerpo.classList.toggle('dark-mode');
 });


 var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

// Change the icons inside the button based on previous settings
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIcon.classList.remove('hidden');
} else {
    themeToggleDarkIcon.classList.remove('hidden');
}

var themeToggleBtn = document.getElementById('theme-toggle');

themeToggleBtn.addEventListener('click', function() {

    // toggle icons inside button
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');

    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        }

    // if NOT set via local storage previously
    } else {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        }
    }
    
});

