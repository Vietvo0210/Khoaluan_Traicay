<template>
  <form class="contact-form" >
      <div class="form-group">
          <label for="msg-name">Firstname</label>
          <input type="text" id="msg-name" class="form-control" v-model="Item.firstname">
      </div>
      <div class="form-group">
          <label for="msg-name">Lastname</label>
          <input type="text" id="msg-name" class="form-control" v-model="Item.lastname">
      </div>
      <div class="form-group">
          <label for="msg-name">Email</label>
          <input type="text" id="msg-name" class="form-control" v-model="Item.email">
      </div>
      <div class="form-group">
          <label for="msg-email">Phone number</label>
          <input type="text" id="msg-email" class="form-control" v-model="Item.phone_number">
      </div>
      <div class="form-group">
          <label for="msg-message">Message</label>
          <textarea rows="10" id="msg-message" class="form-control" v-model="Item.note"></textarea>
      </div>
      <div class="form-result">
          <p class="alert alert-success" v-if="success && !error">Message sent successfully.</p>
          <p class="alert alert-error" v-if="!success && error">Message failed.</p>
      </div>
      <div class="form-group">
          <button class="btn" type="submit" @click="postData">Send</button>
      </div>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: 'ContactForm',
  data: function () {
      return {
          Item: {
            firstname: '',
            lastname: '',
            email:'',
            phone_number: '',
            note: '',
          },
          success: false,
          error: false,
      }
  },
  methods: {
    postData(){
      axios.post("http://127.0.0.1:8000/api/feedback-create/", this.Item)
        .then(function (response) {
        console.log(response)
        this.data.splice(this.editedIndex, 1)
      })
    },
    created()
    {
      this.postData()
    } ,
      resetForm: function () {
          this.contactFormData = {
            firstname: '',
            lastname: '',
            email:'',
            phone_number: '',
            note: '',
          };
      },
  },
}
</script>

<style scoped>
body { background: #52c1f7; }
* { box-sizing: border-box; }

.contact-form {
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
  padding: 1em;
}
.form-group {
  padding: 10px;
}
.form-control {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}
input[type=text].form-control {
  margin: 8px 0;
  display: inline-block;
}
textarea.form-control {
  resize: none;
}
.btn {
  cursor: pointer;
  padding: 8px 10px;
  outline: none;
  border: none;
  background: #3be249;
  font-size: 16px;
  width: 100%;
  border-radius: 4px;
  text-align: center;
}
.alert {
  padding:0 10px;
}
.alert-success {
  color:#3be249;
}
.alert-error {
  color: #ff2121;
}

</style>