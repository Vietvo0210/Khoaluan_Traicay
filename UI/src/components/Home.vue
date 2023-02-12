<template>
  <div class="container">
    <div class="row justify-content-center">
    </div>
    <br />
    <br />

    <div class="row">
      <div class="col-lg-3" v-for="post in posts" :key="post.id">
        <div class="product">
          <div class="product-wrap">
            <a href="#"><img class="media-object w-100 mb-3 img-first img-sp" :src="post.thumbnail" alt="okke" />
            </a>
          </div>
          <div class="product-hover-overlay">
            <a href="#" @click=onClick(post)><i class="tf-ion-ios-heart"></i></a>
          </div>

          <div class="product-info">
            <router-link :to="{ name: 'viewdetail', params: { id: post.id } }">{{ post.title }}</router-link>
            <br />
            <span class="price">
              {{ post.price }} {{ 'VNĐ' }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="qc">
        <div class="container">
          <div class="row">
            <div class="col-lg-8">
              <img class="img-bottom" src="https://img.meta.com.vn/Data/image/2020/09/03/trai-cay-tot-cho-sinh-ly-nam-al.jpg" />
            </div>
            <div class="col-lg-4">
              <span class="h5 deal">Up to 50% off </span>
              <h3 class="mt-3 text-black">Vietnamese fruits</h3>
              <p class="text-md mt-3 text-white">Quickly order now!</p>
              <a href="#" class="btn btn-main"><i class="ti-bag mr-2"></i>Shop Now </a>
            </div>
          </div>
        </div>
    </div>

  <section class="features border-top">
    <div class="container">
      <div class="row">
        <div class="col-lg-3 col-sm-6 col-md-6">
          <div class="feature-block">
            <i class="tf-ion-android-bicycle"></i>
            <div class="content">
              <h5>Free ship</h5>
              <p>When the total bill is over 300,000 VND</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-sm-6 col-md-6">
          <div class="feature-block">
            <i class="tf-wallet"></i>
            <div class="content">
              <h5>Refund within 3 hours</h5>
              <p>Money back guarantee</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-sm-6 col-md-6">
          <div class="feature-block">
            <i class="tf-key"></i>
            <div class="content">
              <h5>Secure payment</h5>
              <p>100% guaranteed by the Momo app</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-sm-6 col-md-6">
          <div class="feature-block">
            <i class="tf-clock"></i>
            <div class="content">
              <h5>24/7 support</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import ViewDetail from '@/components/ViewDetail';
export default {
  // eslint-disable-next-line vue/no-unused-components
  components: { ViewDetail },

  data() {
    return {
      productsLiked: [],
      posts: [],
      id: null
    };
  },

  methods: {
    onClick(item) {
      if (!this.productsLiked.includes(item)) {
        this.productsLiked.push(item)
        item = Object.assign(item, { 'soluong': 1 })
      }
      localStorage.setItem('products', JSON.stringify(this.productsLiked))
    },
    async getData() {
      try {
        let response = {};
        let check = localStorage.getItem('vietname');

        let title = localStorage.getItem('nameSearch')

        if (check == 1) {
          response = await fetch("http://192.168.1.26:8089/api/product-list/");
        }
        else {
          response = await fetch('http://192.168.1.26:8089/api/vietnam-fruits/')
        }
        this.posts = await response.json();
        if (title) {
          let response = await fetch('http://127.0.0.1:8000/api/search/' + title)
          this.posts = await response.json();
        }

      }
      catch (error) {
        console.log(error);
      }
    },
    mounted() {
      this.id = this.$route.params.id;
      this.post = this.post.find(post => post.id == this.id)
    }
  },
  created() {
    this.getData();
  },
  watch() {
    this.getData();
  }
};
</script>
<style>
h2 {
  padding: 40px;
  background-color: powderblue;
  color: #1b1e21;
}

.product {
  height: 250px;
  width: 200px;
}

.qc{
  margin-bottom: 50px;
}

.img-bottom{
      width:800px ;height: 300px;
}

.img-sp{
  height: 150px;
}
</style>
