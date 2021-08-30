{% extends "admin/main_layout.html" %}
{% block content %}


  {% include 'public/extends/layout/navigationTop.vue' %}

  <br><br><br>
  <div class="container-fluid">

    <v-row>
      <v-col cols="6">

      </v-col>

      <v-col cols="6">

      </v-col>

    </v-row>


    <v-card class="mx-auto" class="elevation-1">
      <v-bottom-navigation
          style="background: linear-gradient(to right, #7C4DFF, #304FFE, #448AFF);"
          v-model="page"
          dark
          flat
          shift
          class="elevation-1"
      >
        <v-btn v-for="(v, i) in navigation" :key="i" @click="changeTransaction(v.href)">
          <v-badge
              color="pink lighten-2"
              :content="transaction.length"
          >
            <span>[[v.header]]</span>
          </v-badge>
          <v-icon>[[v.icon]]</v-icon>
        </v-btn>
      </v-bottom-navigation>


      <!--     start table     -->
      <v-data-table v-model="selected" :loading="!spinTable" show-select :search="search"
                    :headers="headers"
                    loading-text="Loading... Please wait"
                    class="elevation-5 rounded-xl"
                    height="600"
                    :items="transaction"
                    checkbox-color="pink lighten-2"
      >

        <!--       slot TOP         -->

        {% include 'public/extends/customers/slotTop.vue' %}


        {% include 'public/extends/customers/slotHeader.vue' %}


        {% include 'public/extends/customers/slotItem.vue' %}


        <template v-slot:no-data>
          <v-btn
              color="green accent-1"
              @click="initialize"
          >
            Reset
          </v-btn>
        </template>
      </v-data-table>
    </v-card>


    <v-snackbar
        dark
        :color="colorSb"
        v-model="snackbar"
        :timeout="timeout"
    >
      [[ text ]]

      <template v-slot:action="{ attrs }">
        <v-btn
            dark
            text
            v-bind="attrs"
            @click="snackbar = false"
        >
          ปิด
        </v-btn>
      </template>
    </v-snackbar>




  </div>
  {% block script %}
    <script src="/static/js/customers.js"></script>
  {% endblock %}
{% endblock %}