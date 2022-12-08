<template>
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-12">
          <div class="title text-center">
            <h2 >CỬA HÀNG TRÁI CÂY TƯƠI HUFI</h2>
          </div>
        </div>
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
                {{post.price}}x
                    </span>
            </div>
          </div>
        </div>
        <!-- <div class="col-lg-3 col-12 col-md-6 col-sm-6 mb-5" >
          <div class="product">
            <div class="product-wrap">
              <a href="#"><img class="img-fluid w-100 mb-3 img-first" src="https://2.bp.blogspot.com/-rm4WSmTHJsM/Unkgq-rt26I/AAAAAAAAFBg/Wbaj_1wuNxc/s1600/ip+006.JPG" alt="product-img" /></a>
              <a href="#"><img class="img-fluid w-100 mb-3 img-second" src="https://2.bp.blogspot.com/-rm4WSmTHJsM/Unkgq-rt26I/AAAAAAAAFBg/Wbaj_1wuNxc/s1600/ip+006.JPG" alt="product-img" /></a>
            </div>

            <span class="onsale">Sale</span>
            <div class="product-hover-overlay">
              <a href="#"><i class="tf-ion-android-cart"></i></a>
              <a href="#"><i class="tf-ion-ios-heart"></i></a>
            </div>

            <div class="product-info">
              <h2 class="product-title h5 mb-0"><a href="#">Xoài cát</a></h2>
              <span class="price">
                        50.000vnđ - 80.000vnđ/1kg
                    </span>
            </div>
          </div>
        </div>

        <div class="col-lg-3 col-12 col-md-6 col-sm-6 mb-5">
          <div class="product">
            <div class="product-wrap">
              <a href="#"><img class="img-fluid w-100 mb-3 img-first" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxO03C4uqg9L6t2sepaM97dS6sUG7qmA0EcH6xdK7r7E2hDATjP5KrHpFtKBFpLbCefzk&usqp=CAU" alt="product-img" /></a>
              <a href="#"><img class="img-fluid w-100 mb-3 img-second" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxO03C4uqg9L6t2sepaM97dS6sUG7qmA0EcH6xdK7r7E2hDATjP5KrHpFtKBFpLbCefzk&usqp=CAU" alt="product-img" /></a>
            </div>

            <div class="product-hover-overlay">
              <a href="#"><i class="tf-ion-android-cart"></i></a>
              <a href="#"><i class="tf-ion-ios-heart"></i></a>
            </div>

            <div class="product-info">
              <h2 class="product-title h5 mb-0"><a href="#">Táo đỏ mỹ</a></h2>
              <span class="price">
                        85.000vnđ/1kg
                    </span>
            </div>
          </div>
        </div>

        <div class="col-lg-3 col-12 col-md-6 col-sm-6 mb-5">
          <div class="product">
            <div class="product-wrap">
              <a href="#"><img class="img-fluid w-100 mb-3 img-first" src="https://biquyetkhoedep.net/wp-content/uploads/2021/07/an-man-ha-noi-co-nong-khong.png" alt="product-img" /></a>
              <a href="#"><img class="img-fluid w-100 mb-3 img-second" src="https://biquyetkhoedep.net/wp-content/uploads/2021/07/an-man-ha-noi-co-nong-khong.png" alt="product-img" /></a>
            </div>

            <div class="product-hover-overlay">
              <a href="#"><i class="tf-ion-android-cart"></i></a>
              <a href="#"><i class="tf-ion-ios-heart"></i></a>
            </div>

            <div class="product-info">
              <h2 class="product-title h5 mb-0"><a href="#">Mận Hà Nội</a></h2>
              <span class="price">
                        40.000vnđ/1kg
                    </span>
            </div>
          </div>
        </div>

        <div class="col-lg-3 col-12 col-md-6 col-sm-6 mb-5" >
          <div class="product">
            <div class="product-wrap">
              <a href="#"><img class="img-fluid w-100 mb-3 img-first" src="https://tieudung.kinhtedothi.vn/upload_images/images/2020/12/18/oi.jpg" alt="product-img" /></a>
              <a href="#"><img class="img-fluid w-100 mb-3 img-second" src="https://tieudung.kinhtedothi.vn/upload_images/images/2020/12/18/oi.jpg" alt="product-img" /></a>
            </div>

            <div class="product-hover-overlay">
              <a href="#"><i class="tf-ion-android-cart"></i></a>
              <a href="#"><i class="tf-ion-ios-heart"></i></a>
            </div>

            <div class="product-info" >
              <h2 class="product-title h5 mb-0"><a href="#">Ổi</a></h2>
              <span class="price">
                        30.000vnđ/1kg
                    </span>
            </div>
          </div>
        </div>

        <div class="col-lg-3 col-12 col-md-6 col-sm-6 mb-5 " >
          <div class="product">
            <div class="product-wrap">
              <a href="#"><img class="img-fluid w-100 mb-3 img-first" src="https://dacsandalat.com.vn/wp-content/uploads/2014/06/qua-hong.jpg" alt="product-img" /></a>
              <a href="#"><img class="img-fluid w-100 mb-3 img-second" src="https://dacsandalat.com.vn/wp-content/uploads/2014/06/qua-hong.jpg" alt="product-img" /></a>
            </div>

            <div class="product-hover-overlay">
              <a href="#"><i class="tf-ion-android-cart"></i></a>
              <a href="#"><i class="tf-ion-ios-heart"></i></a>
            </div>

            <div class="product-info">
              <h2 class="product-title h5 mb-0"><a href="#">Hồng Đà Lạt</a></h2>
              <span class="price">
                        90.000vnđ/1kg
                    </span>
            </div>
          </div>
        </div>

        <div class="col-lg-3 col-12 col-md-6 col-sm-6 mb-5 " >
          <div class="product">
            <div class="product-wrap">
              <a href="#"><img class="img-fluid w-100 mb-3 img-first"
                               src="https://media.cooky.vn/images/blog-2016/thu-gian-voi-hinh-anh-trai-cay-cuc-dang-yeu%207.jpg" />
              </a>
              <a href="#"><img
                class="img-fluid w-100 mb-3 img-second"
                src="https://media.cooky.vn/images/blog-2016/thu-gian-voi-hinh-anh-trai-cay-cuc-dang-yeu%207.jpg"
                alt="product-img" />
              </a>
            </div>

            <div class="product-hover-overlay">
              <a href="#"><i class="tf-ion-android-cart"></i></a>
              <a href="#"><i class="tf-ion-ios-heart"></i></a>
            </div>

            <div class="product-info">
              <h2 class="product-title h5 mb-0"><a href="#">Táo xanh cười</a></h2>
              <span class="price">
                        <del>300.000vnđ/1kg<pre wp-pre-tag-5=""></pre></del>
                        200.000vnđ/1kg
                    </span>
            </div>
          </div>
        </div>-->
      </div>
    </div>
  <!-- /portfolio -->

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
              <p>Hỗ trợ khách hàng mọi lúc</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  data() {
    return {
      posts: [],
    };
  },

  methods: {
    async getData() {
      try {
        let response = await fetch("http://192.168.1.26:8085/api/product-list/");
        this.posts = await response.json();;
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
