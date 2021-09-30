{% extends 'LINE/layout/layout.html' %}
{% block content %}

  <v-container>
    <br>
    [[user]]
    <h2><strong>Select Product | LINE NOTIFY</strong></h2>
    <v-divider></v-divider>
    <v-card>
      <v-card-text>
        <v-row>
          <v-col cols="12">
            <v-combobox
                v-model="user.model"
                :items="products"
                label="Combobox"
                multiple
                outlined
                dense
            ></v-combobox>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <template>
          <v-btn block color="success" @click="save">
            Accept
          </v-btn>
        </template>
      </v-card-actions>
    </v-card>
  </v-container>





  {% block script %}
    <script src="/static/js/notifyMKT/selectedNotify.js"></script>
  {% endblock %}




{% endblock %}

