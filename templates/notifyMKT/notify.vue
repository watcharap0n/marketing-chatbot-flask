{% extends 'LINE/layout/layout.html' %}
{% block content %}

  <v-container>
    <br>
    <h2><strong>Select Product | LINE NOTIFY</strong></h2>
    <v-divider></v-divider>
    <v-card>
      <v-card-text>
        <v-row>

          <v-col cols="12"
                 sm="12">
            <v-combobox
                v-model="user.model_subject"
                :items="subjects"
                label="Subjects | Helpdesk"
                multiple
                outlined
                hint="Select subject for get notify"
                persistent-hint
                dense
            ></v-combobox>
          </v-col>

          <v-col cols="12"
                 sm="12">
            <v-combobox
                v-model="user.model"
                :items="products"
                label="Products | MKT"
                multiple
                outlined
                dense
                hint="Select product for get notify"
                persistent-hint
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

