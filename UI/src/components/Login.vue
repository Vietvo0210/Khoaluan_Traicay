<template>
  <div id="app">

    <div class="login-page">
      <transition name="fade">
        <div v-if="!registerActive" class="wallpaper-login"></div>
      </transition>
      <div class="wallpaper-register"></div>

      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
            <div v-if="!registerActive" class="card login" v-bind:class="{ error: emptyFields }">
              <h1>Login</h1>
              <form class="form-group">
                <input id="email" v-model="email" type="email" class="form-control" placeholder="Email" required>
                <input id="password" v-model="password" type="password" class="form-control" placeholder="Password" required>
                <input type="button" value="Login" class="btn btn-primary" @click="checkData">
                <p>Do you already have an account?<a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign up here</a>
                </p>
                <p><a href="#">Forgot password?</a></p>
              </form>
            </div>

            <div v-else class="card register" v-bind:class="{ error: emptyFields }">
              <h1>Register</h1>
              <form class="form-group">
                <input v-model="Item.fullname" type="fullname" class="form-control" placeholder="Full name" required>
                <input v-model="Item.email" type="email" class="form-control" placeholder="Email" required>
                <input v-model="Item.password" type="password" class="form-control" placeholder="Password" required>
                <input type="submit" class="btn btn-primary" @click="postData">
                <p>Do you already have an account?<a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign in here</a>
                </p>
              </form>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios";
    export default {
      name:"login",
      data: () => {
        return{
        Item: {
        id: '',
        fullname: '',
        email: '',
        password: '',
      },
        }     
      },
    
      methods: {
       async checkData(){
          let resutl=await axios.get(
            'http://192.168.1.26:8089/api/login/'+this.email+'/'+this.password
            ) 
            if(resutl.status=200)
            {
              window.open('http://localhost:8080')
            } 
            else
             this.errors.push("That bai.");
    },
    postData(){
      axios.post("http://192.168.1.26:8089/api/admin-create/", this.Item)
        .then(function (response) {
        console.log(response)
      })
    },
    created()
    {
      this.checkData()
    } 
  },
    }
</script>
<style>
p {
  line-height: 1rem;
}

.card {
  padding: 20px;
}

.form-group
input {
  margin-bottom: 20px;
}

.login-page {
  align-items: center;
  display: flex;
  height: 80vh;
}

.wallpaper-login {
  height: 50%;
  position: absolute;
  width: 100%;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity .5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.wallpaper-register {
  height: 50%;
  position: absolute;
  width: 100%;
  z-index: -1;
}

h1 {
  margin-bottom: 1.5rem;
}

.error {
  animation-name: errorShake;
  animation-duration: 0.3s;
}

@keyframes errorShake {
  0% {
    transform: translateX(-25px);
  }
  25% {
    transform: translateX(25px);
  }
  50% {
    transform: translateX(-25px);
  }
  75% {
    transform: translateX(25px);
  }
  100% {
    transform: translateX(0);
  }
}
</style>
