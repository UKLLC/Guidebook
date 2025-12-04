function openDetailsFromHash() {
  const hash = window.location.hash.slice(1);
  if (!hash) return;

  const details = document.getElementById(hash);
  if (details && details.tagName.toLowerCase() === "details") {
    details.open = true;
    // Scroll after a slight delay to ensure browser renders it open
    setTimeout(() => {
      details.scrollIntoView({ behavior: "smooth" });
    }, 50);
    return true;
  }
  return false;
}

// Run on page load and periodically until found
function tryOpenDetails() {
  if (!openDetailsFromHash()) {
    setTimeout(tryOpenDetails, 100); // retry every 100ms until found
  }
}

window.addEventListener("load", tryOpenDetails);
