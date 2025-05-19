---
layout: home
title: Frankie Spring’s Coloring Books
---

Welcome to the creative world of **Frankie Spring**!

Explore my books :
<ul>
  {% for book in site.data.books %}
    <li>
      <a href="/{{ book.slug }}/">
        <img src="{{ book.cover_image }}" alt="{{ book.title }}" width="150"/>
        <h2>{{ book.title }}</h2>
        <p>{{ book.subtitle }}</p>
      </a>
    </li>
  {% endfor %}
</ul>
