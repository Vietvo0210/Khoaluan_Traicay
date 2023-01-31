<template>
<div class="container">
        <div class="row">
            <div class="col-12 text-center">
            </div>
        </div>
        <div class="row">
            <div class="col-3"></div>
            <div class="col-6">
                <form v-if="posts">
                    <div class="product-detail">
                      <a href="#"><img
                        class="img-fluid w-100 mb-3 img-first"
                        :src="posts.thumbnail"
                        alt="Err"/>
                      </a>
                      <a>
                        <label>Loại quả:</label>
                        {{posts.title}}
                      </a>
                      <br>
                      <a>
                        <label>Giá:</label>
                        {{posts.price}}
                      </a>
                      <br>
                      <a>
                        <label>Giảm giá:</label>
                        {{posts.discount}} %
                      </a>
                      <br>
                      <a>
                        <label>Chi tiết loại quả:</label>
                        {{posts.description}}
                      </a>
                      
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
      let response = await fetch("http://10.1.14.234:8089/api/product-detail/"+this.$route.params.id+"/");
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

</style>
