<template>
  <!-- Search component Alert with name of type,  press Ctrl + F -->

  <div class="alert h-auto p-3">
    <nav class="flex" aria-label="Breadcrumb">
      <ol class="inline-flex items-center space-x-1 md:space-x-3">
        <li class="inline-flex items-center">
          <a
            href="#"
            class="inline-flex items-center text-sm font-medium text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
          >
            <svg
              class="mr-2 w-4 h-4"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"
              ></path>
            </svg>
            Dashboard
          </a>
        </li>
        <li>
          <div class="flex items-center">
            <svg
              class="w-6 h-6 text-gray-400"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                clip-rule="evenodd"
              ></path>
            </svg>
            <a
              href="#"
              class="ml-1 text-sm font-medium text-gray-700 hover:text-gray-900 md:ml-2 dark:text-gray-400 dark:hover:text-white"
              >Components</a
            >
          </div>
        </li>
        <li>
          <div class="flex items-center">
            <svg
              class="w-6 h-6 text-gray-400"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                clip-rule="evenodd"
              ></path>
            </svg>
            <a
              href="#"
              class="ml-1 text-sm font-medium text-gray-700 hover:text-gray-900 md:ml-2 dark:text-gray-400 dark:hover:text-white"
              >Trái Cây</a
            >
          </div>
        </li>
      </ol>
    </nav>
    <!-- end nav -->
    <div class="mt-5 w-full">
      <h1 class="text-2xl text-gray-900 font-medium dark:text-gray-200">
        Trái Cây
      </h1>
      <p class="mt-1 text-sm font-normal text-gray-400">
        Trái cây Việt Nam là một tổng hợp những loại trái cây được trồng và phát triển tại Việt Nam. Trong số đó có rất nhiều loại trái cây đặc sản được xuất khẩu ra nước ngoài, có thể kể đến như Măng cụt Lái Thiêu, Bơ sáp Lâm Đồng, Sầu riêng Ri6, Xoài cát chu vàng, .vv...

        Trái cây giàu vitamin và khoáng chất từ tự nhiên, giúp bạn bổ sung dinh dưỡng, cải thiện sức khỏe, duy trì sắc đẹp và chống lại bệnh tật. 

      </p>
    </div>
    <!-- grid wrapper card -->
    <div class="grid lg:grid-cols-2 grid-col-1 gap-4 mt-5">
      
      <!-- Chuối  -->
      <div class="card bg-white dark:bg-gray-800 w-full rounded-md p-5 shadow ">
        <h2 class="dark:text-gray-1000">Trái Chuối</h2>
        <div class="wrapper-alert grid grid-cols-1 gap-3 mt-3">
          <div>
            
            Hình Ảnh
          </div>
          
        </div>
      </div>  
      <!-- Xoài  -->
      <div class="card row-span-2 bg-white dark:bg-gray-800 w-full rounded-md p-5 shadow ">
        <h2 class="dark:text-gray-1000">Trái Xoài</h2>
        <div class="wrapper-alert grid grid-cols-1 gap-3 mt-3">
          <div>
            
            Hình Ảnh
          </div>
          
        </div>
      </div> 
      <!-- Trái  -->
      <div class="card row-span-2 bg-white dark:bg-gray-800 w-full rounded-md p-5 shadow ">
        <h2 class="dark:text-gray-1000">Trái Xoài</h2>
        <div class="wrapper-alert grid grid-cols-1 gap-3 mt-3">
          <div>
            
            Hình Ảnh
          </div>
          
        </div>
      </div> 
      <!-- Trái  -->
      <div class="card row-span-3 bg-white dark:bg-gray-800 w-full rounded-md p-5 shadow ">
        <h2 class="dark:text-gray-1000">Trái...</h2>
        <div class="wrapper-alert grid grid-cols-1 gap-3 mt-3">
          <div>
            
            Hình Ảnh
          </div>
          
        </div>
      </div> 
      <!-- Trái  -->
      <div class="card row-span-4 bg-white dark:bg-gray-800 w-full rounded-md p-5 shadow ">
        <h2 class="dark:text-gray-1000">Trái...</h2>
        <div class="wrapper-alert grid grid-cols-1 gap-3 mt-3">
          <div>
            
            Hình Ảnh
          </div>
          
        </div>
      </div> 
    </div>
  </div>
</template>

<script>
  import { Icon } from "@iconify/vue";
  export default {
    components: {
      Icon,
    },
    mounted() {
      var alert_dis = document.querySelectorAll(".alert-dismiss");
      alert_dis.forEach((x) =>
        x.addEventListener("click", function () {
          x.parentElement.classList.add("hidden");
        })
      );
    },
  };
</script>
