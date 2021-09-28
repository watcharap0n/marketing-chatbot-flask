<template v-slot:top>

  <v-toolbar flat>

    {% include "public/extends/customers/addCustomer.vue" %}


    <v-btn
        color="teal darken-1"
        dark
        :hidden="!btnRE"
        @click="createRE"
    >
      <v-icon left> mdi-wrench</v-icon>
      สร้างที่ RE
    </v-btn>

    <v-btn
        style="margin-left: 10px"
        color="primary"
        dark
        @click="editRE"
        :hidden="!btnRE"
    >
      <v-icon left>fas fa-edit</v-icon>
      อัพเดทที่ RE
    </v-btn>

    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title><h5>คุณแน่ใจว่าจะลบข้อมูล ?</h5></v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="success" text @click="closeDelete">ยกเลิก</v-btn>
          <v-btn color="error" text @click="deleteItemConfirm"
                 :loading="!spinButton">ตกลง
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogDuplicateRE" max-width="500px">
      <v-card>
        <v-card-title>
          <v-icon left> mdi-wrench</v-icon>
          <h5>มีข้อมูลที่เคยนำเข้าโปรแกรม RE แล้ว !</h5></v-card-title>
        <v-divider></v-divider>
        <v-card-text v-for="(k, v) in itemsDuplicateRE" :key="k">
          <v-responsive
              class="overflow-y-auto"
              max-height="400"
          >
            <b>ลำดับ [[v + 1]]: Customer code: [[k.customer_code]] ชื่อ: [[k.name]]</b>
          </v-responsive>
        </v-card-text>
        <v-divider></v-divider>
        <small
            style="color: red; margin-left: 20px">*รายการที่ท่านต้องการบันทึก
          มีข้อมูลแล้วในระบบท่านต้องการดำเนินต่อหรือไม่?</small>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" text @click="closeDuplicateRE">ยกเลิก</v-btn>
          <v-btn color="success" text @click="finallyCreate"
                 :loading="!spinButton">
            ตกลง
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogConfirmRE" max-width="500px">
      <v-card>
        <v-card-title>
          <v-icon left> mdi-wrench</v-icon>
          <h5>ยืนยันเพื่อนำเข้าโปรแกรม RE ?</h5></v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-responsive
              class="overflow-y-auto"
              max-height="400"
          >
            <div class="mb-4" v-for="(k, v) in usersRE" :key="k">
              <b>ลำดับ [[v + 1]]: ชื่อ: [[k.company]] บริษัท: [[k.first_name]]</b>
            </div>
          </v-responsive>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" text @click="closeConfirmRE">ยกเลิก</v-btn>
          <v-btn color="success" text @click="finallyCreate" :loading="!spinButton">
            ตกลง
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogUpdateRE" max-width="500px">
      <v-card>
        <v-card-title>
          <v-icon left>fas fa-edit</v-icon>
          <h5>ยืนยันเพื่อแก้ไขรายชื่อต่อไปนี้ในโปรแกรม RE ?</h5></v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-responsive
              class="overflow-y-auto"
              max-height="400"
          >
            <div class="mb-4" v-for="(k, v) in usersRE" :key="k">
              <b>ลำดับ [[v + 1]]: Customer code: [[k.customer_code]] ชื่อ: [[k.company]]</b>
            </div>
          </v-responsive>
        </v-card-text>
        <v-divider></v-divider>
        <small style="color: red; margin-left: 20px">*ข้อมูลที่จะทำการอัพเดทได้จะต้องเคยเพิ่มเข้าโปรแกรม RE
          แล้ว!</small>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" text @click="closeUpdateRE">ยกเลิก</v-btn>
          <v-btn color="success" text @click="finallyEditRE" :loading="!spinButton">
            ตกลง
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    &nbsp;
    <v-btn
        dark
        color="pink lighten-2"
        :hidden="!btnImport"
        @click="moveImport"
        :loading="spinImport"
    >
      <v-icon left>mdi-application-import</v-icon>
      นำเข้า
    </v-btn>


    {% include "public/extends/customers/importExcel.vue" %}


    {% include "public/extends/customers/formCustom.vue" %}


    <v-btn
        style="margin-left: 10px"
        color="teal darken-1"
        dark
        :hidden="!btnAPI"
        :loading="!spinRE"
        @click="validCheckRE(selected)">

      <v-icon left>mdi-api</v-icon>
      ตรวจสอบเข้า RE
    </v-btn>
    <v-spacer></v-spacer>

    <div class="small" style="margin-right: 20px">
      <v-text-field
          color="pink lighten-2"
          :loading="!spinTable"
          v-model="search"
          append-icon="mdi-magnify"
          label="ค้นหา"
          single-line
          hide-details
      >
      </v-text-field>
    </div>

  </v-toolbar>


  <v-toolbar flat>

    {% include "public/extends/customers/sorting.vue" %}


    {% include "public/extends/customers/excel.vue" %}

    &nbsp;
    <v-btn
        style="margin-bottom: 10px"
        elevation="3"
        :disabled="!btnDelete"
        :loading="!spinDelete"
        small
        color="#FF648D"
        dark
        @click="sendDeleteMultiple"
    ><i class="fas fa-trash-alt"></i>
      ลบข้อมูล
    </v-btn>


    <v-spacer></v-spacer>

    <!-- tag start -->

    <v-btn
        style="margin-bottom: 20px"
        elevation="3"
        :loading="!spinTag"
        :disabled="!btnTag"
        small
        color="#FF648D"
        dark
        @click="tagTransaction(selected)"
    ><i class="fas fa-user-tag"></i>
      ติดแท็ก
    </v-btn>

    <div class="small" style="margin-left: 10px; margin-right: 20px" :hidden="!btnHiddenAPI">
      <v-combobox
          :loading="!spinTable"
          v-model="model"
          :filter="filter"
          :hide-no-data="!searchTag"
          :items="itemsTag"
          :search-input.sync="searchTag"
          hide-selected
          label="แท็ก"
          color="pink lighten-2"
          multiple
          dense
          small-chips

      >
        <template v-slot:no-data>
          <v-list-item>
            <v-icon color="green">mdi-arrow-right-thick</v-icon>
            <span class="subheading">สร้าง</span>&nbsp;&nbsp;
            <v-chip
                style="color: white"
                color="pink lighten-2"
                label
                small
            >
              [[ searchTag ]]
            </v-chip>
          </v-list-item>
        </template>
        <template v-slot:selection="{ attrs, item, parent, selected, index}">
          <v-chip
              v-if="index < 2"
              v-if="item === Object(item)"
              v-bind="attrs"
              color="pink lighten-2"
              :input-value="selected"
              label
              small
              close
              close-icon="mdi-delete"
              @click:close="parent.selectItem(item)"
          >
                      <span class="pr-2" style="color: white">
                        [[ item.text ]]
                      </span>
          </v-chip>
          <span v-if="index === 1"
                class="grey--text caption">(+[[ model.length - 1 ]] แท็กอื่นๆ)
                    </span>
        </template>

        <template v-slot:item="{ index, item }">
          <v-text-field
              v-if="editingTag === item"
              v-model="editingTag.text"
              autofocus
              flat
              background-color="transparent"
              hide-details
              solo
              @keyup.enter="edit(index, item)"
          ></v-text-field>
          <v-chip
              v-else
              color="pink lighten-2"
              dark
              label
              small
          >
            [[ item.text ]]
          </v-chip>
          <v-spacer></v-spacer>
          <v-list-item-action @click.stop>
            <v-row>
              <v-col>
                <v-btn
                    icon
                    @click.stop.prevent="edit(index, item)"
                >
                  <v-icon color="teal">[[ editingTag !== item ? 'mdi-pencil' : 'mdi-check' ]]</v-icon>
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                    icon
                    @click.stop.prevent="toRemove(index, item)"
                >
                  <v-icon color="red">mdi-delete</v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-list-item-action>
        </template>
      </v-combobox>

    </div>

  </v-toolbar>
</template>