<template v-slot:top>

      <v-toolbar flat>

        {% include "public/extends/customers/addCustomer.vue" %}

        <!--            <v-btn-->
        <!--                style="margin-left: 10px"-->
        <!--                color="pink lighten-2"-->
        <!--                dark-->
        <!--                :hidden="!btnAPI"-->
        <!--                @click="ImportRE(selected)"-->
        <!--            >-->
        <!--              <v-icon left>mdi-api</v-icon>-->
        <!--              [[ formBtnAPI ]]-->
        <!--            </v-btn>-->

        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">คุณแน่ใจว่าจะลบข้อมูล ?</v-card-title>
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