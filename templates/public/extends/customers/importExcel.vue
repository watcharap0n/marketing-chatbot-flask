<v-dialog v-model="dialogImportExcel" max-width="500px" persistent>
  <template v-slot:activator="{ on, attrs }">
    <v-btn
        style="margin-left: 8px;"
        color="pink lighten-2"
        dark
        v-bind="attrs"
        v-on="on"
        :hidden="!btnHiddenAPI"
    >
      <v-icon>
        mdi-microsoft-excel
      </v-icon>
    </v-btn>
  </template>

  <v-card>
    <v-card-title class="text-h5">กรุณาเลือกไฟล์ excel ที่ท่านต้องการเพื่อนำเข้ารายการ</v-card-title>
    <v-card-text>
      <v-row>
        <v-col cols="12">
          <v-file-input v-model="fileImportExcel" :rules="rulesImport"
                        required
                        color="pink lighten-2"
                        accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"
                        prepend-icon="mdi-paperclip"
                        :show-size="2000"
                        label="อัพโหลดไฟล์ excel"
                        counter
          >
            <template v-slot:selection="{ index, text }">
              <v-chip color="pink lighten-2"
                      dark
                      label
                      small
              >
                [[text]]
              </v-chip>
            </template>
            <v-chip
          </v-file-input>
        </v-col>
      </v-row>
      <v-btn color="pink lighten-2" text @click="excelPreview" :loading="!spinPreview"
      >
        <v-icon left>
          mdi-microsoft-excel
        </v-icon>
        ดาวน์โหลดไฟล์ตัวอย่าง
      </v-btn>

    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="error" text @click="closeImportExcel">ยกเลิก</v-btn>
      <v-btn color="success" text @click="importExcel"
             :loading="!spinButton">ตกลง
      </v-btn>
      <v-spacer></v-spacer>
    </v-card-actions>
  </v-card>
  <v-overlay :value="!spinButton">
    <v-progress-circular
        color="pink lighten-2"
        indeterminate
        size="64"
    ></v-progress-circular>
  </v-overlay>
</v-dialog>