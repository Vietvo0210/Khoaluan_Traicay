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
              <h1>Đăng nhập</h1>
              <form class="form-group">
                <input id="email" v-model="email" type="email" class="form-control" placeholder="Email" required>
                <input id="password" v-model="password" type="password" class="form-control" placeholder="Mật khẩu" required>
                <input type="button" value="Login" class="btn btn-primary" @click="checkData">
                <!-- <button  type="submit" @click="checkData">Login</button> -->
                <p>Bạn chưa có tài khoản? <a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign up here</a>
                </p>
                <p><a href="#">Quên mật khẩu?</a></p>
              </form>
            </div>

            <div v-else class="card register" v-bind:class="{ error: emptyFields }">
              <h1>Đăng ký</h1>
              <form class="form-group">
                <input v-model="emailReg" type="email" class="form-control" placeholder="Email" required>
                <input v-model="passwordReg" type="password" class="form-control" placeholder="Mật khẩu" required>
                <input v-model="confirmReg" type="password" class="form-control" placeholder="Nhập lại mật khẩu" required>
                <input type="submit" class="btn btn-primary" @click="doRegister">
                <p>Bạn đã có tài khoản? <a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign in here</a>
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
          email:'',
          password:''
        }     
      },
    
      methods: {
       async checkData(){
<<<<<<< Updated upstream
          let resutl=await axios.post(
=======
          let resutl=await axios.get(
>>>>>>> Stashed changes
            'http://127.0.0.1:8000/api/login/'+this.email+'/'+this.password
            ) 
            if(resutl.status=200)
            {
              this.$router.push({name:'product'})
            }
            else
            // this.$router.push({name:'product'})
             this.errors.push("Something went wrong, please refresh and try again.");
             this.$router.push({name:'Login'})
    },
    created() {
  this.checkData();
},
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
  height: 50vh;
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
