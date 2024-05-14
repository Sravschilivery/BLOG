
//                                               ScrollReveal

ScrollReveal({
    reset: true,
    distance: '80px',
    duration: 2000,
    delay: 200
});

ScrollReveal().reveal('.card', { origin: 'bottom' });




//                                               Typed Js


const typed = new Typed('.typedJs', {
    strings: ['The Best Blogging Site...','Read Daily Updated BLogs..','Write Your Blogs Here..'],
    typeSpeed: 60,
    backSpeed: 40,
    backDelay: 2000,
    loop: true,

});