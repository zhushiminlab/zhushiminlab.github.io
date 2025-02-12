---
title: Team
nav:
  order: 3
  tooltip: 團隊成員
---

# Team

<center> The Zhu Shimin’s Lab consist of a group of passionate students and post-doc and research assistants.<br>
Our lab has trained a group of people who will always remain part of th extended Zhu Lab family.<br>
數字健康研究實驗室由一群滿懷熱忱的博士生、博士後研究員和研究助理組成.

{% include section.html %}

<h2>Core Members 核心成員</h2>

{% include list.html data="members" component="portrait" filters="role: ld" %}



{% capture content %}

{% include list.html data="members" component="portrait" filters="role: postdoc" %}
{% include list.html data="members" component="portrait" filters="role: phd" %}
{% include list.html data="members" component="portrait" filters="role: research assistant" %}
{% include list.html data="members" component="portrait" filters="role: designer" %}

{% endcapture %}


{% include grid.html style="square" content=content %}



<h2>Special Contributors 特別貢獻者</h2>

<div style="text-align: left;"> Here are some special contributors to our lab's success, whose efforts have been invaluable over the years.<br>
以下是對數字健康研究實驗室作出特別貢獻的人員，他們的努力對我們至關重要。</div>

<ul>
    <li>Voice Actress 配音員: Kong Ming Shan Emma 江銘珊，Shu Ting 舒婷</li>
    <li>Research Assistant 研究助理: Zhuang Yanqiong 莊燕瓊</li>
    <li>Undergraduate Trainee 本科實習生: Zhao Ye 趙燁， Chun Ngai Lam 林峻毅 </li>

</ul>