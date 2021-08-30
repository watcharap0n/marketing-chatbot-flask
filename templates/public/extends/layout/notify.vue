  <v-menu
      bottom
      left
      transition="slide-y-transition"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-badge
          color="pink lighten-2"
          :content="notify_today.length"
      >
        <v-icon
            v-bind="attrs"
            v-on="on"
        >
          mdi-bell-ring-outline
        </v-icon>
      </v-badge>
    </template>

    <v-list >
      <v-list-item @click="navigatorAppbar = true">
        <v-list shaped>
          <v-subheader>แจ้งเตือนข้อมูลใหม่: [[datetimeNow]]</v-subheader>
          <v-list-item-group
              v-model="selectedNotify"
              color="pink lighten-2"
          >
            <v-list-item
                v-for="(item, i) in notify_today"
                :key="i"
            >
              <v-list-item-content>
                <v-list-item-title>คนที่ [[i + 1]]: [[item.name]]</v-list-item-title>
                <v-list-item-subtitle>บริษัท [[item.company]]</v-list-item-subtitle>
                <v-list-item-subtitle>ผลิตภัณฑ์: [[item.product]]</v-list-item-subtitle>
                <v-list-item-subtitle>ช่องทาง: [[item.channel]]</v-list-item-subtitle>
                <v-list-item-subtitle>ช่วงเวลา: [[item.time]]</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-list-item>
    </v-list>
  </v-menu>
  &nbsp; &nbsp;