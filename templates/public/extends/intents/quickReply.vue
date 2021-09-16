<v-card>
  <v-card-title dark
                style="background: linear-gradient(to right, #7C4DFF, #304FFE, #448AFF);">
    <v-icon dark>
      mdi-robot
    </v-icon>
    &nbsp;
    ชุดข้อมูล QuickReply

    <v-spacer></v-spacer>

    <v-dialog
        v-model="dialogQuickReply"
        persistent
        max-width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            :hidden="!hiddenQuickReply"
            color="green accent-1"
            v-bind="attrs"
            v-on="on"
        >
          <v-icon left>
            mdi-pencil
          </v-icon>
          สร้าง QuickReply
        </v-btn>
      </template>
      <v-card>

        <v-toolbar flat
                   color="success"
                   dark>
          ชื่อ QuickReply
        </v-toolbar>

        <v-card-text>
          <div class="mb-2">
            <v-text-field
                v-model="quickData.name"
                label="ชื่อ QuickReply"
                clearable
            ></v-text-field>
          </div>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="red darken-1"
              text
              @click="dialogQuickReply = false"
          >
            ยกเลิก
          </v-btn>
          <v-btn
              color="green darken-1"
              text
              :loading="!spinIntent"
              @click="createQuickReply"
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
          :active.sync="active_quick"
          :load-children="quickReply"
          :items="itemQuickReply"
          :open.sync="open_quick"
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
            v-if="!selectedQuickReply"
            class=" grey--text text--lighten-1 font-weight-light"
            style="align-self: center;"
        >
          เลือก QuickReply
        </div>

        <v-card
            class="mx-auto overflow-y-auto"
            flat
        >
          <v-card-text>
            <div class="mb-2">
              <h3 class="text-h6 ">
                Reply
              </h3>
              <div v-if="!selectedQuickReply">
              </div>
              <v-select
                  v-else
                  :items="choice_intents"
                  label="เลือก intent ที่ต้องการสร้าง quick reply"
                  v-model="selectedQuickReply.quick_name"
              ></v-select>
              <v-row
                  class="text-left"
                  tag="v-card-text"
              >
                <div v-if="!selectedQuickReply">
                </div>
                <v-text-field
                    v-else
                    v-model="selectedQuickReply.reply"
                    clear-icon="mdi-close-circle"
                    clearable
                    label="ให้บอทตอบ"
                    type="text"
                    :loading="!spinIntent"
                    @keyup.enter="sendQuickReply"
                    @click:append-outer="sendQuickReply"
                ></v-text-field>
              </v-row>
            </div>


            <v-divider></v-divider>
            <div class="mb-2">
              <h3 class="text-h6 ">
                Text
              </h3>
              <v-text-field
                  v-model="textQuick"
                  :append-outer-icon="textQuick ? 'mdi-send' : ''"
                  filled
                  clear-icon="mdi-close-circle"
                  clearable
                  label="แสดงข้อความ"
                  type="text"
                  :loading="!spinIntent"
                  @keyup.enter="sendQuickReply"
                  @click:append-outer="sendQuickReply"
              ></v-text-field>

              <div v-if="!selectedQuickReply">
              </div>
              <v-combobox
                  v-else
                  v-model="selectedQuickReply.texts"
                  :item="selectedQuickReply.texts"
                  label="แสดงข้อความ"
                  chips
                  multiple
                  readonly
              >
                <template v-slot:selection="{ item }">
                  <v-chip
                      class="ma-2"
                      close
                      @click:close="removeQuickReply(item)"
                  >
                    [[item]]
                  </v-chip>
                </template>
              </v-combobox>
            </div>

            <v-divider></v-divider>
            <h3 class="text-h6 ">
              Label
            </h3>
            <v-text-field
                v-model="labelQuick"
                :append-outer-icon="labelQuick ? 'mdi-send' : ''"
                filled
                clear-icon="mdi-close-circle"
                clearable
                label="ข้อความที่ส่งไป"
                type="text"
                :loading="!spinIntent"
                @keyup.enter="sendLabelQuick"
                @click:append-outer="sendLabelQuick"
            ></v-text-field>
            <div v-if="!selectedQuickReply">
            </div>
            <v-combobox
                v-else
                v-model="selectedQuickReply.labels"
                :item="selectedQuickReply.labels"
                label="แสดงข้อความที่ส่งไป"
                chips
                multiple
                readonly
            >
              <template v-slot:selection="{ item }">
                <v-chip
                    class="ma-2"
                    close
                    @click:close="removeLabelQuick(item)"
                >
                  [[item]]
                </v-chip>
              </template>
            </v-combobox>


          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn
                color="success darken-1"
                text
                @click="putQuickReply"
            >
              บันทึกข้อมูล
            </v-btn>
            <div v-if="!selectedQuickReply"></div>
            <v-dialog
                v-else
                v-model="dialogDeleteQuick"
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
                <v-card-title>
                  คุณแน่ใจที่จะลบ [[selectedQuickReply.name]] ?
                </v-card-title>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                      color="green darken-1"
                      text
                      @click="selectedQuickReply = false"
                  >
                    Disagree
                  </v-btn>
                  <v-btn
                      color="red darken-1"
                      text
                      :loading="!spinIntent"
                      @click="deleteQuickReply(selectedQuickReply)"
                  >
                    Agree
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