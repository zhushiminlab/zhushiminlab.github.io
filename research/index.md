---
title: Publications
nav:
  order: 2
  tooltip: 論文發表
---

# Our Publications

<center>
Our publications focus on the overall well-being of children and adolescents.<br>
我們的文章關注並致力於提升兒童與青少年的整體健康。

</center>

<!--
<div style="text-align: center; margin: 40px 0;">
  <img src="{{ '/images/roadmap.png' | relative_url }}" alt="Lab Research Roadmap" style="max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);" />
</div>
-->

{% include section.html %}


## Featured Papers
{% include list.html data="citations" component="citation" filters="status: Featured" style="rich" section="featured" %}

## All

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="rich" section="all" %}
