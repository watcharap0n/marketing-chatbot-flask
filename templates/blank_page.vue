{% extends "admin/main_layout.html" %}
{% block content %}

  {% include 'public/extends/layout/navigationTop.vue' %}

  <br><br><br>
  <div class="container-fluid">

  </div>

  {% block footer %}
    {% include 'public/extends/layout/footer.vue' %}
  {% endblock %}


  {% block script %}
    <script src="/static/js/blank.js"></script>
  {% endblock %}




{% endblock %}