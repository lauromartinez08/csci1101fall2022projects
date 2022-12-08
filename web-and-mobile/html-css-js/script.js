window.addEventListener("load", function ()
{
  let clickButtonElement = document.getElementById("click_button");
  let clickCounterElement = document.getElementById("click_counter");

  let counter = 0;

  let clickButtonFunction = function ()
    {
      counter++
      clickCounterElement.innerHTML = counter;
    };
  
  clickButtonElement.addEventListener("click", clickButtonFunction);
});