<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-white w-100 navigation" id="navbar">
    <div class="container">

      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#main-navbar"
              aria-controls="main-navbar" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse " id="main-navbar">
        <ul class="navbar-nav mx-auto">

          <li class="nav-item">
            <router-link to="/product">
              <a class="nav-link" >Trang chủ</a>
            </router-link>
          </li>
          <li class="nav-item dropdown dropdown-slide">
            <router-link to="/product">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown3" role="button" data-delay="350"
               data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Sản phẩm
            </a>
            </router-link>
          </li>


          <li class="nav-item">
            <router-link to="/news">
              <a class="nav-link" >Tin tức</a>
            </router-link>
          </li>

          <li class="nav-item">
            <router-link to="/contact">
              <a class="nav-link" >Liên hệ</a>
            </router-link>
          </li>

          <li class="nav-item">
            <router-link to="/login">
              <a class="nav-link" >Đăng nhập</a>
            </router-link>
          </li>
        </ul>

      <!-- Navbar-collapse -->
      <ul class="navbar-nav mx-auto" >
        <li class="nav-item">
          <i
            class="tf-ion-android-search"
            @click="() => showModal('buttonTrigger')"
          >
          </i>

          <ModalSearch
            v-if="visible.buttonTrigger"
            :showModal="() => showModal('buttonTrigger') "
            @hiddenModel="catchHidden"
          >
            <h3>SEARCH</h3>
          </ModalSearch>
        </li>

        <li class="dropdown cart-nav dropdown-slide list-inline-item">
          <a href="#" class="dropdown-toggle cart-icon" data-toggle="dropdown" data-hover="dropdown">
            <i class="tf-ion-android-cart" @click="getProducts"></i>
          </a>
          <div class="dropdown-menu cart-dropdown" >
            <template v-if="cart.length !== 0" >
            <!-- Cart Item -->
            <div class="media" v-for="(item, index) in cart">
              <a href="#">
                <img class="media-object img-fluid mr-3" :src="item?.thumbnail" alt="image" />
              </a>
              <div class="media-body" >
                <h6>{{ item?.title }}</h6>
                <div class="cart-price">
                  <span>{{ item.price }} {{'VNĐ'}}</span>
                </div>
              </div>
              <a href="#" class="remove"><i class="tf-ion-close" @click="deleteProductInCart(index)"></i></a>
            </div><!-- / Cart Item -->
            </template>

            <div class="cart-summary">

              <div class="text-center cart-buttons mt-3">
                <a href="#" class="btn btn-small btn-main btn-block">Thanh Toán</a>
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
import { ref } from 'vue';
export default {
  components: { ModalSearch },

  setup() {
    const cart = ref([])
    const visible = ref({
      buttonTrigger: false,
      timeTrigger: false
    });
    const showModal = (trigger) => {
      visible.value[trigger] = !visible.value[trigger]
    };

    const catchHidden = () => {
      console.log('23131321321')
      console.log('23131321321')
    };

    const getProducts = () => {
      let products = localStorage.getItem('products')
      const jsonProducts = JSON.parse(products)
      cart.value = jsonProducts
      console.log(jsonProducts)
      // jsonProducts.forEach(p => {
      //   console.log(cart.value)
      //   // cart.value.some((c) => c.id !== p.id ? cart.value.push(p) : console.log('item exist'))
      // })
      // cart.value.push(jsonProducts)
      // console.log(cart.value)
    }
    const deleteProductInCart = (index) => {
      cart.value =  cart.value.filter((c, i) => i !== index)
    }

    return {
      visible,
      cart,
      deleteProductInCart,
      showModal,
      getProducts,
      catchHidden,
    }
  }
}
</script>

<style scoped>

</style>
