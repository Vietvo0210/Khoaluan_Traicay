<template>
  <div class="container">
    <h1
    >DỰ ĐOÁN TRÁI CÂY ĐẶC SẢN VIỆT NAM</h1>
    <button @click="fetchData" >TEST FETCHDATA</button>

    <br><br>
    <form class="form-horizontal" action="/submit" method="post" enctype="multipart/form-data">
        <div
            style="align-items: center">
          <img
              src="http://cdn.tgdd.vn/Files/2017/05/23/985304/nhung-cong-dung-tuyet-voi-cua-thanh-long-ban-nen-biet-202109171144120943.jpg"
              alt="pred-img" />
          <h3>Lựa chọn hình ảnh: </h3>

          <h4
              style="width:300px"
              class="mb-5"
          >
            (Upload Your Image)
          </h4>
          <input type="file"
                 style="width: 390px"
                 class="mb-4"
                 name="my_image">
          <br/>
            <div>
              <button
                  type="submit"
                  class="btn btn-success mb-5"
              >Submit</button>
            </div>
          <br/>
          <div>
            <p></p>
            <h4>{{ tasks }}</h4>
            <h4 > Dự đoán : <i> {{'PRED_VIETNAMESE'}} </i> </h4>
          </div>
        </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import { onMounted, ref } from 'vue';

export default {
  name: 'HomePredict',
  data() {
    return {
      // tasks
      tasks: {}
    }
  },
  methods: {
    fetchData(){
      axios.get('http://127.0.0.1:8000/api/predict/')
      .then((response) => {
        console.log(response.data)
        this.tasks = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
    data() {
      return {
        predict: axios.get('http://127.0.0.1:8000/api/predict/'),
      }
    },
  },
  created() {
    // Fetch tasks on page load
    this.fetchData();
    Promise.all([
        this.data(),
    ])
  }
}

</script>

<script setup>

import { onMounted, ref } from 'vue';
const props = defineProps({
  item: {
    type: Object,
    default: () => {},
  },
})
onMounted(() => {
  result()
  axios.get('http://192.168.1.26:8085/api/predict/')
})

let rs1 = null
const result = () => {
}
</script>

<style scoped>
.container{
  display: inline-block;
  vertical-align: center;
}
.form-horizontal{
  width: 1100px;
  align-items: center;
}
img{
  width: 700px;
  float: right;
}
button{
  float: left;
}
h1{
  padding: 40px;
  background-color:powderblue;
  color: #1b1e21;
}
h3{
  width:300px;
  float: left;
}
h4{
  width:300px;
  float:left;
}
</style>
