# Global Lightbox - HTML Snippet

Add this HTML snippet at the **bottom of `<body>`** on every page that needs lightbox functionality:

```html
<!-- Global Image Lightbox Viewer -->
<div id="image-lightbox" class="lightbox" onclick="closeLightbox()">
  <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
  <a class="lightbox-prev" id="lightbox-prev" onclick="changeLightboxImage(-1)">&#10094;</a>
  <a class="lightbox-next" id="lightbox-next" onclick="changeLightboxImage(1)">&#10095;</a>
  <img class="lightbox-content" id="lightbox-img" alt="Full screen view">
</div>
```

---

## Include Files

Add these to your page `<head>`:

```html
<!-- Lightbox CSS -->
<link rel="stylesheet" href="css/lightbox.css">
```

Add this before closing `</body>`:

```html
<!-- Global Lightbox JS -->
<script src="js/global-lightbox.js"></script>
```

---

## Initialize for Static Galleries

After including the scripts, initialize for your specific gallery:

### For Standard Gallery Container:
```html
<script>
  // Initialize after DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
    initStaticGallery('.your-gallery-class');
  });
</script>
```

### For Owl Carousel:
```html
<script>
  // Initialize after carousel is ready
  $(document).ready(function() {
    // ... your carousel init ...
    
    // Then initialize lightbox
    initCarouselGallery('#your-carousel-id');
  });
</script>
```

### For Multiple Galleries:
```html
<script>
  document.addEventListener('DOMContentLoaded', function() {
    initStaticGallery('.gallery-1');
    initStaticGallery('.gallery-2');
    initCarouselGallery('#main-slider');
  });
</script>
```

---

## For Dynamic Reviews (Already Handled in JS):

No additional initialization needed - just call:
```javascript
openLightbox(imagesArray, startIndex);
```
