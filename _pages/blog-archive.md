---
layout: page
title: "Blog Archive"
permalink: /blog-archive/
---

<div id="categories" style="padding-bottom:30px">
  <h3>Categories</h3>
  {% assign categories_sorted = site.categories | sort %}
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
  {% assign tags_sorted = site.tags | sort %}
  {% for tag in tags_sorted %}
    <div class="archive-group" style="background-color: lightgrey">
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
