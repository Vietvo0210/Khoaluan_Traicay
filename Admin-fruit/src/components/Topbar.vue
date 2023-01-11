<template>
  <v-app-bar app elevate-on-scroll elevation="3" color="white">
    <v-app-bar-nav-icon @click="$emit('drawerEvent')"></v-app-bar-nav-icon>
    <v-spacer />
    <v-col lg="6" cols="12">
      <v-form>
        <v-text-field
          class="p-0 m-0 mt-6"
          full-width
          dense
          append-icon="mdi-magnify"
          outlined
          rounded
          placeholder="Search"
        />
      </v-form>
    </v-col>
    <v-spacer />
    <v-menu offset-y>
      <template v-slot:activator="{ attrs, on }">
        <span
          class="mx-5 mr-10"
          style="cursor: pointer"
          v-bind="attrs"
          v-on="on"
        >
          <v-badge content="3" color="red" offset-y="10" offset-x="10">
            <v-icon>mdi-bell</v-icon>
          </v-badge>
        </span>
      </template>
      <v-list three-line width="250">
        <template v-for="(item, index) in items">
          <v-subheader
            v-if="item.header"
            :key="item.header"
            v-text="item.header"
          ></v-subheader>

          <v-divider
            v-else-if="item.divider"
            :key="index"
            :inset="item.inset"
          ></v-divider>

          <v-list-item v-else :key="item.title">
            <v-list-item-avatar>
              <v-img :src="item.avatar"></v-img>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title v-html="item.title"></v-list-item-title>
              <v-list-item-subtitle
                v-html="item.subtitle"
              ></v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-menu>
    <v-menu offset-y>
      <template v-slot:activator="{ attrs, on }">
        <span style="cursor: pointer" v-bind="attrs" v-on="on">
          <v-chip link>
            <v-badge dot bottom color="green" offset-y="10" offset-x="10">
              <v-avatar size="40">
                <v-img src="" />
              </v-avatar>
            </v-badge>
            <span class="ml-3">HUY-VIET-DOAN</span>
          </v-chip>
        </span>
      </template>
      <v-list width="250" class="py-0">
        <v-list-item two-line>
          <v-list-item-avatar>
            <img src="" />
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>HUYTV</v-list-item-title>
            <v-list-item-subtitle>Logged In</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-divider />
        <v-list-item link v-for="(menu, i) in menus" :key="i">
          <v-list-item-icon>
            <v-icon>{{ menu.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>
            {{ menu.title }}
          </v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>
</template>

<script>
export default {
  name: "Topbar",
  data() {
    return {
      menus: [
        { title: "Profile", icon: "mdi-account" },
        { title: "Change Password", icon: "mdi-key" },
        { title: "Setting", icon: "mdi-cog" },
        { title: "Logout", icon: "mdi-logout" },
      ],
      items: [
        {
          avatar: "https://scontent.fhan3-4.fna.fbcdn.net/v/t1.6435-9/129722272_1204180786643993_7106996165974283206_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=174925&_nc_ohc=_CDUwD-pYksAX9HjsUL&_nc_ht=scontent.fhan3-4.fna&oh=00_AfCyDwhgcN3jMVtamZKrjqNOGowuRcw_u68ZR87_CBkfbQ&oe=63C10AB1",
          title: "Quốc việt vừa mua hàng",
          subtitle: '',
        },
        { divider: true, inset: true },
        {
          avatar:"https://scontent.fhan4-1.fna.fbcdn.net/v/t39.30808-6/244349341_1404050403323696_3025368870314890430_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=174925&_nc_ohc=O8vzY-kGl2YAX-BCChz&_nc_ht=scontent.fhan4-1.fna&oh=00_AfBUfVpuPFDmik8V0H5HFCkkigvhY-aKK4N0YQxJntDiBQ&oe=639DED6A",
          title: "Quốc việt vừa mua hàng",
          subtitle: '',
        },
       
      ],
    };
  },
};
</script>

<style scoped></style>
