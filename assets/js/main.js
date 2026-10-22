document.querySelectorAll('.media img').forEach(img=>{const f=()=>img.parentElement.classList.add('noimg');if(img.complete&&!img.naturalWidth)f();img.addEventListener('error',f)});
document.querySelectorAll('.g[data-video]').forEach(card=>{const src=card.dataset.video;if(!src)return;let v;
 card.addEventListener('mouseenter',()=>{if(!matchMedia('(hover:hover)').matches)return;if(!v){v=document.createElement('video');v.src=src;v.muted=true;v.loop=true;v.playsInline=true;card.querySelector('.media').appendChild(v)}v.play().then(()=>card.classList.add('playing')).catch(()=>{})});
 card.addEventListener('mouseleave',()=>{if(v){v.pause();card.classList.remove('playing')}})});
const sub=[...document.querySelectorAll('.sub a[href^="#"]')];
if(sub.length){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)sub.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id))}),{rootMargin:'-35% 0px -60% 0px'});sub.forEach(a=>{const t=document.querySelector(a.getAttribute('href'));t&&io.observe(t)})}

document.querySelectorAll('.showall').forEach(b=>b.addEventListener('click',()=>{const g=b.previousElementSibling;const o=g.classList.toggle('open');b.setAttribute('aria-expanded',o);b.textContent=o?'Show less':'Show all '+g.children.length+' achievements'}));

document.querySelectorAll('.showall').forEach(b=>b.addEventListener('click',()=>{const g=b.previousElementSibling;const o=g.classList.toggle('open');b.setAttribute('aria-expanded',o);b.textContent=o?b.dataset.less:b.dataset.more}));
