<template>

<div class="Popup">
  <div class="popup-inner">
    <slot/>
    <div>
    <input class="searchInput" id="textField">
      &nbsp
      &nbsp
      <button class="searchButton" @click="SEARCH">Seach</button>
     <br/>
      <br/>
      <input type="file" id="img" name="img" accept="image/*" @change="previewImage"/>
      <img class="previewImg"  :src="preview" alt="your image" />
      <br/>
      <br/>
    </div>
    <br/>
    <button class="popup-close" @click="showModal()">
      Close
    </button>
  </div>
</div>
</template>

<script>

import axios from 'axios'
import { ref } from 'vue'
export default {
  name: 'ModalSearch',
  props: ['showModal'],
  data: function() {
    return {
      preview: null,
      image: null,
      predictedImg: '',
      list: [],
    };
  },
  methods: {
    previewImage: function (event){
      const input = event.target
      if (input.files) {
        const reader = new FileReader()
        reader.onload = (e) => {
          this.preview = e.target.result;
        }
        this.image=input.files[0];
        reader.readAsDataURL(input.files[0]);
        console.log(this.image)
        console.log(this.image.name)
        let img = new FormData();
        img.append('FILE', this.image)
        axios.post("http://192.168.1.26:8089/api/predict/", img, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }).then(function (response) {
          console.log(response.data[0])
          document.getElementById('textField').value = response.data[0].type
        })
      }
    },
    async SEARCH() {
        const name = document.getElementById('textField').value
        localStorage.setItem('nameSearch', name)
        await axios.get('http://192.168.1.26:8089/api/search/' + name)
          .then(function (response) {
            location.reload()
            console.log(this)
            console.log('2222222222222222')
            console.log(response)
          })
    },
  },
}
</script>

<style scoped>
.Popup {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 99;
  background-color: rgba(0, 0, 0, 0.2);

  display: flex;
  align-items: center;
  justify-content: center;
}
  .popup-inner {
    background: #EABE12;
    padding: 32px;
    width: 800px;
    border-radius: 15px;
  }
  .searchButton{
    padding: 15px 25px;
    box-shadow: 0 9px #999;
    border: none;
    border-radius: 15px;
  }
  .popup-close {
    padding: 15px 20px;
    box-shadow: 0 9px #999;
    border: none;
    border-radius: 15px;
  }
  .searchInput{
    width: 400px;
    height: 50px;
    border-radius: 15px;
  }
  .previewImg{
    height: 200px;
    width: 400px;
    border-radius: 15px;
  }
  .searchButton:hover {background-color: #3e8e41}
  .popup-close:hover {background-color: #dcbba8}
</style>
