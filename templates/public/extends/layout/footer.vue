<v-footer
    class="elevation-5"
    absolute
>
  <small>
    <v-app-bar
        class="elevation-5"
        absolute
        dense
    >
      Copyright &copy; 2021 Mango Consultant Built @watcharapon. All Rights Reserved
      <v-spacer></v-spacer>
      <small>
        <v-btn
            v-for="icon in icons"
            :key="icon"
            class="mx-4 "
            icon
            :href="icon.href"
            target="_blank"
        >
          <v-icon size="24px">
            [[ icon.icon ]]
          </v-icon>
        </v-btn>
      </small>
    </v-app-bar>
  </small>
</v-footer>