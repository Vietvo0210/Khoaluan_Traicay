<template>
  <v-navigation-drawer v-model="drawer" app>
    <v-img
      height="140"
      class="pa-4"
      src="https://preview.pixlr.com/images/800wm/1439/2/1439104804.jpg"
    >
      <div class="text-center">
        <v-avatar class="mb-4" color="grey darken-1" size="64">
          <v-img
            aspect-ratio="30"
            src=""
          />
        </v-avatar>
        <h2 class="white--text">Admin</h2>
      </div>
    </v-img>
    <v-divider></v-divider>
    <v-list>
      <v-list-item v-for="[icon, text,link] in links" :key="icon" :to="link" link>
        <v-list-item-icon>
          <v-icon>{{ icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ text }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "Sidebar",
  props: ["drawer"],
  data() {
    return {
      links: [
        ["mdi-microsoft-windows", "Dashboard","/"],
        ["mdi-account", "Profile","/Profile"],
        ["mdi-clipboard-list-outline", "Products","/Product"],
        ["mdi-card-account-details-outline", "Orders","/Order"],
        ["mdi-account-details-outline", "Customer","/Customer"],
      ],
    };
  },
};
</script>

<style scoped></style>