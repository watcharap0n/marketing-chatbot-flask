{% extends 'LINE/layout/layout.html' %}
{% block content %}

  <v-container :hidden="!showDashboard">
    <br>
    <h2><strong>Follower Users LINE NOTIFY</strong></h2>
    <v-divider></v-divider>
    <v-card>
      <v-card-title>
        <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
        ></v-text-field>
      </v-card-title>

      <v-card-text>
        <v-data-table
            height="550"
            :headers="headers"
            :items="transaction"
            :search="search"
        >

          <template v-slot:item.img="{item}">
            <v-avatar>
              <img
                  :src="item.img"
                  alt="Image404"
              >
            </v-avatar>
          </template>
          <template v-slot:item.display_name="{item}">
            <v-chip
                class="ma-2"
                label
                small
                color="primary"
            >
              <v-icon left>
                mdi-account
              </v-icon>
              [[item.display_name]]
            </v-chip>
            <br>
            <v-chip
                class="ma-2"
                label
                small
                color="amber"
            >
              [[item.email]]
            </v-chip>
          </template>

          <template v-slot:item.approval_status="{item}">
            <v-checkbox
                v-model="item.approval_status"
                color="success"
                indeterminate
                :label="`${item.approval_status ? 'Approve': 'Disapproved'}`"
                @change="updateObj(item)"
            ></v-checkbox>
          </template>

          <template v-slot:item.role="{item}">

            <v-menu
                bottom
                left
                transition="slide-y-transition"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-chip
                    v-bind="attrs"
                    v-on="on"
                    class="ma-2"
                    dark
                    color="red lighten-1"
                >
                  <v-icon left>
                    mdi-wrench
                  </v-icon>
                  [[item.role]]
                </v-chip>
              </template>
              <v-list>
                <v-list-item @click="roleList = true">
                  <v-list shaped>
                    <v-subheader>Roles</v-subheader>
                    <v-list-item-group
                        v-model="selectedList"
                        color="pink lighten-2"
                    >
                      <v-list-item
                          v-for="(val, i) in roles"
                          :key="i"
                          @click="roleUpdate(item, val)"
                      >
                        <v-list-item-content>
                          <v-list-item-title v-text="val"></v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </v-list-item>
              </v-list>
            </v-menu>
          </template>

          <template v-slot:item.model="{item}">
            <v-list-group
                color="teal darken-2"
                v-if="item.model.length > 0"
                :value="false"
                prepend-icon="mdi-office-building"
            >
              <v-list-item-content>

                <v-chip
                    dark
                    color="teal darken-2"
                    v-for="(val, i) in item.model" :key="i"
                >
                  <v-icon left>
                    mdi-office-building
                  </v-icon>
                  [[val]]
                </v-chip>

              </v-list-item-content>
            </v-list-group>

          </template>

          <template v-slot:item.date="{item}">
            [[ item.date ]]
            <v-divider></v-divider>
            [[ item.time ]]
          </template>

        </v-data-table>
      </v-card-text>
    </v-card>

  </v-container>



  {% block script %}
    <script src="/static/js/notifyMKT/dashboard.js"></script>
  {% endblock %}




{% endblock %}