<template>
    <v-data-table
      :headers="headers"
      :items="desserts"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar
          flat
        >
          <v-toolbar-title>Orders</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
            v-model="dialog"
            max-width="500px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
              >
                Add New
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>
  
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.id"
                        label="ID"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.customer_id"
                        label="Customer_id"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.fullname"
                        label="Fullname"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.email"
                        label="Email"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.phone_number"
                        label="Phone_number"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.address"
                        label="Address"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.note"
                        label="Note"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.order_date"
                        label="Order_date"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.status"
                        label="Status"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="editedItem.total_money"
                        label="Total_money"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
  
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="save"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5">Are you sure you want to delete this order?</v-card-title>
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
        <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          small
          @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn
          color="primary"
          @click="initialize"
        >
          Reset
        </v-btn>
      </template>
    </v-data-table>
  </template>
  
  <script>
    export default {
      name:"Order",
      data: () => ({
        dialog: false,
        dialogDelete: false,
        headers: [
        {
            text: 'ID',
            align: 'start',
            sortable: false,
            value: 'id',
          },
          
          { text: 'Customer_id', value: 'customer_id' },
          { text: 'Fullname', value: 'fullname' },
          { text: 'Email', value: 'email' },
          { text: 'Phone_number', value: 'phone_number' },
          { text: 'Address', value: 'address' },
          { text: 'Note', value: 'note' },
          { text: 'Order_date', value: 'order_date' },
          { text: 'Status', value: 'status' },
          { text: 'Total_money', value: 'total_money' },
          { text: 'Actions', value: 'actions', sortable: false },
        ],
        desserts: [],
        editedIndex: -1,
        editedItem: {
          id: '',
          customer_id: 0,
          fullname: 0,
          email: 0,
          phone_number: 0,
          address: 0,
          note: 0,
          order_date: 0,
          status: 0,
          total_money: 0,
          actions: 0,
        },
        defaultItem: {
          id: '',
          customer_id: 0,
          fullname: 0,
          email: 0,
          phone_number: 0,
          address: 0,
          note: 0,
          order_date: 0,
          status: 0,
          total_money: 0,
          actions: 0,
        },
      }),
      computed: {
        formTitle () {
          return this.editedIndex === -1 ? 'New Order' : 'Edit Order'
        },
      },
      watch: {
        dialog (val) {
          val || this.close()
        },
        dialogDelete (val) {
          val || this.closeDelete()
        },
      },
      created () {
        this.initialize()
      },
      methods: {
        initialize () {
          this.desserts = [
            {
              id: '',
              customer_id: 0,
              fullname: 0,
              email: 0,
              phone_number: 0,
              address: 0,
              note: 0,
              order_date: 0,
              status: 0,
              total_money: 0,
              actions: 0,
            },
            {
              id: '',
              customer_id: 0,
              fullname: 0,
              email: 0,
              phone_number: 0,
              address: 0,
              note: 0,
              order_date: 0,
              status: 0,
              total_money: 0,
              actions: 0,
            },
            {
              id: '',
              customer_id: 0,
              fullname: 0,
              email: 0,
              phone_number: 0,
              address: 0,
              note: 0,
              order_date: 0,
              status: 0,
              total_money: 0,
              actions: 0,
            },
            {
              id: '',
              customer_id: 0,
              fullname: 0,
              email: 0,
              phone_number: 0,
              address: 0,
              note: 0,
              order_date: 0,
              status: 0,
              total_money: 0,
              actions: 0,
            },
            {
              id: '',
              customer_id: 0,
              fullname: 0,
              email: 0,
              phone_number: 0,
              address: 0,
              note: 0,
              order_date: 0,
              status: 0,
              total_money: 0,
              actions: 0,
            },
            {
              id: '',
              customer_id: 0,
              fullname: 0,
              email: 0,
              phone_number: 0,
              address: 0,
              note: 0,
              order_date: 0,
              status: 0,
              total_money: 0,
              actions: 0,
            },
          ]
        },
        editItem (item) {
          this.editedIndex = this.desserts.indexOf(item)
          this.editedItem = Object.assign({}, item)
          this.dialog = true
        },
        deleteItem (item) {
          this.editedIndex = this.desserts.indexOf(item)
          this.editedItem = Object.assign({}, item)
          this.dialogDelete = true
        },
        deleteItemConfirm () {
          this.desserts.splice(this.editedIndex, 1)
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
        save () {
          if (this.editedIndex > -1) {
            Object.assign(this.desserts[this.editedIndex], this.editedItem)
          } else {
            this.desserts.push(this.editedItem)
          }
          this.close()
        },
      },
    }
  </script>
  
  