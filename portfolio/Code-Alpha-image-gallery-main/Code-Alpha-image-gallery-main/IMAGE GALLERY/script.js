function viewImage(imgElement) {
    const popup = document.getElementById("popup");
    const popupImg = document.getElementById("popup-img");
  
    popup.style.display = "flex";
    popupImg.src = imgElement.src;
  }
  
  function closePopup() {
    document.getElementById("popup").style.display = "none";
  }
  
  // Filter Function
  function filterGallery(type) {
    const images = document.querySelectorAll(".box");
    images.forEach(img => {
      if (img.getAttribute("data-type") === type) {
        img.style.display = "block";
      } else {
        img.style.display = "none";
      }
    });
  }
  
  function showAll() {
    const images = document.querySelectorAll(".box");
    images.forEach(img => {
      img.style.display = "block";
    });
  }