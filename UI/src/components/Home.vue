<template>
    <div class="container">
      <div class="row justify-content-center">
      </div>
      <br/>
      <br/>
      <div class="row" >
        <div class="col-lg-3" v-for="post in posts" :key="post.id">
          <div class="product" >
            <div class="product-wrap">
              <a href="#"><img
                class="img-fluid w-100 mb-3 img-first"
                :src="post.thumbnail"
                alt="okke"/>
              </a>
            </div>
            <div class="product-hover-overlay">
              <a href="#"><i class="tf-ion-android-cart"></i></a>
              <a href="#"><i class="tf-ion-ios-heart"></i></a>
            </div>

            <div class="product-info">
              <h3 class="product-title h5 mb-0">{{post.title}}</h3>
              <span class="price">
                {{post.price}}
                    </span>
            </div>
          </div>
        </div>
      </div>
    </div>

  <view-detail>

  </view-detail>
  <section>
    <div class="container">
      <div class="row" >
        <div class="col-lg-6">
      <img
        src="https://img.meta.com.vn/Data/image/2020/09/03/trai-cay-tot-cho-sinh-ly-nam-al.jpg"/>\
        </div>
        <div class="col-lg-6">
            <span class="h5 deal">Giảm lên đến 50% </span>
            <h3 class="mt-3 text-black">Các loại trái cây Việt Nam</h3>
            <p class="text-md mt-3 text-white">Nhanh chóng đặt hàng ngay nào!</p>
            <a href="#" class="btn btn-main"><i class="ti-bag mr-2"></i>Shop Now </a>
          </div>
        </div>
      </div>
  </section>

  <section class="features border-top">
    <div class="container">
      <div class="row">
        <div class="col-lg-3 col-sm-6 col-md-6">
          <div class="feature-block">
            <i class="tf-ion-android-bicycle"></i>
            <div class="content">
              <h5>Miễn phí giao hàng</h5>
              <p>Khi tổng hoá đơn trên 300.000vnđ</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-sm-6 col-md-6">
          <div class="feature-block">
            <i class="tf-wallet"></i>
            <div class="content">
              <h5>Hoàn trả trong vòng 3h</h5>
              <p>Đảm bảo hoàn lại tiền</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-sm-6 col-md-6">
          <div class="feature-block">
            <i class="tf-key"></i>
            <div class="content">
              <h5>Thanh toán an toàn</h5>
              <p>100% được đảm bảo bởi ứng dụng Momo</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-sm-6 col-md-6">
          <div class="feature-block">
            <i class="tf-clock"></i>
            <div class="content">
              <h5>Hỗ trợ 24/7 </h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import ViewDetail from '@/components/ViewDetail'
export default {
  components: { ViewDetail },
  data() {
    return {
      posts: [],
    };
  },

  methods: {
    async getData() {
      try {
        let response = await fetch("http://192.168.1.26:8085/api/product-list/");
        this.posts = await response.json();
      } catch (error) {
        console.log(error);
      }
    },
  },

  created() {
    this.getData();
  },
};
</script>
<style>
h2{
  padding: 40px;
  background-color:powderblue;
  color: #1b1e21;
}
</style>
