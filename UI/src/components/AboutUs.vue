<template>
  <div class="about-section">
    <h1>Về chúng tôi</h1>
    <p>Some text about who we are and what we do.</p>
    <p>Resize the browser window to see that this page is responsive by the way.</p>
  </div>

  <h2 style="text-align:center">Our Team</h2>
  <div class="row">
    <div class="column">
      <div class="card">
        <img src="https://scontent.fsgn2-4.fna.fbcdn.net/v/t39.30808-6/316098583_1694021794326554_734760932040845010_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=QsDLzI6DeQUAX8p5BSK&_nc_ht=scontent.fsgn2-4.fna&oh=00_AfAIwAg7MucIN8iskrLTWJI7m2Qyi2H87Ri8iJ--Enu2wQ&oe=63902362"
             alt="Viet"
             style="width:100%">
        <div class="container">
          <h2>Quoc Viet</h2>
          <p class="title">CEO & Founder</p>
          <p>LEADER</p>
          <p>vietvmq@smartgift.vn</p>
          <p><button class="button">Liên Hệ</button></p>
        </div>
      </div>
    </div>

    <div class="column">
      <div class="card">
        <img
            src="https://scontent.fvca1-1.fna.fbcdn.net/v/t1.6435-9/118564241_329363171596166_1873332451438417099_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=09MQMNMer8oAX9SP9uh&_nc_ht=scontent.fvca1-1.fna&oh=00_AfCLvDfZ7Gpwl4Cx-DHDpyphTjsGGiDZHldsG3q-7OrPkg&oe=638FF06F"
            alt="Huy"
            style="width:100%">
        <div class="container">
          <h2>Van Huy</h2>
          <p class="title">Thành Viên</p>
          <p>MEMBER</p>
          <p>huytv@gmail.com</p>
          <p><button class="button">Liên Hệ</button></p>
        </div>
      </div>
    </div>

    <div class="column">
      <div class="card">
        <img src="https://zpsocial-f49-org.zadn.vn/734cf6a35c13b34dea02.jpg"
             alt="Doan"
             style="width:100%">
        <div class="container">
          <h2>Cong Doan</h2>
          <p class="title">Thành Viên</p>
          <p>MEMBER</p>
          <p>Doancc@gmail.com</p>
          <p><button class="button">Liên Hệ</button></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutUs',
};
</script>

<style scoped>
body {
  font-family: Arial, Helvetica, sans-serif;
  margin: 0;
}

html {
  box-sizing: border-box;
}

*, *:before, *:after {
  box-sizing: inherit;
}

.column {
  float: left;
  width: 33.3%;
  margin-bottom: 16px;
  padding: 0 8px;
}

.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  margin: 8px;
}

.about-section {
  padding: 20px;
  text-align: center;
  background-color: #dcbba8;
  color: white;
}

.container {
  padding: 0 16px;
}

.container::after, .row::after {
  content: "";
  clear: both;
  display: table;
}

.title {
  color: grey;
}

.button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
}

.button:hover {
  background-color: #555;
}

@media screen and (max-width: 650px) {
  .column {
    width: 100%;
    display: block;
  }
}

</style>
