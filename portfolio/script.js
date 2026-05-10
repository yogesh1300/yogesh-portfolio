const navLinks = document.getElementById('navLinks');
const navToggle = document.getElementById('navToggle');

navToggle?.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});

// Screenshot Modal
const screenshotModal = document.getElementById('screenshotModal');
const modalImage = document.getElementById('modalImage');
const modalTitle = document.getElementById('modalTitle');
const modalCaption = document.getElementById('modalCaption');
const modalClose = document.getElementById('modalClose');
const modalViewLive = document.getElementById('modalViewLive');
const modalViewGithub = document.getElementById('modalViewGithub');
const modalPrev = document.getElementById('modalPrev');
const modalNext = document.getElementById('modalNext');
const screenshotButtons = document.querySelectorAll('.screenshot-btn');

let currentImageIndex = 0;
let currentProject = null;

// Store project data for navigation
const projectsData = Array.from(screenshotButtons).map(btn => ({
  screenshot: btn.dataset.screenshot,
  title: btn.dataset.title,
  description: btn.dataset.description,
  demo: btn.dataset.demo,
  github: btn.dataset.github
}));

// Open modal
screenshotButtons.forEach((btn, index) => {
  btn.addEventListener('click', () => {
    currentProject = index;
    currentImageIndex = 0;
    loadProjectScreenshot(index);
    screenshotModal.classList.add('open');
    screenshotModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  });
});

function loadProjectScreenshot(projectIndex) {
  if (projectIndex < 0 || projectIndex >= projectsData.length) return;
  
  const project = projectsData[projectIndex];
  modalImage.src = project.screenshot;
  modalTitle.textContent = project.title;
  modalCaption.textContent = project.description;
  
  // Handle demo link
  if (project.demo && project.demo !== '#') {
    modalViewLive.href = project.demo;
    modalViewLive.style.display = 'inline-flex';
  } else {
    modalViewLive.style.display = 'none';
  }
  
  // Handle github link
  if (project.github && project.github !== '#') {
    modalViewGithub.href = project.github;
    modalViewGithub.style.display = 'inline-flex';
  } else {
    modalViewGithub.style.display = 'none';
  }
  
  currentProject = projectIndex;
}

// Navigation
modalPrev.addEventListener('click', () => {
  const prevIndex = (currentProject - 1 + projectsData.length) % projectsData.length;
  loadProjectScreenshot(prevIndex);
});

modalNext.addEventListener('click', () => {
  const nextIndex = (currentProject + 1) % projectsData.length;
  loadProjectScreenshot(nextIndex);
});

// Close modal
function closeModal() {
  screenshotModal.classList.remove('open');
  screenshotModal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

modalClose.addEventListener('click', closeModal);

// Close modal on background click
document.getElementById('modalOverlay').addEventListener('click', closeModal);

// Close modal on Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && screenshotModal.classList.contains('open')) {
    closeModal();
  } else if (e.key === 'ArrowLeft' && screenshotModal.classList.contains('open')) {
    modalPrev.click();
  } else if (e.key === 'ArrowRight' && screenshotModal.classList.contains('open')) {
    modalNext.click();
  }
});

const sections = document.querySelectorAll('section');
const observer = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  },
  { threshold: 0.12 }
);

sections.forEach(section => observer.observe(section));
