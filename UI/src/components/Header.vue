
<template>
  <div>
    <img style="width: 100%;" src="https://theme.hstatic.net/1000141988/1000913105/14/top_banner.jpg?v=617" alt="">
  </div>
  <nav class="navbar navbar-expand-lg navbar-light bg-white w-100 navigation menu-header" id="navbar" style="">
    <div class="container">

      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#main-navbar"
        aria-controls="main-navbar" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse " id="main-navbar">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item">
            <router-link to="/product">
              <a  @click="setfruits(1)" class="nav-link" >Home</a>
            </router-link>
          </li>
          <li class="nav-item dropdown dropdown-slide">
            <router-link to="/product">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown3" role="button" data-delay="350"
                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Product
              </a>
            </router-link>
            <ul class="dropdown-menu">
              <li>
                <router-link to="/product">
                  <a @click="setfruits(0)">Vietnamese special fruit</a>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <router-link to="/news">
              <a class="nav-link">News</a>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/contact">
              <a class="nav-link">Contact</a>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/login">
              <a class="nav-link">Login</a>
            </router-link>
          </li>
        </ul>
        <!-- Navbar-collapse -->
        <ul class="navbar-nav mx-auto">
          <li class="nav-item">
            <i class="tf-ion-android-search" @click="() => showModal('buttonTrigger')">
            </i>
            <ModalSearch v-if="visible.buttonTrigger" :showModal="() => showModal('buttonTrigger')"
              @hiddenModel="catchHidden">
              <h3>SEARCH</h3>
            </ModalSearch>
          </li>
          <li class="dropdown cart-nav dropdown-slide list-inline-item">
            <a href="#" class="dropdown-toggle cart-icon" data-toggle="dropdown" data-hover="dropdown">
              <i class="tf-ion-android-cart" @click="getProducts"></i>
            </a>
            <div class="dropdown-menu cart-dropdown" width="150px">
              <h4 v-if="cart.length === 0">No items chosen</h4>
              <template v-if="cart.length !== 0">
                <!-- Cart Item -->
                <div class="media" v-for="(item, index) in cart">
                  <a href="#">
                    <img class="media-object img-fluid mr-3" :src="item?.thumbnail" alt="image" />
                  </a>
                  <div class="media-body">
                    <h6>{{ item?.title }}</h6>
                    <div class="cart-price">
                      <span>{{ item.price }}{{'.000'}} {{ 'VNĐ'}}</span>
                      <div class="input-group">
                        <input type="button" value="-" class="button-minus" data-field="quantity"
                          @click="minusCountProduct(index)">
                        <input type="number" step="1" :value="item.soluong" name="quantity" class="quantity-field"
                          disabled>
                        <input type="button" value="+" class="button-plus" data-field="quantity"
                          @click="updateCountProduct(index)">
                      </div>
                    </div>
                  </div>
                  <div>
                  </div>
                  <a href="#" class="remove"><i class="tf-ion-close" @click="deleteProductInCart(index)"></i></a>
                </div><!-- / Cart Item -->
              </template>
              <div class="cart-summary" v-if="cart.length > 0">
                <div class="text-center cart-buttons mt-3">
                  <router-link to="/payment">
                    <a href="" class="btn btn-small btn-main btn-block">Payment</a>
                  </router-link>
                </div>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import ModalSearch from '@/components/ModalSearch';
import Home from '@/components/Home';
import { ref } from 'vue';
export default {
  components: { ModalSearch, Home },

  setup() {
    const cart = ref([])
    const visible = ref({
      buttonTrigger: false,
      timeTrigger: false,
    });
    const showModal = (trigger) => {
      visible.value[trigger] = !visible.value[trigger]
    };

    const catchHidden = () => {
    };

    const updateCountProduct = (index) => {
      if (cart.value[index].soluong < 5) {
        let updatedSoluong = cart.value[index].soluong += 1
        console.log(cart.value[index])
        cart.value[index] = Object.assign(cart.value[index], { 'soluong': updatedSoluong })
        localStorage.setItem('cartPay', JSON.stringify(cart.value))
      }
    }

    const minusCountProduct = (index) => {
      if (cart.value[index].soluong > 1) {
        cart.value[index].soluong -= 1
      }
    }

    const getProducts = () => {
      let products = localStorage.getItem('products')
      const jsonProducts = JSON.parse(products)
      cart.value = jsonProducts
    }
    const deleteProductInCart = (index) => {
      cart.value = cart.value.filter((c, i) => i !== index)
    }
    const setfruits=(val)=>{

      let vn=val;
      const vietnam = JSON.parse(vn);

      localStorage.setItem('vietname',vietnam);
      location.reload()

    }

    return {
      visible,
      cart,
      updateCountProduct,
      minusCountProduct,
      deleteProductInCart,
      showModal,
      getProducts,
      catchHidden,
      setfruits,
    }
  }
}

</script>

<style scoped>
input,
textarea {
  border: 1px solid #eeeeee;
  box-sizing: border-box;
  margin: 0;
  outline: none;
  padding: 10px;
}

input[type="button"] {
  -webkit-appearance: button;
  cursor: pointer;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.input-group {
  clear: both;
  margin: 15px 0;
  position: relative;
}

.input-group input[type='button'] {
  background-color: #eeeeee;
  min-width: 38px;
  width: auto;
  transition: all 300ms ease;
}

.input-group .button-minus,
.input-group .button-plus {
  font-weight: bold;
  height: 38px;
  padding: 0;
  width: 38px;
  position: relative;
}

.input-group .quantity-field {
  position: relative;
  height: 38px;
  left: -6px;
  text-align: center;
  width: 62px;
  display: inline-block;
  font-size: 13px;
  margin: 0 0 5px;
  resize: vertical;
}

.button-plus {
  left: -13px;
}

input[type="number"] {
  -moz-appearance: textfield;
  -webkit-appearance: none;
}

.menu-header{
  border: solid 1px #97c924;
  height: 85px !important;
  background-color: #F0FFF0 !important;

}
</style>
