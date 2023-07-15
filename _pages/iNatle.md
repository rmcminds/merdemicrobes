---
layout: page
title: "iNatle"
permalink: /iNatle/
---

<script type="text/javascript">
  fetch("https://rmcminds.shinyapps.io/inatle/")
  .then(response => {
    return response.text()
  })
  .then(data => {
    document.write(data);
  });
</script>
<noscript>
  iNatle requires javascript
</noscript>

<br>

<a href="https://github.com/rmcminds/iNatle/issues">Tell me about bugs or desired features</a>
