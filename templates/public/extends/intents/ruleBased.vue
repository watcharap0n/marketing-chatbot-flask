<v-card>
  <v-card-title dark
                style="background: linear-gradient(to right, #7C4DFF, #304FFE, #448AFF);">
    <v-icon dark>
      mdi-robot
    </v-icon>
    &nbsp;
    ชุดข้อมูล Keywords

    <v-spacer></v-spacer>

    <v-dialog
        v-model="dialogRuleBased"
        persistent
        max-width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            :hidden="!hiddenRuleBased"
            color="green accent-1"
            v-bind="attrs"
            v-on="on"
        >
          <v-icon left>
            mdi-pencil
          </v-icon>
          สร้าง keyword
        </v-btn>
      </template>
      <v-card>

        <v-toolbar flat
                   color="success"
                   dark>
          ชื่อ Rule Based
        </v-toolbar>

        <v-card-text>
          <div class="mb-2">
            <v-text-field
                v-model="nameRuleBased"
                label="ชื่อ RuleBased"
                clearable
            ></v-text-field>
          </div>


        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="red darken-1"
              text
              @click="dialogRuleBased = false"
          >
            ยกเลิก
          </v-btn>
          <v-btn
              color="green darken-1"
              text
              :loading="!spinIntent"
              @click="createRuleBased"
          >
            ตกลง
          </v-btn>
        </v-card-actions>
      </v-card>

    </v-dialog>


  </v-card-title>


  <v-row
      class="pa-4"
      justify="space-between"
  >
    <v-col cols="5">
      <v-treeview
          :active.sync="active_r"
          :load-children="ruleBased"
          :items="itemRuleBased"
          :open.sync="open_r"
          activatable
          color="warning"
          open-on-click
          transition
      >
        <template v-slot:prepend="{ item }">
          <v-icon v-if="!item.children" color="warning">
            mdi-book
          </v-icon>
        </template>


      </v-treeview>
    </v-col>

    <v-divider vertical></v-divider>

    <v-col
        class="text-center"
    >
      <v-scroll-y-transition mode="out-in">
        <div
            v-if="!selectedRuleBased"
            class="text-h6 grey--text text--lighten-1 font-weight-light"
            style="align-self: center;"
        >
          เลือก Keywords
        </div>

        <v-card
            class="pt-6 mx-auto"
            flat
        >
          <v-card-text>
            <div class="mb-2">

              <h3 class="text-h6 ">
                Keyword
              </h3>

              <div v-if="!selectedRuleBased">
              </div>
              <div v-else>
                <v-text-field
                    v-model="selectedRuleBased.keyword"
                    filled
                    clear-icon="mdi-close-circle"
                    clearable
                    label="Keyword"
                    type="text"
                    :loading="!spinIntent"
                ></v-text-field>
              </div>


              <div v-if="!selectedRuleBased">
              </div>

            </div>

            <v-divider></v-divider>


            <h3 class="text-h6 ">
              Reply
            </h3>
            <v-row
                class="text-left"
                tag="v-card-text"
            >
              <div v-if="!selectedRuleBased">
              </div>
              <v-textarea
                  v-else
                  v-model="selectedRuleBased.contents"
                  clearable
                  clear-icon="mdi-close-circle"
                  label="Reply"
                  max-width="800"
              ></v-textarea>

              <div v-if="!selectedRuleBased">
              </div>
            </v-row>

            <div v-if="!selectedRuleBased">
            </div>
            <v-checkbox
                v-else
                color="red"
                v-model="selectedRuleBased.status"
                label="Flex Message"
            ></v-checkbox>
            <div>
              <strong>คุณสามารถไปออกแบบ Flex message ได้ที่ </strong> : <strong><a target="_blank"
                                                                                   href="https://developers.line.biz/flex-simulator">
              FlexMessage </a></strong>
            </div>

          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>


            <v-btn
                color="success darken-1"
                text
                @click="saveRuleBased"
            >
              บันทึกข้อมูล
            </v-btn>

            <v-dialog
                v-model="dialogDeleteRuleBased"
                persistent
                max-width="290"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                    class="mx-2"
                    fab
                    dark
                    x-small
                    color="red"
                    v-bind="attrs"
                    v-on="on"
                >
                  <v-icon dark>
                    mdi-delete
                  </v-icon>
                </v-btn>
              </template>
              <v-card>
                <div v-if="!selectedRuleBased"></div>
                <v-card-title v-else>
                  คุณแน่ใจที่จะลบ [[selectedRuleBased.name]]?
                </v-card-title>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                      color="green darken-1"
                      text
                      @click="dialogDeleteRuleBased = false"
                  >
                    ยกเลิก
                  </v-btn>
                  <v-btn
                      color="red darken-1"
                      text
                      :loading="!spinIntent"
                      @click="deleteRuleBased(selectedRuleBased)"
                  >
                    ตกลง
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-actions>

        </v-card>

      </v-scroll-y-transition>
    </v-col>
  </v-row>
</v-card>
