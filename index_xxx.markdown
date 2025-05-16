---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

---
layout: default
title: Frankie Spring Books
---

<h2>All Books</h2>
<div class="book-grid">
  {% for book in site.books %}
  <div class="book-box">
    <a href="{{ book.url }}">
      <img src="{{ book.cover }}" alt="{{ book.title }}" width="200">
    </a>
    <p>{{ book.title }}</p>
  </div>
  {% endfor %}
</div>
