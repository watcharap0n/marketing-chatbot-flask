{% extends 'LINE/layout/layout.html' %}
{% block content %}


  <div id="app">
    <v-app id="inspire">
      <v-container>
        <div class="d-flex flex-column justify-space-between align-center">
          <v-img
              width="360"
              src="/static/images/erp_con.1.png"
          ></v-img>
        </div>
        <v-row justify="center">
          <v-col
              cols="12"
              sm="10"
              md="8"
              lg="6"
          >
            <v-card>
              <v-form
                  ref="form"
                  v-model="valid"
                  lazy-validation
              >
                <v-card-text>
                  <v-text-field
                      dense
                      outlined
                      clearable
                      v-model="formElement.name"
                      :rules="validOther"
                      label="ชื่อผู้ติดต่อ"
                      required
                  ></v-text-field>

                  <v-text-field
                      dense
                      outlined
                      clearable
                      v-model="formElement.company"
                      :rules="validOther"
                      label="บริษัท"
                      required
                  ></v-text-field>

                  <v-text-field
                      dense
                      outlined
                      clearable
                      v-model="formElement.email"
                      :rules="validEmail"
                      label="อีเมล"
                      required
                  ></v-text-field>

                  <v-select
                      dense
                      outlined
                      clearable
                      v-model="formElement.other"
                      :items="products"
                      label="ผลิตภัณฑ์อื่นๆที่ท่านสนใจ"
                      required
                  ></v-select>


                  <v-text-field
                      dense
                      outlined
                      clearable
                      v-model="formElement.tel"
                      :rules="validTel"
                      label="เบอร์ที่สะดวกให้เจ้าหน้าที่ติดต่อกลับ"
                      type="tel"
                      required
                  ></v-text-field>

                  <v-textarea
                      dense
                      outlined
                      v-model="formElement.message"
                      clearable
                      autocomplete
                      label="ข้อมูลที่ท่านต้องการทราบเพิ่มเติม"
                  ></v-textarea>
                  <v-card-actions>
                    <v-btn block
                           :disabled="!valid"
                           :loading="!spinBtn"
                           color="success"
                           class="mr-4"
                           @click="onSubmit"
                    >
                      ยืนยัน
                    </v-btn>
                  </v-card-actions>
                </v-card-text>
              </v-form>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </div>


  {% block script %}
    <script src="/static/js/LINE/construction.js"></script>
  {% endblock %}

{% endblock %}

