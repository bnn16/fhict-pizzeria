const openModalButton = document.getElementById('open-modal');
const modalWindowOverlay = document.getElementById('modal-overlay');
const closeModalButton = document.getElementById('close-modal');


const showModalWindow = () => {
  modalWindowOverlay.style.display = 'flex';
};

const hideModalWindow = () => {
  modalWindowOverlay.style.display = 'none';
};
const hideModalWindowOnBlur = (e) => {
  if (e.target === e.currentTarget) {
    hideModalWindow();
  }
};

closeModalButton.addEventListener('click', hideModalWindow);
openModalButton.addEventListener('click', showModalWindow);
modalWindowOverlay.addEventListener('click', hideModalWindowOnBlur);
