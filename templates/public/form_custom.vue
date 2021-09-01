{% extends "admin/main_layout.html" %}
{% block content %}

  {% include 'public/extends/layout/navigationTop.vue' %}

  <br><br><br>
  <div class="container-fluid">
    <input type="hidden" value="{{ id }}" ref="formId"/>
    <v-row justify="center">
      <v-col
          cols="6"
          sm="6"
          md="6"
          lg="6"
      >
        <v-card
            class="mx-auto my-6"
            max-width="500"
            :loading="!spinData"
        >
          <v-list-item>
            <v-list-item-content>
              <div class="text-overline">
                ฟอร์มปรับแต่ง
              </div>
              <div class="text-overline">
                <small>id form: [[ form.id ]]</small>
              </div>
            </v-list-item-content>
          </v-list-item>
          <v-form
              ref="form"
              v-model="valid"
              lazy-validation
          >
            <v-card-text>
              <v-text-field
                  :rules="validOther"
                  v-model="form.name"
                  dense
                  outlined
                  clearable
                  prepend-inner-icon="mdi-account"
                  label="ชื่อผู้ติดต่อ"
                  required
              >
              </v-text-field>
              <v-text-field
                  :rules="validOther"
                  v-model="form.company"
                  dense
                  outlined
                  clearable
                  prepend-inner-icon="mdi-office-building"
                  label="บริษัท"
                  required
              >
              </v-text-field>

              <v-text-field
                  :rules="validOther"
                  v-model="form.email"
                  dense
                  outlined
                  clearable
                  prepend-inner-icon="mdi-email"
                  label="อีเมล"
                  required
              >
              </v-text-field>

              <v-text-field
                  :rules="validOther"
                  v-model="form.product"
                  dense
                  outlined
                  clearable
                  prepend-inner-icon="mdi-post-outline"
                  label="ผลิตภัณฑ์"
                  required
              >
              </v-text-field>

              <v-text-field
                  :rules="validOther"
                  v-model="form.other"
                  dense
                  outlined
                  clearable
                  prepend-inner-icon="mdi-post-outline"
                  label="อื่นๆ"
                  required
              >
              </v-text-field>

              <v-text-field
                  :rules="validOther"
                  v-model="form.tel"
                  dense
                  outlined
                  clearable
                  prepend-inner-icon="mdi-card-account-phone"
                  label="เบอร์ติดต่อ"
                  required
              >
              </v-text-field>

              <v-text-field
                  :rules="validOther"
                  v-model="form.message"
                  dense
                  outlined
                  clearable
                  prepend-inner-icon="mdi-message"
                  label="ข้อความ"
                  required
              >
              </v-text-field>

              <v-text-field
                  :rules="validOther"
                  v-model="form.channel"
                  dense
                  outlined
                  clearable
                  prepend-inner-icon="mdi-access-point-check"
                  label="ช่องทาง"
                  required
              >
              </v-text-field>


              <v-text-field
                  v-model="selectedProduct"
                  dense
                  clearable
                  label="กำหนดผลิตภัณฑ์ เมื่อพร้อมให้ ENTER"
                  @keyup.enter="addProduct({key: 'product'})"
                  required
              >
              </v-text-field>

              <v-combobox
                  v-model="form.itemProducts"
                  :items="form.itemProducts"
                  label="เลือกผลิตภัณฑ์เพื่อนำเข้าฟอร์ม"
                  multiple
                  chips
                  hide-selected
                  color="pink lighten-2"
              >
                <template v-slot:selection="{ item }">
                  <v-chip
                      :key="JSON.stringify(item)"
                      close
                      close-icon="mdi-delete"
                      @click:close="deleteProduct({key: 'product', item: item})"
                  >
                    <v-avatar
                        class="accent white--text"
                        left
                        v-text="item.slice(0, 1).toUpperCase()"
                    ></v-avatar>
                    [[ item ]]
                  </v-chip>
                </template>
              </v-combobox>
              <v-text-field
                  v-model="selectedOther"
                  dense
                  clearable
                  label="กำหนดอื่นๆ เมื่อพร้อมให้ ENTER"
                  @keyup.enter="addProduct({key: 'other'})"
                  required
              >
              </v-text-field>

              <v-combobox
                  v-model="form.itemOthers"
                  :items="form.itemOthers"
                  label="เลือกผลิตภัณฑ์เพื่อนำเข้าฟอร์ม"
                  multiple
                  chips
                  hide-selected
                  color="pink lighten-2"
              >
                <template v-slot:selection="{ item }">
                  <v-chip
                      :key="JSON.stringify(item)"
                      close
                      close-icon="mdi-delete"
                      @click:close="deleteProduct({key: 'other', item: item})"
                  >
                    <v-avatar
                        class="accent white--text"
                        left
                        v-text="item.slice(0, 1).toUpperCase()"
                    ></v-avatar>
                    [[ item ]]
                  </v-chip>
                </template>
              </v-combobox>
              <v-text-field
                  :rules="validOther"
                  disabled
                  v-if="form.type === 'LINE'"
                  v-model="form.token_liff"
                  dense
                  clearable
                  label="app id liff"
                  required
              >
              </v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-btn
                  :disabled="!valid"
                  color="success"
                  block
                  @click="updateProduct"
                  :loading="!spinData"
              >
                บันทึก
              </v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-col>

      <v-col
          cols="6"
          sm="6"
          md="6"
          lg="6"
      >
        <v-card
            class="mx-auto my-6"
            max-width="500"
            :loading="!spinData"
        >
          <v-list-item>
            <v-list-item-content>
              <div>
                <div class="text-overline" v-if="!form.channel">
                  ช่องทาง: ไม่ได้กำหนด
                </div>
                <div class="text-overline" v-else>
                  ช่องทาง: [[form.channel]]
                </div>
              </div>
              <small>
                <strong>url:</strong>
                <a :href="form.href">
                  [[form.href]]
                </a>
              </small>
            </v-list-item-content>
          </v-list-item>
          <v-card-text>
            <v-text-field
                persistent-hint
                hint="*เปลี่ยนชื่อฟอร์ม -> ข้อมูลลูกค้า"
                dense
                outlined
                clearable
                :label="form.name"
            ></v-text-field>

            <v-text-field
                persistent-hint
                hint="*เปลี่ยนชื่อฟอร์ม -> บริษัท"
                dense
                outlined
                clearable
                :label="form.company"
            ></v-text-field>

            <v-text-field
                persistent-hint
                hint="*เปลี่ยนชื่อฟอร์ม -> ข้อมูลลูกค้า"
                dense
                outlined
                clearable
                :label="form.email"
            ></v-text-field>

            <v-select
                persistent-hint
                hint="*เปลี่ยนชื่อฟอร์ม และสร้างไอเท็ม -> ผลิตภัณฑ์"
                :label="form.product"
                dense
                outlined
                clearable
                :items="form.itemProducts"
            ></v-select>

            <v-select
                persistent-hint
                hint="*เปลี่ยนชื่อฟอร์ม และสร้างไอเท็ม -> อื่นๆ"
                :label="form.other"
                dense
                outlined
                clearable
                :items="form.itemOthers"
            ></v-select>

            <v-text-field
                persistent-hint
                hint="*เปลี่ยนชื่อฟอร์ม -> ข้อมูลลูกค้า"
                dense
                outlined
                clearable
                :label="form.tel"
                type="tel"
            ></v-text-field>


            <v-textarea
                persistent-hint
                hint="*เปลี่ยนชื่อฟอร์ม -> ข้อความ"
                dense
                outlined
                clearable
                autocomplete
                :label="form.message"
            ></v-textarea>

            <v-card-actions>
              <v-btn block
                     disabled
                     color="success"
                     class="mr-4"
              >
                ยืนยัน
              </v-btn>
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

  </div>

  {% block footer %}
    {% include 'public/extends/layout/footer.vue' %}
  {% endblock %}


  {% block script %}
    <script src="/static/js/form_custom.js"></script>
  {% endblock %}





{% endblock %}