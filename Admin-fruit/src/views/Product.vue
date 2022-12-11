<template>
  <v-data-table
    :headers="headers"
    :items="data"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Product</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">

          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
              Add New
            </v-btn>
          </template>

          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              {{ data[0].id }}
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.title" label="Title"></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.price" label="price"></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.discount" label="Discount"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.thumbnail" label="Thumbnail"></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.description" label="Description"></v-text-field>
                  </v-col>

                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>

              <v-btn color="blue darken-1" text @click="postData">SAVE</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">Are you sure you want to delete this product?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>

    <template v-slot:item.actions="{ item }">
      {{ item.id }}
      <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
      <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize">Reset</v-btn>
    </template>
  </v-data-table>
</template>
<script>
import axios from "axios";
import { ref } from 'vue'
export default {
  props: {
    item: {
      type: Object,
      default: () => {
      }
    }
  },
  id_item_temp:Number,
  name: "Products",
  data: () => ({
    selected: "",
    headers: [
      { text: "Id", align: "center", sortable: false, value: "id" },
      { text: "Title", value: "title" },
      { text: "Price", value: "price" },
      { text: "Discount", value: "discount" },
      { text: "Thumbnail", value: "thumbnail" },
      { text: "Description", value: "" },
      { text: "Actions", value: 'actions', sortable: false },
    ],
    editedIndex: ref(-1),
    data: [],
    editedItem: {
      id: '',
      title: '',
      price: '',
      discount: '',
      thumbnail: '',
      description: '',
    },
    defaultItem: {
      id: '',
      title: '',
      price: '',
      discount: '',
      thumbnail: '',
      description: '',
    },
    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Product' : 'Edit Product'
      },
    },
  }),
  watch: {
    dialog (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    },
  },
  methods: {
    getData() {
      console.log(this.item)
      axios
        .get("http://192.168.1.10:8085/api/product-list/" )
        .then((response) => {
          this.data = response.data;
        })
        .catch((err) => alert(err));
    },
    postData(){
      console.log('INSERT DATA')
      axios.post("http://192.168.1.10:8085/api/product-create/", this.editedItem)
        .then(function (response) {
          //close form
          this.dialog(false)
        console.log(response)
        console.log("POST SUCCESS!")

        
      })
    },
   editItem (item) {
     this.editedIndex = this.data.indexOf(item.id)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.id_item_temp=item.id;
      this.editedItem = Object.assign({}, item)
      console.log(this.data.row)
      this.dialogDelete = true
    },
    deleteItemConfirm () {
      axios.get("http://192.168.1.10:8085/api/product-delete/"+this.id_item_temp+"/")
      this.getData()
      this.closeDelete()
    },
    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    save (item) {
      console.log(item)
      this.editItem()
      this.close()
    },
  },

  mounted() {
    this.getData();
  },
};
</script>