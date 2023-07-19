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
  {% for tag in site.tags %}
    <div class="archive-group">
      {% capture tag_name %}{{ tag | first }}{% endcapture %}
      <div style="background-color: lightgrey" id="#{{ tag_name | slugify }}"></div>
      <p></p>
      
      <details>
        <h4 class="tag-head"><summary>{{ tag_name }}</summary></h4>
        
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
