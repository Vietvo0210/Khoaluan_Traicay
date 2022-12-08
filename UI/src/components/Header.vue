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
            <router-link to="/homepredict">
              <a class="nav-link" >Dự đoán trái cây</a>
            </router-link>
          </li>

          <li class="nav-item">
            <router-link to="/aboutUs">
            <a class="nav-link" >Về chúng tôi</a>
            </router-link>
          </li>
          <!-- Pages -->

          <!-- / Blog -->

          <li class="nav-item dropdown dropdown-slide">
            <router-link to="/product">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown3" role="button" data-delay="350"
               data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Sản phẩm
            </a>
            </router-link>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown3">
              <li><a href="#">Trái cây đặc sản </a></li>
              <li><a href="#">Giỏ hàng của bạn</a></li>
              <li><a href="#">Thanh toán</a></li>
            </ul>
          </li><!-- / Blog -->

          <li class="nav-item">
            <router-link to="/login">
              <a class="nav-link" >Đăng nhập</a>
            </router-link>
          </li>
        </ul>

      <!-- Navbar-collapse -->

      <ul class="navbar-nav mx-auto" >
        <li class="nav-item">
          <i class="tf-ion-android-search"/>
          <a href="http://localhost:5003/" class="search_toggle" id="search-icon">Tìm kiếm</a>
        </li>

        <li class="dropdown cart-nav dropdown-slide list-inline-item">
          <a href="#" class="dropdown-toggle cart-icon" data-toggle="dropdown" data-hover="dropdown">
            <i class="tf-ion-android-cart"></i>
          </a>
          <div class="dropdown-menu cart-dropdown">
            <!-- Cart Item -->
            <div class="media">
              <a href="#">
                <img class="media-object img- mr-3" src="assets/images/1.jpg" alt="image" />
              </a>
              <div class="media-body">
                <h6>

                Buoi  Tay</h6>
                <div class="cart-price">
                  <span>1 x</span>
                  <span>1250.00</span>
                </div>
              </div>
              <a href="#" class="remove"><i class="tf-ion-close"></i></a>
            </div><!-- / Cart Item -->

            <!-- Cart Item -->
            <div class="media">
              <a href="#">
                <img class="media-object img-fluid mr-3" src="assets/images/cart-2.jpg" alt="image" />
              </a>
              <div class="media-body">
                <h6>Chuoi Tay</h6>
                <div class="cart-price">
                  <span>1 x</span>
                  <span>1250.00</span>
                </div>
              </div>
              <a href="#" class="remove"><i class="tf-ion-close"></i></a>
            </div><!-- / Cart Item -->

            <div class="cart-summary">
              <span class="h6">Total</span>
              <span class="total-price h6">$1799.00</span>

              <div class="text-center cart-buttons mt-3">
                <a href="#" class="btn btn-small btn-transparent btn-block">View Cart</a>
                <a href="#" class="btn btn-small btn-main btn-block">Checkout</a>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </div>
    </div>
  </nav>
</template>
