---
layout: page
title: "Blog Archive"
permalink: /blog-archive/
---
  
<link rel="stylesheet" href="/assets/archive.css" />

<hr class="section-break">
<div id="categories" class="archive-section section-spacing">
  <h2 class="section-heading">Categories</h2>
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
        {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
        <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a><span class="post-meta"> {{ post.date | date: date_format }}</span>
      </article>
      {% endfor %}
    </div>
  {% endfor %}
</div>

<hr class="section-break">
<div class="archive-section section-spacing">
  <details open>
    <summary><h2 class="section-heading">Tags</h2></summary>
    
    <div id="tags" class="tags-container">
      {% assign tags = "" | split:"" %}
      {% for t in site.tags %}
        {% assign tags = tags | push: t[0] %}
      {% endfor %}
      {% assign tags_sorted = tags | sort_natural %}
      {% for tag in tags_sorted %}
        <details class="tag-item">
          <summary>
            <span>{{ tag }} <span class="tag-count">({{site.tags[tag].size}} post{%- if site.tags[tag].size > 1 -%}s{%- endif -%})</span></span>
          </summary>
   
          <div class="tag-posts">
            <a name="{{ tag | slugify }}"></a>
            {% for post in site.tags[tag] %}
            <article class="archive-item">
              {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
              <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a><span class="post-meta"> {{ post.date | date: date_format }}</span>
            </article>
          
            {% endfor %}
          </div>
        </details>
      {% endfor %}
    </div>
    
  </details> 
</div>

<hr class="section-break">
<div id="chronological" class="archive-section section-spacing">
  <h2 class="section-heading">All posts (chronological)</h2>
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
      <hr class="section-break">
    </li>
    {%- endfor -%}
  </ul>
</div>
