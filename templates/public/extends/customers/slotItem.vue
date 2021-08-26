<template v-slot:item.tag="{item}">
  <v-chip
      dark
      color="red"
      class="ma-2"
      v-for="i in item.tag" :key="i.length"
      @click="sortingOnclick({'tag': i})"
  >

    [[ i ]]
    <v-icon
        ref="copyTag"
        right
        v-clipboard:copy.prevent="i"
        @click.stop.prevent="copyTag(i)"
    >
      mdi-content-copy
    </v-icon>
  </v-chip>
</template>

<template v-slot:item.name="{item}">
  <div style="margin-top: 15px; margin-bottom: 15px">
    <v-row>
      <v-col>
        <strong>[[item.name ]]</strong>
        <span>[[item.email ]]</span>
        <span>[[item.tel ]]</span>

        <v-list-group
            dense
            color="red lighten-2"
            v-if="item.person_id || item.tax_id"
            :value="false"
            prepend-icon="mdi-card-account-details-outline"
        >
          <v-list-item-content>
            <span v-if="item.person_id"> <strong>เลขที่บัตรประชาชน</strong> [[item.person_id]]</span>
            <span v-if="item.tax_id"> <strong>เลขที่เสียภาษี</strong> [[item.tax_id]]</span>

          </v-list-item-content>
        </v-list-group>
        <div v-else></div>

      </v-col>
    </v-row>
  </div>
</template>

<template v-slot:item.product="{item}">
  <v-chip class="ma-2" :color="colorProduct(item.product)" label
          @click="sortingOnclick({'product': item.product})">
    <div v-if="item.product === 'Construction'">
      <strong style="color: green">[[item.product]]</strong>
    </div>

    <div v-else-if="item.product === 'RealEstate'">
      <strong style="color: blue">[[item.product]]</strong>
    </div>

    <div v-else-if="item.product === 'Project Planning'">
      <strong style="color: deeppink">[[item.product]]</strong>
    </div>

    <div v-else-if="item.product === 'Consulting'">
      <strong style="color: black">[[item.product]]</strong>
    </div>

    <div v-else>
      <strong>[[item.product]]</strong>
    </div>
  </v-chip>
</template>

<template v-slot:item.message="{item}">
  <v-list-group
      color="#7A8FC0"
      v-if="item.message"
      :value="false"
      prepend-icon="mdi-message"
  >
    <v-list-item-content>
      [[item.message]]
    </v-list-item-content>
  </v-list-group>
  <div v-else></div>
</template>

<template v-slot:item.channel="{item}">
  <div v-if="item.channel === 'Contact'" @click="sortingOnclick({'channel': item.channel})">
    <v-chip outlined color="blue darken-2">
      [[item.channel ]]
    </v-chip>
  </div>

  <div v-else-if="item.channel === 'GetDemo'" @click="sortingOnclick({'channel': item.channel})">
    <v-chip outlined color="pink lighten-2">
      [[item.channel ]]
    </v-chip>
  </div>

  <div v-else-if="item.channel === 'LINE'" @click="sortingOnclick({'channel': item.channel})">
    <v-chip outlined color="green accent-4">
      [[item.channel ]]
    </v-chip>
  </div>

  <div v-else @click="sortingOnclick({'channel': item.channel})">
    <v-chip outlined>
      [[item.channel ]]
    </v-chip>
  </div>
</template>

<template v-slot:item.date="{item}">
  [[ item.date ]]
  <v-divider></v-divider>
  [[ item.time ]]
</template>

<template v-slot:item.actions="{item}">
  <v-icon small class="mr-2" color="green lighten-2" @click="editItem(item)">
    mdi-pencil
  </v-icon>
  <v-icon small color="red" @click="deleteItem(item)">
    mdi-delete
  </v-icon>
</template>