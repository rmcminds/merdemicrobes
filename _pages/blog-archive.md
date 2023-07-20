---
layout: page
title: "Blog Archive"
permalink: /blog-archive/
---
  
<link rel="stylesheet" href="/assets/archive.css" />

<hr style="border-top: 1px solid #e1e4e8; border-right: none; border-bottom: none; border-left: none;">
<div id="categories" style="padding-top:30px; padding-bottom:30px">
  <h3>Categories</h3>
  {% assign categories = "" | split:"" %}
  {% for c in site.categories %}
    {% assign categories = categories | push: c[0] %}
  {% endfor %}
  {% assign categories_sorted = categories | sort_natural %}
  {% for category in categories_sorted %}
    <div class="archive-group">
      <div id="#{{ category | slugify }}"></div>
      <p></p>
      
      <h4 class="category-head">{{ category }}</h4>
      <a name="{{ category | slugify }}"></a>
      {% for post in site.categories[category] %}
      <article class="archive-item">
        <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a>
      </article>
      {% endfor %}
    </div>
  {% endfor %}
</div>

<hr style="border-top: 1px solid #e1e4e8; border-right: none; border-bottom: none; border-left: none;">
<details>
  <summary style="display: inline"><h3>Tags</h3></summary>
  
  <div id="tags" style="padding-top:30px; padding-bottom:30px; margin:5px">
    {% assign tags = "" | split:"" %}
    {% for t in site.tags %}
      {% assign tags = tags | push: t[0] %}
    {% endfor %}
    {% assign tags_sorted = tags | sort_natural %}
    {% for tag in tags_sorted %}
      <div class="archive-group" style="background-color: #e1e4e8; border-radius: 5px; padding: 5px; margin-top: 5px">
        <div id="#{{ tag | slugify }}"></div>
        
        <details>
          <summary>{{ tag }} ({{site.tags[tag].size}} posts)</summary>
  
          <div style="background-color: white; border-radius: 5px; padding-left: 5px">
          <a name="{{ tag | slugify }}"></a>
          {% for post in site.tags[tag] %}
          <article class="archive-item">
            {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
            <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a><span> {{ post.date | date: date_format }}</span>
          </article>
        
          {% endfor %}
          </div>
        </details>
        
      </div>
    {% endfor %}
  </div>
  
</details> 

<hr style="border-top: 1px solid #e1e4e8; border-right: none; border-bottom: none; border-left: none;">
<div id="chronological" style="padding-top:30px">
  <h3>All (chronological)</h3>
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
