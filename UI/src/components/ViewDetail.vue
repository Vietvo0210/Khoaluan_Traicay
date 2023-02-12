<template>
  <div class="container">
          <div class="row">
              <div class="col-12 text-center">
              </div>
          </div>
          <div class="row">
              <div class="mr-top">
                  <form v-if="posts">
                      <div class="product-detail row">
                        <div class="col-6" placeholder="{{ post.title }}">
                          <a href="#"><img
                          class="img-first img-sp"
                          :src="posts.thumbnail"
                          alt="Err"/>
                        </a>
                        </div>
                        <div class="col-6"> 
                          <section class="text-dl">
                            <a>
                          <label>Type of fruit:</label>
                          {{posts.title}}
                        </a>
                          </section>
                        <br>
                        <section class="text-c">
                          <a>
                          <label>Price:</label>
                          {{posts.price}}
                        </a>
                        <br>
                        <a>
                          <label>Discount:</label>
                          {{posts.discount}} %
                        </a>
                        <br>
                        <a>
                          <label>Details of the fruit:</label>
                          {{posts.description}}
                        </a>
                        </section>
                        </div>
                      </div>
                  </form>
              </div>
              <div class="col-3"></div>
          </div>
      </div>
  </template>
  
  <script>
  
  export default {
    name: 'ViewDetail',
    
    data() {
              return {
                posts: null,
                id: null,
              }
          },
          methods: {
    async getData() {
      try {
        let response = await fetch("http://192.168.1.26:8089/api/product-detail/"+this.$route.params.id+"/");
        this.posts = await response.json();
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getData();
  },
  }
  
  </script>
  
<style scoped>
  
  .mr-top{
    margin-top: 50px;
  }

  .img-sp{
    height: 400px;
  }
  .text-dl{
    font-size: 18px;
  }
  .text-c{
    font-size: 14px;
    text-align: center;
  }
</style>
