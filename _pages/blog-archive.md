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
    {% comment %} Define number of top tags to always display {% endcomment %}
    {% assign top_tags_count = 3 %}
    
    {% comment %} Create array of tags with their counts for sorting {% endcomment %}
    {% assign tag_array = "" | split: "" %}
    {% for t in site.tags %}
      {% comment %} Zero-pad count to 5 digits for correct numerical sorting {% endcomment %}
      {% assign count_padded = "" %}
      {% assign count_str = t[1].size | append: "" %}
      {% assign padding_needed = 5 | minus: count_str.size %}
      {% for j in (1..padding_needed) %}
        {% assign count_padded = count_padded | append: "0" %}
      {% endfor %}
      {% assign count_padded = count_padded | append: count_str %}
      {% assign tag_item = count_padded | append: "|" | append: t[0] %}
      {% assign tag_array = tag_array | push: tag_item %}
    {% endfor %}
    
    {% comment %} Sort tags by padded count (descending order via reverse) {% endcomment %}
    {% assign sorted_tags = tag_array | sort | reverse %}
    
    {% comment %} Display top N most common tags (always visible) {% endcomment %}
    {% assign max_top = top_tags_count | minus: 1 %}
    {% for i in (0..max_top) %}
      {% if sorted_tags[i] %}
        {% assign tag_parts = sorted_tags[i] | split: "|" %}
        {% assign count = tag_parts[0] | plus: 0 %}
        {% assign tag = tag_parts[1] %}
        <details class="tag-item">
          <summary>
            <span>{{ tag }} <span class="tag-count">({{ count }} post{%- if count > 1 -%}s{%- endif -%})</span></span>
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
    {% if sorted_tags.size > top_tags_count %}
      <details class="more-tags-wrapper">
        <summary class="more-tags-summary">
          <span class="more-tags-text">Show {{ sorted_tags.size | minus: top_tags_count }} more tags...</span>
        </summary>
        
        <div class="more-tags-content">
          {% assign max_index = sorted_tags.size | minus: 1 %}
          {% for i in (top_tags_count..max_index) %}
            {% if sorted_tags[i] %}
              {% assign tag_parts = sorted_tags[i] | split: "|" %}
              {% assign count = tag_parts[0] | plus: 0 %}
              {% assign tag = tag_parts[1] %}
              <details class="tag-item">
                <summary>
                  <span>{{ tag }} <span class="tag-count">({{ count }} post{%- if count > 1 -%}s{%- endif -%})</span></span>
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
