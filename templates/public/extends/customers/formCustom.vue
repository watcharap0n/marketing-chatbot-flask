<v-btn
    style="margin-left: 8px;"
    color="pink lighten-2"
    color="primary"
    dark
    @click="openForm"
    :hidden="!btnHiddenAPI"
>
  <v-icon left>
    mdi-form-select
  </v-icon>
  สร้างฟอร์ม
</v-btn>

<v-dialog
    v-model="dialogForm"
    transition="dialog-top-transition"
    max-width="600"
>
  <v-card>
    <v-toolbar
        color="pink lighten-2"
        dark
    >สร้างฟอร์มแก้ไขฟอร์ม
    </v-toolbar>
    <v-card-text>
      <div
          v-if="!spinForm"
          class="text-h4 pa-12 text-center">
        <v-progress-circular
            indeterminate
            color="red"
            :size="50"
        ></v-progress-circular>
      </div>
      <div
          style="margin-top: 10px;"
          v-else
      >
        <v-btn
            style=" margin-bottom: 10px"
            fab
            dark
            small
            color="success"
            @click="openInForm"
        >
          <v-icon dark>
            mdi-plus
          </v-icon>
        </v-btn>


        <v-simple-table
            fixed-header
            height="300px"
        >
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-left">
                Page Name
              </th>
              <th class="text-left">
                URL
              </th>
              <th class="text-left">
                Delete
              </th>
            </tr>
            </thead>
            <tbody>
            <tr
                v-for="item in formCustom"
                :key="item.name"
            >
              <td>[[ item.page_name ]]</td>
              <td>
                <v-btn
                    :href="'/custom/form/'+ item.id"
                    target="_blank"
                    x-small
                    color="info">
                  [[item.id]]
                </v-btn>
              </td>
              <td>
                <v-btn
                    x-small
                    @click="deleteObjectForm(item)"
                    color="red">
                  ลบแบบฟอร์ม
                </v-btn>
              </td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>

      </div>

      <v-dialog
          v-model="dialogInForm"
          transition="dialog-top-transition"
          max-width="400"
      >
        <v-card>
          <v-card-text>
            <v-text-field label="ตั้งชื่อ" v-model="formElementCustom.page_name">
            </v-text-field>
          </v-card-text>
          <v-spacer></v-spacer>
          <v-card-actions>
            <v-btn
                small
                :loading="!spinForm"
                @click="addForm"
                color="success">
              ตกลง
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card-text>
    <v-card-actions class="justify-end">
      <v-btn
          text
          @click="dialogForm = false"
      >Close
      </v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>