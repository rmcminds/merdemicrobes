---
layout: page
title: "Blog Archive"
permalink: /blog-archive/
---

<div id="categories">
  <h3>Categories</h3>
  {% for category in site.categories %}
    <div class="archive-group">
      {% capture category_name %}{{ category | first }}{% endcapture %}
      <div id="#{{ category_name | slugify }}"></div>
      <p></p>
      
      <h3 class="category-head">{{ category_name }}</h3>
      <a name="{{ category_name | slugify }}"></a>
      {% for post in site.categories[category_name] %}
      <article class="archive-item">
        <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
      </article>
      {% endfor %}
    </div>
  {% endfor %}
</div>

<div id="tags">
  <h3>Tags</h3>
  {% for tag in site.tags %}
    <div class="archive-group">
      {% capture tag_name %}{{ tag | first }}{% endcapture %}
      <div id="#{{ tag_name | slugify }}"></div>
      <p></p>

      <h3 class="tag-head">{{ tag_name }}</h3>
      <a name="{{ tag_name | slugify }}"></a>
      {% for post in site.tags[tag_name] %}
      <article class="archive-item">
        <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
      </article>
      {% endfor %}
    </div>
  {% endfor %}
</div>
