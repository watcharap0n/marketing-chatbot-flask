{% extends "admin/main_layout.html" %}
{% block content %}

  {% include 'public/extends/layout/navigationTop.vue' %}

  <br><br><br>
  <div class="container-fluid">
    <v-row>
      <v-col cols="8">
        <v-card class="mx-auto overflow-y-auto elevation-1">
          <v-data-table
              :loading="!spinTable"
              :headers="headers"
              loading-text="Loading... Please wait"
              class="elevation-5 overflow-y-auto"
              :items="transaction"
              checkbox-color="pink lighten-2"
              height="350"
          >
            {% include 'public/extends/customers/slotHeader.vue' %}

            <template v-slot:top>
              <v-toolbar flat>
                <strong>ข้อมูลลูกค้า</strong>
              </v-toolbar>
            </template>

            <template v-slot:item.tag="{item}">
              <v-chip
                  dark
                  color="red"
                  class="ma-2"
                  v-for="i in item.tag" :key="i.length"
              >

                [[ i ]]
              </v-chip>
            </template>

            <template v-slot:item.product="{item}">
              <v-chip class="ma-2" :color="colorProduct(item.product)" label>
                <div v-if="item.product === 'Construction'">
                  <strong style="color: green">[[item.product]]</strong>
                </div>

                <div v-else-if="item.product === 'RealEstate'">
                  <strong style="color: blue">[[item.product]]</strong>
                </div>

                <div v-else-if="item.product === 'Project Planning'">
                  <strong style="color: deeppink">[[item.product]]</strong>
                </div>

                <div v-else-if="item.product === 'Consulting'">
                  <strong style="color: black">[[item.product]]</strong>
                </div>

                <div v-else>
                  <strong>[[item.product]]</strong>
                </div>
              </v-chip>
            </template>

            <template v-slot:item.name="{item}">
              <div style="margin-top: 15px; margin-bottom: 15px">
                <v-row>
                  <v-col>
                    <strong>[[item.name ]]</strong>
                    <span>[[item.email ]]</span>
                    <span>[[item.tel ]]</span>

                    <v-list-group
                        dense
                        color="red lighten-2"
                        v-if="item.person_id || item.tax_id"
                        :value="false"
                        prepend-icon="mdi-card-account-details-outline"
                    >
                      <v-list-item-content>
                        <span v-if="item.person_id"> <strong>เลขที่บัตรประชาชน</strong> [[item.person_id]]</span>
                        <span v-if="item.tax_id"> <strong>เลขที่เสียภาษี</strong> [[item.tax_id]]</span>

                      </v-list-item-content>
                    </v-list-group>
                    <div v-else></div>

                  </v-col>
                </v-row>
              </div>
            </template>


            <template v-slot:item.message="{item}">
              <v-list-group
                  color="#7A8FC0"
                  v-if="item.message"
                  :value="false"
                  prepend-icon="mdi-message"
              >
                <v-list-item-content>
                  [[item.message]]
                </v-list-item-content>
              </v-list-group>
              <div v-else></div>
            </template>


            <template v-slot:item.channel="{item}">
              <div v-if="item.channel === 'Contact'">
                <v-chip outlined color="blue darken-2">
                  [[item.channel ]]
                </v-chip>
              </div>

              <div v-else-if="item.channel === 'GetDemo'">
                <v-chip outlined color="pink lighten-2">
                  [[item.channel ]]
                </v-chip>
              </div>

              <div v-else-if="item.channel === 'LINE'">
                <v-chip outlined color="green accent-4">
                  [[item.channel ]]
                </v-chip>
              </div>

              <div v-else>
                <v-chip outlined>
                  [[item.channel ]]
                </v-chip>
              </div>
            </template>

          </v-data-table>
        </v-card>
      </v-col>
      <v-col cols="4">
        <v-card
            elevation="2"
            class="mx-auto overflow-y-auto"
            max-width="520"

        >
          <v-card-text>
            <apexcharts ref="chart" width="500" height="420" type="bar" :options="chartOptions" :series="series">
            </apexcharts>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <br>
    <v-row>
      <v-col cols="4">
        <v-card
            elevation="2"
            class="mx-auto overflow-y-auto"
            max-width="600"

        >
          <v-card-text>
            <apexcharts ref="chartInitialized" width="500" height="350" type="bar" :options="chartOptionsInit"
                        :series="seriesInit">
            </apexcharts>

            <v-dialog
                v-model="dialogChart"
                width="500"
                persistent
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                    style="margin-left: 10px; margin-top: -10px"
                    color="pink lighten-2"
                    dark
                    v-bind="attrs"
                    v-on="on"
                    small
                >
                  <v-icon>
                    mdi-chart-arc
                  </v-icon>
                </v-btn>
              </template>
              <v-card>
                <v-card-title class="headline grey lighten-2">
                  ข้อมูลในการกรอง
                </v-card-title>

                <v-card-text>
                  <v-select
                      v-model="selectedProduct"
                      :items="products"
                      label="ผลิตภัณฑ์"
                  ></v-select>
                  <v-select
                      v-model="selectedChannel"
                      :items="channels"
                      label="ช่องทาง"
                  ></v-select>
                </v-card-text>
                <v-card-actions>
                  <v-btn color="success" @click="conditionChart" :loading="!spinChart">
                    ตกลง
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="8">
        <v-card
            elevation="2"
            class="mx-auto overflow-y-auto"
        >
          <v-card-text>
            <apexcharts ref="chartDay" width="1500" height="300" type="line" :options="chartOptionsDay"
                        :series="seriesDay">
            </apexcharts>
            <v-row>
              <v-col cols="4">
                <v-select
                    v-model="selectedChannel"
                    :items="channels"
                    label="ผลิตภัณฑ์"
                ></v-select>
              </v-col>
              <v-col cols="4">
                <v-select
                    v-model="selectedMonth"
                    :items="months"
                    label="เดือน"
                ></v-select>
              </v-col>
              <v-col cols="4">
                <v-btn color="success" @click="conditionDay" :loading="!spinChart">
                  ตกลง
                </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <br>
    <br>
  </div>

  {% block footer %}
    {% include 'public/extends/layout/footer.vue' %}
  {% endblock %}


  {% block script %}
    <script src="/static/js/dashboard.js"></script>
  {% endblock %}

  <style>
      #chart {
          max-width: 650px;
          margin: 35px auto;
      }

  </style>



{% endblock %}