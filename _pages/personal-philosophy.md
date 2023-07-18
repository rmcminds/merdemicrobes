---
layout: page
title: Personal Philosophy
permalink: /about/personal-philosophy/
---

<ul class="post-list">
  {% for post in site.categories.personal-philosophy %}
   <li>
    {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
    <span class="post-meta">{{ post.date | date: date_format }}</span>
    <h3>
      <a class="post-link" href="{{ post.url | relative_url }}">
        {{ post.title | escape }}
      </a>
    </h3>
    {{ post.excerpt }}
    <hr style="border-top: 1px solid #e1e4e8; border-right: none; border-bottom: none; border-left: none;">
  {% endfor %}
</ul>
