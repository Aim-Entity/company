function cardAppear(){
  // let card = document.querySelectorAll(".topic-card");
  let dropdown = document.querySelectorAll(".topic-dropdown")

  for(let i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", e => {
      cards = e.target.parentElement.parentElement.children

      for(let j = 1; j < cards.length; j++) {
        // cards[j].style.display = "block"
        cards[j].classList.toggle("card-appear");
        cards[j].classList.toggle("topic-card");
      }
    })
  }
};

function cardExpand() {
  let expand = document.querySelectorAll(".tc-btn");

  for(let i = 0; i < expand.length; i++) {
    expand[i].addEventListener("click", e => {
      text = e.target.parentElement.parentElement.children[1];
      text.classList.toggle("tc-text-appear");
      // text.classList.toggle("tc-text");
    })
  };
};

cardExpand()
cardAppear()