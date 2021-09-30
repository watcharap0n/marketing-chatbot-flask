{% extends 'LINE/layout/layout.html' %}
{% block content %}


  <div id="app">
    <v-app id="inspire">
      <v-container>
        [[formElement]]
      </v-container>
    </v-app>
  </div>


  {% block script %}
    <script src="/static/js/notifyMKT/dashboard.js"></script>
  {% endblock %}

{% endblock %}

