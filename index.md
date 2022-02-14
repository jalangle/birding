---
Title: Washington State Birding Site Impressions
---

A site dedicated to keeping track of impressions about various birding locations.

# Map
[map](map.html)

# Sites

{% for birding_site in site.sites %}
## [{{birding_site.Name}}]({{site.baseurl}}{{birding_site.url}})

{% endfor %}

# Meta
[Repository]({{site.github.repository_url}}) at [Build Revision]({{site.github.repository_url}}/commit/{{site.github.build_revision}})