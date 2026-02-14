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
  <h2 class="section-heading">Tags</h2>
  
  <div id="tags" class="tags-container">
    {% comment %} Create array of tags with their counts for sorting {% endcomment %}
    {% assign tag_array = "" | split: "" %}
    {% for t in site.tags %}
      {% assign tag_item = t[0] | append: "|" | append: t[1].size %}
      {% assign tag_array = tag_array | push: tag_item %}
    {% endfor %}
    
    {% comment %} Sort tags by count (we'll reverse later for descending order) {% endcomment %}
    {% assign sorted_tags = tag_array | sort %}
    {% assign sorted_tags = sorted_tags | reverse %}
    
    {% comment %} Display top 3 most common tags (always visible) {% endcomment %}
    {% for i in (0..2) %}
      {% if sorted_tags[i] %}
        {% assign tag_parts = sorted_tags[i] | split: "|" %}
        {% assign tag = tag_parts[0] %}
        {% assign count = tag_parts[1] %}
        <details class="tag-item">
          <summary>
            <span>{{ tag }} <span class="tag-count">({{ count }} post{%- if count > "1" -%}s{%- endif -%})</span></span>
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
      {% endif %}
    {% endfor %}
    
    {% comment %} Collapsible section for remaining tags {% endcomment %}
    {% if sorted_tags.size > 3 %}
      <details class="more-tags-wrapper">
        <summary class="more-tags-summary">
          <span class="more-tags-text">Show {{ sorted_tags.size | minus: 3 }} more tags...</span>
        </summary>
        
        <div class="more-tags-content">
          {% for i in (3..1000) %}
            {% if sorted_tags[i] %}
              {% assign tag_parts = sorted_tags[i] | split: "|" %}
              {% assign tag = tag_parts[0] %}
              {% assign count = tag_parts[1] %}
              <details class="tag-item">
                <summary>
                  <span>{{ tag }} <span class="tag-count">({{ count }} post{%- if count > "1" -%}s{%- endif -%})</span></span>
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
            {% endif %}
          {% endfor %}
        </div>
      </details>
    {% endif %}
  </div>
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
