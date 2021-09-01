{% extends 'LINE/layout/layout.html' %}
{% block content %}


  <div id="app">
    <v-app id="inspire">
      <input type="hidden" value="{{ id }}" ref="formId"/>
      <v-container>
        <div class="d-flex flex-column justify-space-between align-center">
          <v-img
              width="200"
              src="/static/images/mango-profile.jpg"
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
                      :label="form.name"
                      required
                  ></v-text-field>

                  <v-text-field
                      dense
                      outlined
                      clearable
                      v-model="formElement.company"
                      :rules="validOther"
                      :label="form.company"
                      required
                  ></v-text-field>

                  <v-text-field
                      dense
                      outlined
                      clearable
                      v-model="formElement.email"
                      :rules="validEmail"
                      :label="form.email"
                      required
                  ></v-text-field>

                  <v-select
                      dense
                      outlined
                      clearable
                      v-model="formElement.product"
                      :items="form.itemProducts"
                      :rules="validSelect"
                      :label="form.product"
                      required
                  ></v-select>


                  <v-text-field
                      dense
                      outlined
                      clearable
                      v-model="formElement.tel"
                      :rules="validTel"
                      :label="form.tel"
                      type="tel"
                      required
                  ></v-text-field>

                  <v-textarea
                      dense
                      outlined
                      v-model="formElement.message"
                      clearable
                      autocomplete="email"
                      :label="form.message"
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
      <v-overlay :value="!spinPage">
        <v-progress-circular
            color="pink lighten-2"
            indeterminate
            size="64"
        ></v-progress-circular>
      </v-overlay>
    </v-app>
  </div>

  {% block script %}
    <script src="/static/js/page_custom.js"></script>
  {% endblock %}

{% endblock %}

