window.addEventListener("load", () => {
    const hamburger = document.querySelector(".hamburger");
    hamburger.addEventListener("click", () => {
        const navtl = gsap.timeline();
        navtl.to(".hamburger", { duration: .2, opacity: 0, rotation: -30, display: "none" });
        navtl.to("nav ul", { display: "flex" }, "<+.3");
        navtl.fromTo("nav ul li", { x: 30, opacity: 0 }, { duration: .29, stagger: -.3, x: 0, opacity: 1 }, "<-.2");
        navtl.timeScale(2.85);

        setTimeout(() => {
            navtl.reverse();
        }, 5000);
    })
})