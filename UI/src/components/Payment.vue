<template>
  <div class="row">
    <div class="col-50">
      <div class="container">
        <form>
          <div class="row">
            <div class="col-50">
              <h3>Billing Address</h3>
              <label for="fname"><i class="fa fa-user"></i> Full Name</label>
              <input type="text" id="fname" name="fullname" placeholder="Viet, Huy, Doan">
              <label for="email"><i class="fa fa-envelope"></i> Email</label>
              <input type="text" id="email" name="email" placeholder="2001190936@hufi.edu.vn">
              <label for="number"><i class="fa fa-envelope"></i>Phone Number</label>
              <input id="number" @keypress="onlyNumber" type="text" placeholder="+84**********">
              <label for="adr"><i class="fa fa-address-card-o"></i> Address</label>
              <input type="text" id="adr" name="address" placeholder="140 LE TRONG TAN">
              <label for="city"><i class="fa fa-institution"></i> City</label>
              <input type="text" id="city" name="city" placeholder="Q. Tan Phu, TP.HCM">
              <label for="note"><i class="fa fa-user"></i> Full Name</label>
              <input type="text" id="note" name="note" placeholder="Note">
              <label for="otp" id="otp" v-if="checkOTP === true"> OTP </label>
              <input v-if="checkOTP === true" type="text" id="inputOtp">
            </div>
          </div>
          <label>
            <input type="checkbox" checked="checked" name="sameadr"> Shipping address same as billing
          </label>
          <div class="row">
            <div class="col-6">
          <input value="Continue to checkout" class="btn" @click="checkOut">
            </div>
            <div class="col-6">
              <input value="VerifyOTP" class="btn" @click="OTPVERIFY" v-if="checkOTP === true">
            </div>
            <div class="col-12">
              <label for="otp" id="otp">PLEASE VERIFY YOUR OTP BEFORE CHECKOUT</label>
              <input value="Checkout" class="btn" @click="Payment">
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="col-25">
      <div class="cart-container">
        <h4>Cart
          <span class="price" style="color:black">
          <i class="fa fa-shopping-cart"></i>
        </span>
        </h4>
        <div class="cart-media"
             v-for="(item, index) in cart"
             :key="item.id">

          <a href="#">
            <img class="media-object mr-3 img-pay" :src="item?.thumbnail" alt="image" />
            <a class="price">{{ item.price }}  {{'VNĐ'}}{{'/KG'}}</a>
          </a>

          &nbsp
          <p>Count
          <span class="price">
                {{ item.soluong }}
          </span>
          </p>
        <p>Total <span class="price" style="color:black"><b>{{ item.price * item.soluong}}</b></span></p>
          </div>
        <br/>
        <p>Summary<span class="price" style="color:black"><b>{{ summaryPara }}</b></span></p>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue'
import axios from 'axios'

export default {
  name: 'Payment',

  setup() {

    const checkOTP = ref(false)
    const visibleContinue = ref(true)
    const cart = ref([])
    const date = Date()
    const summaryPara = ref(0)

    const OTPVERIFY = () => {
      axios.post('http://192.168.1.26:8089/api/verify-otp', { "otp": document.getElementById("inputOtp").value }, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })
        .then((response) => {
        console.log(response)
      })
      visibleContinue.value = false
    }
    const checkOut = () => {
      checkOTP.value = true
      console.log(checkOTP.value)
      console.log(document.getElementById("number").value)
      axios.post('http://192.168.1.26:8089/api/otp')
    }

    const Payment = () => {
      let OrderForm = {
        "fullname": document.getElementById("fname").value,
        "email": document.getElementById("email").value,
        "phone_number": document.getElementById("number").value,
        "address": document.getElementById("adr").value,
        "note": document.getElementById("note").value,
        "order_date": Date(),
        "total_money": summaryPara.value,
      }
      console.log(OrderForm)
      if(visibleContinue.value === false){
      axios.post("http://192.168.1.26:8089/api/orders-create/", OrderForm)
        .then(function (response) {
          //close form
          console.log(response)
          if(response.status === 200){
            alert('Payment Success!')
          }
        })
      }
    }

    const onlyNumber = ($event) => {
      //console.log($event.keyCode); //keyCodes value
      let keyCode = ($event.keyCode ? $event.keyCode : $event.which);
      if ((keyCode < 48 || keyCode > 57) && keyCode !== 46) { // 46 is dot
        console.log($event.value)
        $event.preventDefault();
      }
    }

    const summary = () => {
      cart.value.forEach((value, index) => {
        console.log(value)
        console.log('index')
        console.log(index)

        summaryPara.value += value.price * value.soluong
      })
      console.log(summaryPara.value)
    }

    const getProducts = () => {
      localStorage.removeItem('products')
      let products = localStorage.getItem('cartPay')
      const jsonProducts = JSON.parse(products)
      cart.value = jsonProducts
    }

    onMounted(() => {
      getProducts()
      summary()
    })
    return {
      cart,
      visibleContinue,
      summaryPara,
      checkOTP,
      date,
      OTPVERIFY,
      onlyNumber,
      checkOut,
      summary,
      getProducts,
      Payment,
    }
  }
}
</script>

<style scoped>

.row {
  display: -ms-flexbox; /* IE10 */
  display: flex;
  -ms-flex-wrap: wrap; /* IE10 */
  flex-wrap: wrap;
  margin: 0 -16px;
}

.col-25 { /* IE10 */
  flex: 25%;
}

.col-50 {
  -ms-flex: 50%; /* IE10 */
  flex: 50%;
}

.col-75 {
  -ms-flex: 75%; /* IE10 */
  flex: 75%;
}

.col-25,
.col-50,
.col-75 {
  padding: 0 16px;
}

.container {
  background-color: #f2f2f2;
  padding: 5px 20px 15px 20px;
  border: 1px solid lightgrey;
  border-radius: 3px;
  width: 1000px;
}

.cart-container  {
  background-color: #f2f2f2;
  padding: 5px 20px 15px 20px;
  border: 1px solid lightgrey;
  border-radius: 3px;
  width: 500px;
}

input[type=text] {
  width: 100%;
  margin-bottom: 20px;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

label {
  margin-bottom: 10px;
  display: block;
}

.icon-container {
  margin-bottom: 20px;
  padding: 7px 0;
  font-size: 24px;
}

.btn {
  background-color: #04AA6D;
  color: white;
  padding: 12px;
  margin: 10px 0;
  border: none;
  width: 100%;
  border-radius: 3px;
  cursor: pointer;
  font-size: 17px;
}

.btn:hover {
  background-color: #45a049;
}

span.price {
  padding: 10px 10px;
  float: right;
  color: grey;
}

.img-pay{
  max-width:25%;
  height:auto;
  float:left;
}

.cart-media{
  display: flex;
  align-items: flex-start;
  padding: 10px 10px;
}

/* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other (and change the direction - make the "cart" column go on top) */
@media (max-width: 800px) {
  .row {
    flex-direction: column-reverse;
  }
  .col-25 {
    margin-bottom: 20px;
  }
}
</style>
