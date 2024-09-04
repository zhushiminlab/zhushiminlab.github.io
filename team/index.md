---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# Team

<center> The Zhu Shimin’s Lab consist of a group of passionate students and post-doc and research assistants.<br>
Our lab has trained over 50 people who will always remain part of th extended Zhu Lab family.<br>
我們的實驗室由一群滿懷熱忱的博士生、博士後研究員和研究助理組成.

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}

{% include section.html background="images/background.jpg" dark=true %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{% include section.html %}

{% capture content %}

{% include list.html data="members" component="portrait" filters="role: postdoc" %}
{% include list.html data="members" component="portrait" filters="role: phd" %}
{% include list.html data="members" component="portrait" filters="role: postgrade" %}
{% include list.html data="members" component="portrait" filters="role: designer" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
