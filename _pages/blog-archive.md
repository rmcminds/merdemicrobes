---
layout: page
title: "Blog Archive"
permalink: /blog-archive/
---

<div id="categories" style="padding-bottom:30px">
  <h3>Categories</h3>
  {% assign categories = "" | split:"" %}
  {% for c in site.categories %}
    {% assign categories = categories | push: c[0] %}
  {% endfor %}
  {% assign categories_sorted = categories | sort_natural %}
  {% for category in categories_sorted %}
    <div class="archive-group">
      {% capture category_name %}{{ category | first }}{% endcapture %}
      <div id="#{{ category_name | slugify }}"></div>
      <p></p>
      
      <h4 class="category-head">{{ category_name }}</h4>
      <a name="{{ category_name | slugify }}"></a>
      {% for post in site.categories[category_name] %}
      <article class="archive-item">
        <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a>
      </article>
      {% endfor %}
    </div>
  {% endfor %}
</div>

<hr style="border-top: 1px solid #e1e4e8; border-right: none; border-bottom: none; border-left: none;">
<div id="tags" style="padding-top:30px">
  <h3>Tags</h3>
  {% assign tags = "" | split:"" %}
  {% for t in site.tags %}
    {% assign tags = tags | push: t[0] %}
  {% endfor %}
  {% assign tags_sorted = tags | sort_natural %}
  {% for tag in tags_sorted %}
    <div class="archive-group" style="background-color: #e1e4e8; border-radius: 5px">
      {% capture tag_name %}{{ tag | first }}{% endcapture %}
      <div id="#{{ tag_name | slugify }}"></div>
      <p></p>
      
      <details>
        <summary>{{ tag_name }}</summary>
        
        <a name="{{ tag_name | slugify }}"></a>
        {% for post in site.tags[tag_name] %}
        <article class="archive-item">
          <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a>
        </article>
      
        {% endfor %}
      </details>
    </div>
  {% endfor %}
</div>

<hr style="border-top: 1px solid #e1e4e8; border-right: none; border-bottom: none; border-left: none;">
<div id="chronological" style="padding-top:30px">
    <ul class="post-list">
      {%- for post in site.posts -%}
      <li>
        {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
        <span class="post-meta">{{ post.date | date: date_format }}</span>
        <h3>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
        </h3>
        {%- if site.show_excerpts -%}
          {{ post.excerpt }}
        {%- endif -%}
        <hr style="border-top: 1px solid #e1e4e8; border-right: none; border-bottom: none; border-left: none;">
      </li>
      {%- endfor -%}
    </ul>
</div>
