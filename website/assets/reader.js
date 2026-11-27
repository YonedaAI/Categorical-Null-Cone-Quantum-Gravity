// Only equations that need scrolling should interrupt keyboard navigation.
const formulaBoxes = document.querySelectorAll(".mathframe, .inline-math");

function updateKeyboardAccess(box) {
  const scrolls = box.clientWidth > 0 && box.scrollWidth > box.clientWidth + 1;
  if (scrolls) {
    box.tabIndex = 0;
    box.setAttribute("role", "region");
    box.setAttribute("aria-label", "Scrollable mathematical content");
  } else {
    box.removeAttribute("tabindex");
    box.removeAttribute("role");
    box.removeAttribute("aria-label");
  }
}

const observer = new ResizeObserver(entries => {
  for (const entry of entries) updateKeyboardAccess(entry.target);
});
for (const box of formulaBoxes) observer.observe(box);
document.fonts.ready.then(() => formulaBoxes.forEach(updateKeyboardAccess));
